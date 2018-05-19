from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import os
import sqlite3

conn = sqlite3.connect("offenders.sqlite")
cur  = conn.cursor()

''' *table for offenders information
	*table for who is retreived who is not
	*table for Words and it is occurence
'''
cur.executescript('''
	DROP TABLE IF EXISTS OffenderPages;
	DROP TABLE IF EXISTS Offenders;
	DROP TABLE IF EXISTS Laststaments;
	DROP TABLE IF EXISTS Images;
	DROP TABLE IF EXISTS Words;

	CREATE TABLE IF NOT EXISTS OffenderPages (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    urlinfo, urlstatement TEXT,
    err1 INTEGER DEFAULT 0.0,	--for inforamtion page
    err2 INTEGER DEFAULT 0.0,	--for laststatemt page
    htmlInfo TEXT
);
CREATE TABLE IF NOT EXISTS Offenders (
    id  INTEGER,
    name TEXT NOT NULL,
    age int NOT NULL,
    gendre, nativeState, race TEXT,
    prior_occupation, incidents TEXT,
    victims, DODR TEXT,   --date of death row
    CONSTRAINT OFFUNIQUE UNIQUE(id, name)
);
CREATE TABLE IF NOT EXISTS Laststaments(
id INTEGER,
laststament TEXT  NULL,
CONSTRAINT laststUNIQUE UNIQUE(id, laststament)
);
CREATE TABLE IF NOT EXISTS Images(
id INTEGER, 
image BLOB,
CONSTRAINT imageUNIQUE UNIQUE(id, image)

);
CREATE TABLE IF NOT EXISTS Words (
    word  TEXT NOT NULL PRIMARY KEY UNIQUE,
    occurs INTEGER
);

''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#extract the important data of offenders row by row
def ExtractInfo(html):
	soup = BeautifulSoup(html, "html.parser")
	trTags = soup('tr')
	c = 0
	values = list()

	for tr in trTags:
		tdTags = tr.findAll('td')
		vals = []

		for td in tdTags:
			atag = td.find('a')
			if atag is not None:
				vals.append(atag.get('href', None))
			else:
				vals.append(td.text)

		if len(vals) > 0:
			values.append(vals) 
			c = c + 1
	return values

#start fetch offenders from this page and then find last statements
def findurls(url):
	basurl = url[:url.rfind('/')]
	basurl = url[:basurl.rfind('/')]
	try:
		html = urlopen(url, context=ctx).read().decode()
	except:
		print("can't retreive : ", url)
		quit()
	
	rows = ExtractInfo(html)
	'''row fields are: Execution number, offender information, laststatement,
	   last name, first name, tdcj number, age, date, race, county'''
	count = 0
	hrefst = hrefinfo = ''

	for row  in rows:
		#url of information
		href = row[1]
		if href is not None :
			if href.startswith('/death_row'):
				hrefinfo = basurl + href
			else:
				hrefinfo = basurl+ '/death_row/' + href

		#url of last statement
		href = row[2] 
		if href is not None :
			if href.startswith('/death_row'):
				hrefst = basurl + href
			else:
				hrefst = basurl+ '/death_row/' + href

		#offender name
		name = row[4] + row[3]

		cur.execute('''INSERT OR IGNORE INTO OffenderPages (urlinfo, urlstatement)
				VALUES ( ?, ? )''' , (hrefinfo, hrefst) )
		cur.execute('''SELECT id FROM OffenderPages 
			WHERE urlinfo=? AND urlstatement=?''', ((hrefinfo, hrefst)))
		id = cur.fetchone()[0]

		cur.execute('''INSERT OR IGNORE INTO Offenders 
			(id, name, age, race, DODR) VALUES (?, ?, ?, ?, ?)''',
			(id, name, row[6], row[8], row[7]))	

		count = count + 1
		if(count % 20) == 0:
			conn.commit()
	conn.commit()
	cur.close()
	return count

def main():
	#Texas Department of Criminal Justic
	url = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"
	count = findurls(url)
	print("there are " , count, "offenders")

if __name__ == '__main__':
	main()
