"""
this program like crawler To some extent
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter ')
count = int(input('Count : '))
position = int(input('Position : '))

# Retrieve all of the anchor tags

while(count > 0 and url != None):
	print(url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')

	#get the http and https urls only
	urls = list(map(lambda x: x.get('href', None), tags))
	fltr = lambda x: (x != None ) and (x.startswith("http") or x.startswith("https"))
	urls = list(filter(fltr, urls))

	if (len(urls) <= position - 1) : 
		url = None
	else: url = urls[position-1]

	count = count - 1
	pass
if url != None:
	print(url)
	print(tag.contents[0])
else: print("sorrry it none ")



