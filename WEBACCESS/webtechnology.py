"""
in this program we restore plain text from data.pr4e.org
"""

import socket
import urllib.request,  urllib.error
import time
from bs4 import BeautifulSoup

#create socket in Tcp connection to communicate with the outside world
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  		#TCP connection 
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() 
mysock.send(cmd)

#receive the returned data from the site
fh = open('return_data.txt', 'w')
while True:
	data = mysock.recv(1024)
	if (len(data) < 1):
		break
	fh.write(data.decode())
mysock.close()

"""
in this program we retrieve an image from data.pr4e.org
"""
"""
HOST = 'data.pr4e.org' 
PORT = 80 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect((HOST, PORT))
cmd = 'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) 

picture = b""   #declare bytes variable
while True: 
	data = mysock.recv(5120) 
	if (len(data) < 1): break 
	time.sleep(0.25) 
	picture = picture + data
mysock.close()


# Skip past the header and save the picture data 
pos = picture.find(b"\r\n\r\n") 
picture = picture[pos+4:] 
fhand = open("stuff.jpg", "wb") 
fhand.write(picture) 
fhand.close()
"""
"""
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
for line in fhand: print(line.decode().strip())"""
"""
html = urllib.request.urlopen("https://www.coursera.org/learn/python-network-data/lecture/S4FIR/worked-example-beautifulsoup-chapter-12").read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
print(tags)
for tag in tags:
	#print(tag.get('href', None))
	pass
"""