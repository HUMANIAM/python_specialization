import sqlite3
#make connection to the sqlite file
conn = sqlite3.connect('music.sqlite')

#create file handler to the DB
cur = conn.cursor()

#drop command
cur.execute('DROP TABLE IF EXISTS Tracks')

#create new table with some attrs with Create command
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

#Insert commands 
cur.execute('INSERT INTO Tracks (title, plays) VALUES (\'hello\', 5)' )

#(?,?) USES TO REFERS THAT VAULES IN TUBLE
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))  

#force the data to be written to the data base file
conn.commit()   

#update command
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = \'hello\'')
conn.commit()
 
#tuple with one element (element,)
#choose only one row
#r = cur.fetchone()
#select command to retrieve data
cur.execute('SELECT title, plays FROM Tracks WHERE plays != 5')
for row in cur:
	print(row)

# Delete command
cur.execute('DELETE FROM Tracks WHERE plays<10')

conn.close()