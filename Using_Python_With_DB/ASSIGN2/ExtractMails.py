import sqlite3

#creare db
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()         #get hanlde

#remove the table from the db if exists
cur.execute('DROP TABLE IF EXISTS Counts')

#create new table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('mbox-short.txt')

for line in fh:
    if line.startswith('From: '):
        #count number of orginization that has this email
        email = line.split('@')[1].rstrip()

        cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))

        #if no one has it then insert new organization to the table
        if cur.fetchone() is None:
            cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
       #else increment it by 1
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
conn.commit()

#print emails that we get from the txt file
cur.execute('SELECT * from Counts')
for r in cur:
    print(r)
    
cur.close()