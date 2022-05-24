import sqlite3

conn = sqlite3.connect('database.db')
with open('schema.sql') as file:
    conn.executescript(file.read())
cursor = conn.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('#1 Post', 'Content of this motherfucker website')
               )
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('#2 Post', 'Content of this motherfucker website')
               )

conn.commit()
conn.close()