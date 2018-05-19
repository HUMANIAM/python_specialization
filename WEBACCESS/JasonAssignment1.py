import json
import urllib.request, urllib.parse, urllib.error as urlReq, urlPar, urlErr

url = 'http://py4e-data.dr-chuck.net/comments_23429.json'
js = json.loads(urlReq.urlopen(url).read().decode())
sum = 0

for item in js['comments']:
    sum = sum + int(item['count'])

print(sum)
