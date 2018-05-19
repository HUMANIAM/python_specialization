import urllib.request, urllib.parse, urllib.error as urlReq, urlPar, urlErr
import xml.etree.ElementTree as ET
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #parse url and get data from that location
    url = serviceurl + urlPar.urlencode({'address': address})
    print('Retrieving', url)
    data = urlReq.urlopen(url).read().decode()
    

    try:
        js = json.loads(data)
    except:
        js = None

    #check integrity of data
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #retrieve data according to its locations        
    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    

    