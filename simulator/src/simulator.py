import time
import logging
from simulator.src.config import SENSOR_ID, PUBLISH_INTERVAL
from simulator.src.sensor import TemperatureSensor
from simulator.src.publisher import publish_sensor_data
from config.logging_config import configure_logging


def main():
    configure_logging("simulator")
    sensor = TemperatureSensor(SENSOR_ID)

    logger = logging.getLogger(__name__)
    logger.info("Starting temperature sensor simulation...")

    while True:
        logger.debug("Reading temperature...")
        reading = sensor.read()

        logger.debug(f"Publishing sensor data: {reading}")
        publish_sensor_data(reading)

        time.sleep(PUBLISH_INTERVAL)


if __name__ == "__main__":
    main()
