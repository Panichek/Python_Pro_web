import sqlite3
import random

conn = sqlite3.connect('instance/project.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS record (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')

for _ in range(100000):
    name = "Name" + str(_)
    score = random.randint(0, 100)
    cursor.execute('INSERT INTO Record (name, score) VALUES (?, ?)', (name, score))


conn.commit()
conn.close()

print("Базу даних створено!")
