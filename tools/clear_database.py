import sqlite3

DB_PATH = "../database/readings.db"

con = sqlite3.connect(DB_PATH)

con.execute("DELETE FROM temp_readings;")

con.commit()
con.close()