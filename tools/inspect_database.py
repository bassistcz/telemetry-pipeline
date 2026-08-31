import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "readings.db"

con = sqlite3.connect(DB_PATH)

rows = con.execute(
    "SELECT * FROM temp_readings"
).fetchall()

for row in rows:
    print(row)

con.close()