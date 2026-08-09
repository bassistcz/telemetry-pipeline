import sqlite3

DB_PATH = "../database/readings.db"

con = sqlite3.connect(DB_PATH)

rows = con.execute(
    "SELECT * FROM temp_readings"
).fetchall()

for row in rows:
    print(row)

con.close()