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
conn.commit()

conn.execute('DELETE FROM contacts where id=2')
conn.execute('UPDATE contacts SET number = 999 where name="Kevin"')
user = conn.execute('SELECT id, name, email, number FROM contacts where id=1')
[print(f'Hello {row[1]}! ({row[3]}) is your number') for row in user]
