import json
import paho.mqtt.publish as publish

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    TOPIC
)


def publish_sensor_data(data):
    publish.single(
        TOPIC,
        json.dumps(data),
        hostname=MQTT_BROKER,
        port=MQTT_PORT,
        auth={
            "username": MQTT_USERNAME,
            "password": MQTT_PASSWORD
        }
    )