import time

from config import SENSOR_ID, PUBLISH_INTERVAL
from sensor import TemperatureSensor
from publisher import publish_sensor_data


def main():
    sensor = TemperatureSensor(SENSOR_ID)

    while True:
        reading = sensor.read()

        publish_sensor_data(reading)

        time.sleep(PUBLISH_INTERVAL)


if __name__ == "__main__":
    main()
