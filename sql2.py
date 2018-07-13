import sqlite3
conn = sqlite3.connect("D:/Python/databases/sql1.db")
cur = conn.cursor()
cur.execute('SELECT ENAME FROM ENTERPRISE')
out = cur.fetchall()
for i in out:
    print i
