import xml.etree.ElementTree as ET
import urllib.request as urlReq

input = urlReq.urlopen('http://py4e-data.dr-chuck.net/comments_23428.xml').read().decode()
stuff = ET.fromstring(input) 
lst = stuff.findall('comments/comment') 
sum = 0
for item in lst: 
	sum = sum + int(item.find('count').text)
print(sum)
	
