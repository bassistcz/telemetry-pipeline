import json
from jsonschema import validate, ValidationError
from pathlib import Path

SCHEMA_DIR = Path(__file__).parent / "schemas"

with open(SCHEMA_DIR / "temperature_schema.json") as f:
    temperature_schema = json.load(f)

#future: add humidity and pressure schemas
# with open(SCHEMA_DIR / "schemas/humidity.json") as f:
#     humidity_schema = json.load(f)

# with open(SCHEMA_DIR / "schemas/pressure.json") as f:
#     pressure_schema = json.load(f)


SCHEMAS = {
    "temperature": temperature_schema,
    # future: add humidity and pressure schemas
    # "humidity": humidity_schema,
    # "pressure": pressure_schema,
}


def validate_message(message):
    sensor_type = message.get("sensor_type")

    schema = SCHEMAS.get(sensor_type)

    if schema is None:
        raise ValueError(f"Unknown sensor type: {sensor_type}")

    validate(
        instance=message,
        schema=schema
    )

    return True