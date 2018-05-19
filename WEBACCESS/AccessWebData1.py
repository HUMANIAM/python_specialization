"""
in this simple program we try parse html page to its tags
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

#parse the html page to its tags as a dict (tag:values)
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
    pass

print(sum)