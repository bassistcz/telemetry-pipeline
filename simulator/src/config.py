import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

TOPIC = "building/room1/temperature"

SENSOR_ID = "temp_sensor_001"

MIN_TEMP = 10.0
MAX_TEMP = 24.0

PUBLISH_INTERVAL = 10