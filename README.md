# Telemetry Pipeline
A modular telemetry ingestion pipeline built with Python, MQTT, Docker, and SQLite.

The project is designed as a learning platform for modern software engineering practices, including message-driven architectures, IoT communication, data persistence, testing, and observability.

## Features

- Dockerised Mosquitto MQTT broker
- Python telemetry simulator
- MQTT consumer service
- JSON schema validation
- Modular project structure
- Designed to support both simulated and physical sensors

## Project Goal
Build a modular telemetry platform capable of:

- ingesting telemetry from simulated and physical sensors
- validating incoming messages
- storing telemetry for historical analysis
- visualising system state
- experimenting with reliability and fault injection
- exploring Digital Twin concepts

## Current Architecture
```
+-------------+      MQTT      +-------------+      +-------------+
| Simulator   | ─────────────▶ | Mosquitto   | ───▶ | Consumer    |
+-------------+                +-------------+      +-------------+
                                                         │
                                                         ▼
                                                     Validation
                                                         │
                                                         ▼
                                                      SQLite
                                                         │
                                                         ▼
                                                Dashboard (planned)
```

## Current Status
### Completed
✅ Repository structure
✅ Docker Compose environment
✅ Mosquitto MQTT broker
✅ Python sensor simulator
✅ MQTT consumer
✅ JSON schema validation
✅ Sensor-specific schemas
✅ SQLite persistence

### In Progress
🚧 Structured logging

### Planned
- Multiple sensor support
- Unit testing
- Grafana dashboards
- Authentication
- TLS
- Fault injection

## Repository Structure

```
telemetry-pipeline/
├── config/            # Configuration files
├── consumer/          # MQTT consumer service
├── database/          # Database scripts
├── docs/              # Project documentation
├── logs/              # Log files for testing and debug
├── mosquitto/         # Mosquitto broker configuration
├── simulator/         # Telemetry simulator
├── tests/             # Tests
├── tools/             # Helper scripts
├── docker-compose.yml # Local development environment
├── README.md
├── ROADMAP.md
└── LICENSE
```


## Prerequisites
- Docker
- Python 3.11+
- Git

## Quick Start

Clone the repository.

```
git clone git@github.com:bassistcz/telemetry-pipeline.git
cd telemetry-pipeline
```

Start the MQTT broker.

```
docker compose up -d
```

Verify the broker is running.

```
docker ps
```

You should see the Mosquitto container running.

### Configure MQTT Authentication (Optional)

Open a shell inside the broker container.

```
docker exec -it mosquitto sh
```

Create a user.

```
mosquitto_passwd /mosquitto/config/pwfile <username>
```

Restart the broker.

```
docker restart mosquitto
```

## Simulator

Create a virtual environment.
```
cd simulator

python3 -m venv .venv
```

Activate it
```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create a .env file 

```
simulator/.env
```

With the following:
```
MQTT_USERNAME=<user>
MQTT_PASSWORD=<password>
```

Run the simulator from the telemetry/ directory with the command

```
python -m simulator.src.simulator
```

## Consumer

Create a virtual environment.

```
cd consumer

python3 -m venv .venv
```

Activate it
```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create a .env file 

```
consumer/.env
```

with the following:
```
MQTT_BROKER=localhost
MQTT_PORT=1883
MQTT_TOPIC=building/room1/temperature
MQTT_CLIENT_ID=consumer
MQTT_USERNAME=<user>
MQTT_PASSWORD=<password>
```

Run the consumer from the telemetry/ directory 
```
python -m consumer.src.main
```


## Manual testing

Install MQTT client tools

```
sudo apt install mosquitto-clients
```

Subscribe to a topic

Without authentication
```
mosquitto_sub -v -t 'hello/topic'
```

With authentication
```
mosquitto_sub -h localhost -p 1883 -v -t 'hello/topic' -u <user> -P <password>
```

This will appear to hang until you publish a message.

Publish a message

In a separate terminal run one of the following commands:

Without authentication
```
mosquitto_pub -t 'hello/topic' -m 'hello MQTT'
```

With authentication
```
mosquitto_pub -t 'hello/topic' -m 'hello MQTT' -u <user> -P <password>
```

The subscriber should receive:

```
hello/topic hello MQTT
```


## Documentation

Additional project documentation can be found in the docs/ directory.

- `ROADMAP.md` — planned milestones and future features
- `docs/architecture.md` — system architecture
- `docs/decisions.md` — technical decisions and rationale

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned milestones and future features.


## License

This project is licensed under the MIT License.

