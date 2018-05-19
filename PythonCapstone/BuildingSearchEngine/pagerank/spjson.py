import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

print("Creating JSON output on spider.js...")
howmany = int(input("How many nodes? "))

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound''')

fhand = open('spider.js','w')
nodes = list(row for row in cur)[:howmany+1]
maxrank = max({row[2] for row in nodes})
minrank = min({row[2] for row in nodes})

if maxrank == minrank or maxrank is None or minrank is None:
    print("Error - please run sprank.py to compute page rank")
    quit()

fhand.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
div = (maxrank - minrank)
for row in nodes :
    if count > 0 : fhand.write(',\n')
    ranks[row[3]] = rank = row[2]
    map[row[3]] = count
    rank = 19 * ( (rank - minrank) / div  ) 
    fhand.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    fhand.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    count = count + 1
fhand.write('],\n')

cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
fhand.write('"links":[\n')

count = 0
for row in cur :
    if row[0] not in map or row[1] not in map : continue
    if count > 0 : fhand.write(',\n') 
    fhand.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1
fhand.write(']};')
fhand.close()
cur.close()

print("Open force.html in a browser to view the visualization")
