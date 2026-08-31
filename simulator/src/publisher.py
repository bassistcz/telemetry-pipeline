import json
import paho.mqtt.publish as publish
import logging
import time

logger = logging.getLogger(__name__)

from simulator.src.config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    TOPIC
)


def publish_sensor_data(data):
    start_time = time.monotonic()

    try:
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
    except Exception:
        logger.exception(
            "MQTT publish failed: sensor_id=%s topic=%s",
            data.get("sensor_id"),
            TOPIC,
        )
        raise

    duration_ms = (time.monotonic() - start_time) * 1000

    logger.info(
        "MQTT publish succeeded: sensor_id=%s reading_id=%s topic=%s duration_ms=%.2f",
        data.get("sensor_id"),
        data.get("reading_id"),
        TOPIC,
        duration_ms,
    )