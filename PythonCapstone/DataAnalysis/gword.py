import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('offenders.sqlite')
cur = conn.cursor()

cur.execute('SELECT laststament FROM Laststaments')
counts = dict()

for statement in cur :
    statement = statement[0]
    statement = statement.translate(str.maketrans('','',string.punctuation))
    statement = statement.translate(str.maketrans('','','1234567890'))
    statement = statement.strip().lower()
    words = statement.split()
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1

x = sorted(counts, key=counts.get, reverse=True)
fh = open('words.txt', 'w')
for k in x:
    fh.write(k + " : " + str(counts[k]) + "\n")
highest = None
lowest = None
key= ''
for k in x[:100]:
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:', highest, lowest)

# # Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [\n")
diff = float(highest - lowest)
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / diff
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

# print("Output written to gword.js")
# print("Open gword.htm in a browser to see the vizualization")
