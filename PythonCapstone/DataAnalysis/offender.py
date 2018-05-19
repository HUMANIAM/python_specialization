import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import os
import sqlite3

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:\'\"\,<>./?@#$%^&*_~+'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lastStatements = open('lastStatements.txt', 'w')
wrdsStatistics = open('wds_statistics.txt', 'w')
wrds_statstics = dict()

#connect to the DB
conn = sqlite3.connect("offenders.sqlite")
cur  = conn.cursor()

'''
def SortWords():
	try:
		Lwrds = list((k, d[k]) for k in wrds_statstics)
		j= len(wrds_statstics)-1
		#selction sort to the words
		while(j>0):
			minv = wrds_statstics[j][1]
			minindex = j

			for k in range(0, j+1):
				if l[k][1] < minv: 
					minv = wrds_statstics[k][1]
					minindex = k

			temp = wrds_statstics[j]
			wrds_statstics[j] = wrds_statstics[minindex]
			wrds_statstics[minindex] = temp
			j = j - 1
		print(wrds_statstics)
	except:
		print("an error occurs during sorting operation")
	return
'''

def RecordWords(id, statement):
	#record the statement into the DB
	lastStatements.write("\n\n" + statement)
	cur.execute('''INSERT OR IGNORE INTO Laststaments (id, laststament)
				VALUES ( ?, ? )''' , (id, statement) )

	#count occurenece of words in the statement
	x= 'This offender declined to make.'
	if not statement.startswith(x):
		word_tokens = word_tokenize(statement)
		filterFn = lambda x: x not in stop_words and x not in punctuations
		words = list(filter(filterFn, word_tokens))

		for wrd in words:
			occur = wrds_statstics.get(wrd, 0)
			wrds_statstics[wrd] = occur + 1
	return

#Get the the last statement of the offenders
def GetStatement(id, html):
	lststatm = ''
	try:
		soup = BeautifulSoup(html, "html.parser")
		pTags = soup('p')
		found = False
		txt = ''		
		for p in pTags:
			span = p.find('span')
			if span is not None : txt = (span.text).strip()
			else:  txt = (p.text).strip()

			if found : 
				lststatm = txt
				RecordWords(id, lststatm)
				return lststatm
			if txt.startswith('Last Statement:'):
				found = True
		return None
	except KeyboardInterrupt:
	    print('\nProgram interrupted by user...')
	    quit()
	except:
		print('failed to retreive:', url)
		return None 

#getfields function gets the rest information about the offender
#from its information page and write these info into the DB
def Get(ptags, field, stop):
	res = ''
	for p in ptags:
		ptxt = p.text
		getrest = False

		if ptxt.startswith(field):
			span = p.find('span')
			if span is not None:
				res =   ptxt[ptxt.find('\n') : ]
				getrest = True
				continue
			else: return res

		if  ptxt.startswith(stop):
			return res
		if getrest:
			res = res + ptxt
	return res

def getfields(tag, soup):
	tags = soup(tag)
	#get the gender and native state of the offender
	if tag == 'tr':
		gender = ntvestate = ''
		for tr in tags:
			tdTags = tr.findAll('td')
			txt = tdTags[1].text
			if txt == 'Gender': 
				gender = tdTags[2].text
			elif txt == 'Native State': 
				ntvestate = tdTags[2].text
			else: continue
			 
		return [gender, ntvestate]

	#get prior occupation, vicitims, incidents
	elif tag is 'p':
		po = Get(tags, 'Prior Occupation', 'Prior Prison')
		if po ==  '': po = "unknown"

		soi = Get(tags, 'Summary of Incident', 'Co-Defendants')
		if soi == '': soi = "unknown"

		ragof = Get(tags, 'Race and Gender of Victim', 'xxxx')
		if ragof == '': ragof = "unknown"
		
		return [po, soi, ragof] 
#get inforamtion and last statement of offenders
def InsertInfo(url, what, id):
	try:
		document = urlopen(url, context=ctx)
		html = document.read()
		code = document.getcode()
		err = 0
		ID = str(id)
		if code == 200 :	#it is okey
			if what == 'statement':
				state = GetStatement(id, html.decode())
				if state is None:
					print("failed to statement: ", url)
					err = 1
				print("success to statement: ", url)
			else:
				command1 = '''UPDATE Offenders SET gendre = ?, nativeState=?, prior_occupation=?,
				 				incidents=?, victims=? WHERE id=?'''
				command2 = '''UPDATE OffenderPages SET htmlInfo =? where id = ?'''

				#if the information page is image 
				if url.endswith('.jpg') :
					cur.execute(command2 ,(ID, id))
					cur.execute('''INSERT OR IGNORE INTO Images (id, image)
						VALUES ( ?, ? )''' , (ID, html) )
					cur.execute(command1, (ID, ID, ID, ID, ID, id))
				#if the informatin page is html
				else:
					soup = BeautifulSoup(html, "html.parser")
					cur.execute(command2 ,(memoryview(html), id))

					#read required information about the offender
					#get gender, native state
					lst1 = getfields('tr', soup)
					#get prior occupation, vicitims, incidents
					lst2 = getfields('p', soup)
					#insert into the offender table these information
					cur.execute(command1, (lst1[0], lst1[1], lst2[0], lst2[1], lst2[2], id))
				print('successed to info:', url) 
		else:
			err = 1
			print('failed to page(code is not 200): ', url)
			quit()
		return err
	except KeyboardInterrupt:
	    print('\nProgram interrupted by user...')
	    quit() 

	except:
		return 1

#insert or update words in the database		
def WriteStatistics():
	cur.execute('SELECT * FROM Words')
	words = {w[0]:w[1] for w in cur}

	for wrd in wrds_statstics:
		if wrd not in words :
			cur.execute('''INSERT OR IGNORE INTO Words (word, occurs)
				VALUES ( ?, ? )''' , (wrd, wrds_statstics[wrd]) )
		else:
			cur.execute('''UPDATE Words SET
				occurs =? where word = ?''',(wrd, wrds_statstics[wrd]))
	conn.commit()
	return

#get the rest information about the offender
def GetInfo():
	try:
		# * (id, urlinfo, urlstatement, err1, err2, htmlInfo)
		cur.execute('''SELECT * FROM OffenderPages
			WHERE err1 = 0 AND htmlInfo is NULL''')
		urls = [(r[0], r[1], r[2]) for r in cur]

		c = 0
		for row in urls:
			id = row[0]
			err1 = InsertInfo(row[1], 'info', id)

			if err1 == 0:
				err2 = InsertInfo(row[2], 'statement', id)
				c = c + 1
				if err2 != 0 :
					cur.execute('UPDATE OffenderPages SET err2=? WHERE id=?', (err2, id))
			else:
				cur.execute('UPDATE OffenderPages SET err1=? WHERE id=?', (err1, id))

			if c%20 == 0:
				WriteStatistics()
				c=0
			conn.commit()
	except KeyboardInterrupt:
	    print('\nProgram interrupted by user...')
	    quit() 



def main():
	#Texas Department of Criminal Justic
	GetInfo()
	WriteStatistics()	
	conn.close()
if __name__ == '__main__':
	main()