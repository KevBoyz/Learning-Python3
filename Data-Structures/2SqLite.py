import sqlite3 as sql

conn = sql.connect('assets/data_base')
conn.execute("""CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        number TEXT NOT NULL UNIQUE
    )
""")

conn.execute("INSERT INTO contacts (name, email, number) \
      Values ('Kevin', 'k@bz', 555)")
conn.execute("INSERT INTO contacts (name, email, number) \
      Values ('Prs2', 'pers@xn', 777)")
# conn.commit()

cursor = conn.execute('SELECT id, name, email, number FROM contacts where id=1')
[print(f'Hello {row[1]}!') for row in cursor]
