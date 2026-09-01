import paho.mqtt.client as mqtt
from consumer.src.validate import validate_message
from jsonschema import ValidationError
import json
from consumer.src.persistence import store_reading
import logging


from consumer.src.config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_TOPIC,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_CLIENT_ID,
)

logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        logger.info("Connected to broker")
        client.subscribe(MQTT_TOPIC)
        logger.info(f"Subscribed to {MQTT_TOPIC}")
    else:
        logger.error(f"Connection failed: {reason_code}")


def on_message(client, userdata, message):
    
    payload = message.payload.decode()

    logger.debug(f"[{message.topic}] {payload}")

    process_message(payload)


def create_client():
    logger.info("Creating MQTT client...")
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id=MQTT_CLIENT_ID,
    )

    if MQTT_USERNAME:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    logger.info("MQTT client created successfully.")
    return client


def process_message(payload):

    try:
        message = json.loads(payload)
        if validate_message(message):
            logger.info(
                        "Valid telemetry received: sensor_id=%s, reading_id=%s, sensor_type=%s",
                        message["sensor_id"],
                        message["reading_id"],
                        message["sensor_type"],
            )
            logger.debug("Telemetry message: %s", message)

            store_reading(message)
            
            logger.info("Message processed successfully.")

    except json.JSONDecodeError:
        logger.error("Invalid JSON received")

    except ValidationError as e:
        logger.error(f"Bad telemetry message: {e.message}")

    except ValueError as e:
        logger.error(f"Error processing message: {e}")


def run():
    logger.info("Starting MQTT client...")
    client = create_client()

    logger.info(f"Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}...")
    client.connect(MQTT_BROKER, MQTT_PORT)

    logger.info("Connected to MQTT broker. Awaiting messages...")
    client.loop_forever()