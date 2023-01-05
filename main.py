import sqlite3
import xml.etree.ElementTree as ET


# Connect to database
conn = sqlite3.connect("Musicdb.sqlite")
cur = conn.cursor()


# Drop table if the table already existed
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
    
    
CREATE TABLE Artist(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT UNIQUE
    );
    
CREATE TABLE Album(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Artist_id INTEGER,
        Title TEXT
    );
    
CREATE TABLE Track(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Album_id INTEGER,
        Title TEXT,
        Lenght INTEGER, Rating INTEGER, Count INTEGER
    );
                  ''')


# Open the XML file
with open("Library.xml", "r") as hand:
    fhand = hand.read()

   
all = ET.fromstring(fhand)
data = all.findall("dict/dict/dict")

def lookfor(a , b):
    found = False
    for c in a :
        if found:
            return c.text
        if c.tag == "key" and c.text == b:
            found = True
    return None
   
for bit in data:
    if (lookfor(bit, "Track ID")) is None:
        continue
        
    # Extract values from data
    name = lookfor(bit ,"Name")
    artist = lookfor(bit, 'Artist')
    album = lookfor(bit, 'Album')
    count = lookfor(bit, 'Play Count')
    rating = lookfor(bit, 'Rating')
    length = lookfor(bit, 'Total Time')
    
    if name is None or artist is None or album is None : 
        continue
    
    print(name, artist, album, count, rating, length)
    print("\n")
    
    # Insert values into Artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    
    # Extract artist_id from Artist
    cur.execute('SELECT Id FROM Artist WHERE Name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    # Insert values into Album
    cur.execute('''INSERT OR IGNORE INTO Album (Title, Artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    
    # Extract album_id from Album
    cur.execute('SELECT Id FROM Album WHERE Title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # Insert values into Track
    cur.execute('''INSERT OR REPLACE INTO Track
        (Title, Album_id, lenght, Rating, Count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )

    # Close databse
    conn.commit()
    
    
