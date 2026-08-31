import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "readings.db"

con = sqlite3.connect(DB_PATH)

con.execute("DELETE FROM temp_readings;")

con.commit()
con.close()