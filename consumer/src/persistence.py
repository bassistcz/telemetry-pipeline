import sqlite3
import logging
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "database" / "readings.db"

logger = logging.getLogger(__name__)


def connect_database():
    return sqlite3.connect(DB_PATH)


def close_database(con):
    con.commit()
    con.close()


def initialise_database():

    
    logger.info("Initialising database...")
    
    con = connect_database()
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS temp_readings(
            version INTEGER, 
            sensor_id TEXT,
            reading_id TEXT, 
            sensor_type TEXT, 
            timestamp TEXT, 
            value REAL, 
            unit TEXT)"""
    )

    close_database(con)
    logger.info("Database initialised successfully.")


def store_reading(message):
    version = message["version"]
    sensor_id = message["sensor_id"]
    reading_id = message["reading_id"]
    sensor_type = message["sensor_type"]
    timestamp = message["timestamp"]
    value = message["value"]
    unit = message["unit"]

    con = connect_database()
    cur = con.cursor()

    logger.info(
                "Storing reading: sensor_id=%s, reading_id=%s, value=%s%s",
                message["sensor_id"],
                message["reading_id"],
                message["value"],
                message["unit"]
                )
    logger.debug("Storing reading: %s", message)

    cur.execute(
        "INSERT INTO temp_readings VALUES (?, ?, ?, ?, ?, ?, ?)",
        (version, sensor_id, reading_id, sensor_type, timestamp, value, unit),
    )

    close_database(con)
