import sqlite3
import urllib.error
import ssl
import sys
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Spider(object):

    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.conn = sqlite3.connect('spider.sqlite')
        self.cur = self.conn.cursor()
        self.InitProgram()
        self.Start()
        self.Crawel()

    def InitProgram(self):
        # Ignore SSL certificate errors
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Pages
            (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
            error INTEGER, old_rank REAL DEFAULT 0.0, new_rank REAL DEFAULT 1.0)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Links
            (from_id INTEGER, to_id INTEGER,
            CONSTRAINT rUNIQUE UNIQUE (from_id, to_id))''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

    def Start(self):
        # Check to see if we are already in progress or we begin crawling new web site
        self.cur.execute('''SELECT id,url FROM Pages 
            WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1''')

        row = self.cur.fetchone()
        if row is not None:
            print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")
        else :
            starturl = input('Enter web url or enter: ')
            if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
            if ( starturl.endswith('/') ) : starturl = starturl[:-1]
            web = starturl

            #get web site of this html page
            if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
                pos = starturl.rfind('/')
                web = starturl[:pos]
            if ( len(web) > 1 ) :
                self.cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) )
                self.cur.execute('''INSERT OR IGNORE INTO Pages (url, html) 
                    VALUES ( ?, NULL )''', ( starturl, ) )
                self.conn.commit()
                self.cur.execute('SELECT url from Webs where url = ?', ( web, ) )

    def Crawel(self):
        # Get the current webs
        self.cur.execute('''SELECT url FROM Webs''')
        webs = list()
        for row in self.cur:
            webs.append(str(row[0]))
        print(webs)

        many = 0
        while True:
            if ( many < 1 ):
                sval = input('How many pages:')
                if ( len(sval) < 1 or int(sval) < 1) : break
                many = int(sval)
            many = many - 1

            #choose one page not yet retreived to retreive it
            self.cur.execute('''SELECT id,url FROM Pages 
            WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1''')

            try:
                row = self.cur.fetchone()
                fromid = row[0]
                url = row[1]
            except:
                print('No unretrieved HTML pages found')
                break
            print(fromid, url, end=' ')

            # If we are retrieving this page, there should be no links from it
            self.cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) )
            try:
                document = urlopen(url, context=self.ctx)
                html = document.read()
                code = document.getcode() 
                if code != 200 :
                    print("Error on page: ",document.getcode())
                    self.cur.execute('UPDATE Pages SET error=? WHERE url=?', (code, url) )
                    self.conn.commit()
                    continue

                if 'text/html' != document.info().get_content_type() :
                    print("Ignore non text/html page")
                    #cur.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
                    self.cur.execute('UPDATE Pages SET error=-2 WHERE url=?', (url, ) )
                    self.conn.commit()
                    continue

                print('('+str(len(html))+')', end=' ')

            except KeyboardInterrupt:
                print('\nProgram interrupted by user...')
                break 
            except:
                print("Unable to retrieve or parse page")
                self.cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
                self.conn.commit()
                continue

            self.cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
            self.conn.commit()
            self.PageATages(url, html, fromid, webs)
        self.cur.close()

    def PageATages(self, url, html, fromid, webs):
        soup = BeautifulSoup(html, "html.parser")
        # Retrieve all of the anchor tags
        tags = soup('a')
        count = 0

        #pass through a tags and choose only what is appropriate then clean it
        for tag in tags:
            href = tag.get('href', None)
            if ( href is None ) : continue
            
            # Resolve relative references like href="/contact"
            up = urlparse(href)
            if ( len(up.scheme) < 1 ) :
                href = urljoin(url, href)
            strtwth = href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif')
            ipos = href.find('#')
            if ( ipos > 1 ) : href = href[:ipos]
            if ( strtwth )  : continue
            if ( href.endswith('/') ) : href = href[:-1]
            if ( len(href) < 1 ) : continue

            # Check if the URL is in any of the webs
            found = False
            for web in webs:
                if ( href.startswith(web) ) :
                    found = True
                    break
            if not found : continue
   
            self.cur.execute('''INSERT OR IGNORE INTO Pages (url, html) 
                VALUES ( ?, NULL)''', ( href, ) )
            self.conn.commit()

            try:
                self.cur.execute('SELECT id FROM Pages WHERE url = ? LIMIT 1', (href,))
                toid = self.cur.fetchone()[0]
                if toid != fromid:
	                self.cur.execute('''INSERT OR IGNORE INTO Links (from_id, to_id) 
	                    VALUES ( ?, ? )''', ( fromid, toid ) )
	                count = count + 1
            except:
                print('Could not retrieve id for \n', href)
                continue

        print(count)    
        
def main():
    sp = Spider()
if __name__=="__main__":
    main()