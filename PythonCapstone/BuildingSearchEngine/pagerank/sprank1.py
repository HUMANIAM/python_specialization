# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links

import sqlite3
import functools

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

#all from ids
cur.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids = list(row[0] for row in cur)

#proper to ids
cur.execute('''SELECT DISTINCT to_id FROM Links''')
fil_toID = lambda v: v in from_ids
to_ids = list(filter(fil_toID, {row[0] for row in cur}))

#proper links to pages with bidirectional links
cur.execute('''SELECT * FROM Links''')
filt_links = lambda row: row[1] in from_ids
links = list(filter(filt_links, {row for row in cur}))

#find list of toids of every from node
give_ids = dict()
for (from_id, to_id) in links:
    if from_id in give_ids:
        give_ids[from_id].append(to_id)
    else:
        give_ids[from_id] = [to_id]

# intializing page ranks for strongly connected component
prev_ranks = dict((node, 1.0) for node in from_ids)

sval = input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)
if many == 0: quit()

# Sanity check
if len(to_ids) < 1 : 
    print("there are no pages has inbound and also outbound. Check data.")
    quit()

# Lets do Page Rank in memory so it is really fast
for i in range(many):
    next_ranks = dict((node, 0.0) for node in from_ids)
    total = functools.reduce((lambda x, y: x + y), prev_ranks.values())

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):
        amount = old_rank / len(give_ids[node])
    
        for id in give_ids[node]:
            next_ranks[id] = next_ranks[id] + amount
    
    newtot = functools.reduce((lambda x, y: x + y), next_ranks.values())
    evap = (total - newtot) / len(next_ranks)

    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap
        
    prev_ranks = next_ranks

# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('UPDATE pages SET old_rank = new_rank')
for (id, new_rank) in list(next_ranks.items()) :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()

