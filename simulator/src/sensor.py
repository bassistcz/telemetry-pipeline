import random
import datetime
from simulator.src.config import MIN_TEMP, MAX_TEMP

class TemperatureSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.timestamp = "2026-08-05T20:20:00Z"
        self.temperature = 17.0
        self.unit = "C"

    def read(self):
        # small random drift rather than pure random noise
        self.temperature += random.uniform(-0.5, 0.5)

        self.temperature = max(
            MIN_TEMP,
            min(MAX_TEMP, self.temperature)
        )
        self.timestamp = datetime.datetime.now().isoformat( )

        return {
            "version": 1,
            "sensor_id": self.sensor_id,
            "sensor_type": "temperature",
            "timestamp": str(self.timestamp),
            "value": round(self.temperature, 2),
            "unit": self.unit
        }
