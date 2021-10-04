#importing sqlite3
import sqlite3

#connecting to database
conn = sqlite3.connect('filmlists.db')

#creating a cursor
curr = conn.cursor()

#creating a table
curr.execute(""" CREATE TABLE movies_namess (
                MOVIE_NAME text,
                ACTOR text,
                ACTRESS text,
                DIRECTOR text,
                YEAR_OF_RELEASE int
            )""")

#inserting data into table
all_movies = [
              ('Roohi                  ','Raajkumar Rao        ','Jhanvi Kapoor           ','Hardik Mehta',                 2021),
              ('Kabir Singh            ','Shahid Kapoor        ','Kiara Adwani            ','Sandeep Reddy Vanga',          2019),
              ('Andhadhun              ','Ayushman Khurrana    ','Radika Apte             ','Sriram Raghavan',              2018),
              ('Chhichhore             ','Sushant Singh        ','Shraddha Kapoor         ','Nitesh Tiwari',                2019),
              ('Kesari                 ','Akshay Kumar         ','Parineethi Chopra       ','Anurag Singh',                 2019),
              ('Ludo                   ','Abhishek Bachchan    ','Sanya Malhotra          ','Anurag Basu',                  2020),
              ('Sulthan                ','Salman Khan          ','Anushka Sharma          ','Ali Abbas Zafar',              2016),
              ('Rockstar               ','Amitabh Bachchan     ','Taapsee Pannu           ','Sujoy Ghosh',                  2019),
              ('Badla                  ','Ranbir Kapoor        ','Nargis Fakhri           ','Imitiaz Ali',                  2011),
              ('Aashiqui 2             ','Adithya Roy          ','Shraddha Kapoor         ','Mohit Suri',                   2013),
            ]

curr.executemany("INSERT INTO movies_namess VALUES (?,?,?,?,?)", all_movies)


#commiting the connection
conn.commit()

#closing the connection
conn.close()