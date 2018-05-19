from urllib.request import urlopen 
import urllib.parse, urllib.error
import json 
import sqlite3 
import ssl

parms = dict()
parms["query"] = "AGH University of Science and Technology"
parms["key"]   = "AIzaSyAJINCcdkKjStU9Y_LE3HgzW2nnI9__0wQ"
print("https://maps.googleapis.com/maps/api/place/textsearch/json?"+urllib.parse.urlencode(parms))
