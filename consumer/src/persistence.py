import sqlite3

DB_PATH = "../database/readings.db"


def connect_database():
    return sqlite3.connect(DB_PATH)


def close_database(con):
    con.commit()
    con.close()


def initialise_database():
    
    con = connect_database()
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS temp_readings(
            version INTEGER, 
            sensor_id TEXT, 
            sensor_type TEXT, 
            timestamp TEXT, 
            value REAL, 
            unit TEXT)"""
    )

    close_database(con)


def store_reading(message):
    version = message["version"]
    sensor_id = message["sensor_id"]
    sensor_type = message["sensor_type"]
    timestamp = message["timestamp"]
    value = message["value"]
    unit = message["unit"]

    con = connect_database()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO temp_readings VALUES (?, ?, ?, ?, ?, ?)",
        (version, sensor_id, sensor_type, timestamp, value, unit),
    )

    close_database(con)
