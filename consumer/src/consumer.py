import paho.mqtt.client as mqtt
from validate import validate_message
from jsonschema import ValidationError
import json

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_TOPIC,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_CLIENT_ID,
)


def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Connected to broker")
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to {MQTT_TOPIC}")
    else:
        print(f"Connection failed: {reason_code}")


def on_message(client, userdata, message):
    payload = message.payload.decode()

    print(f"[{message.topic}] {payload}")

    process_message(payload)


def create_client():
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id=MQTT_CLIENT_ID,
    )

    if MQTT_USERNAME:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    return client


def process_message(payload):
    message = json.loads(payload)

    try:
        validate_message(message)

        print("Valid telemetry:")
        print(message)

        # store_reading(message)  # future SQLite storage

    except json.JSONDecodeError:
        print("Invalid JSON received")

    except ValidationError as e:
        print(f"Bad telemetry message: {e.message}")

    except ValueError as e:
        print(e)


def run():
    client = create_client()

    client.connect(MQTT_BROKER, MQTT_PORT)

    client.loop_forever()