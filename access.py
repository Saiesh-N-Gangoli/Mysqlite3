#importing sqlite
import sqlite3

#connecting to database
conn = sqlite3.connect('filmlists.db')

#creating a cursor
curr = conn.cursor()

#Quering the database
curr.execute("SELECT * FROM movies_namess")
items=curr.fetchall()
for item in items:
    print(str(item[0]) + "\t"+ str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t"+ str(item[4]) + "\t\t ")

#commit changes to database
conn.commit()

#close the connection
conn.close()