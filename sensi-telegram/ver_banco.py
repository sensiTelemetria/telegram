import sqlite3

conn = sqlite3.connect('sensi.db')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM reg""")

conn.commit()

query = (cursor.fetchall())
for reg in query:
    print(reg)