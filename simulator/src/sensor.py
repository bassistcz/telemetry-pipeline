import random
from config import MIN_TEMP, MAX_TEMP

class TemperatureSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.temperature = 17.0

    def read(self):
        # small random drift rather than pure random noise
        self.temperature += random.uniform(-0.5, 0.5)

        self.temperature = max(
            MIN_TEMP,
            min(MAX_TEMP, self.temperature)
        )

        return {
            "sensor_id": self.sensor_id,
            "temperature": round(self.temperature, 2)
        }
