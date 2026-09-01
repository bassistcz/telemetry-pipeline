import sqlite3
import logging
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "database" / "readings.db"

logger = logging.getLogger(__name__)


def connect_database():
    return sqlite3.connect(DB_PATH)


def initialise_database():
    logger.info("Initialising database...")

    with connect_database() as con:
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS temp_readings(
                version INTEGER,
                sensor_id TEXT,
                reading_id TEXT NOT NULL,
                sensor_type TEXT,
                timestamp TEXT,
                value REAL,
                unit TEXT
            )"""
        )

        cur.execute(
            """CREATE UNIQUE INDEX IF NOT EXISTS idx_temp_readings_reading_id
            ON temp_readings(reading_id)"""
        )

    logger.info("Database initialised successfully.")


def store_reading(message):
    version = message["version"]
    sensor_id = message["sensor_id"]
    reading_id = message["reading_id"]
    sensor_type = message["sensor_type"]
    timestamp = message["timestamp"]
    value = message["value"]
    unit = message["unit"]

    logger.info(
        "Storing reading: sensor_id=%s, reading_id=%s, value=%s%s",
        sensor_id,
        reading_id,
        value,
        unit,
    )
    logger.debug("Storing message: %s", message)

    with connect_database() as con:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO temp_readings (
                version,
                sensor_id,
                reading_id,
                sensor_type,
                timestamp,
                value,
                unit
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                version,
                sensor_id,
                reading_id,
                sensor_type,
                timestamp,
                value,
                unit,
            ),
        )
