# telemetry-pipeline
A small telemetry ingestion pipeline using MQTT, Python, SQLite and Docker.

## Setup
Clone repo

Run

```
 sudo docker compose -p mosquitto up -d
```

test if broker is up, by running
```
$ docker ps
```

should see something like this
```
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                                                                NAMES
740fcdb1bf79   eclipse-mosquitto    "/docker-entrypoint.…"   7 seconds ago   Up 6 seconds   0.0.0.0:1883->1883/tcp, [::]:1883->1883/tcp                                          mosquitto
```

add a password

```
$ docker exec -it mosquitto sh
```

add password for user
```
mosquitto_passwd /mosquitto/config/pwfile <username>
```

restart container
```
sudo docker restart <container id>
```

## Test

Install client

```
sudo apt install mosquitto-clients
```

### Start a topic
Without authentication
```
mosquitto_sub -v -t 'hello/topic'
```

With authentication
```
mosquitto_sub -h localhost -p 1883 -v -t 'hello/topic' -u <user> -P <password>
```

This will appear to hang until you publish a message.

### Publish to the topic
In a separate terminal run one of the following commands:

Without authentication
```
mosquitto_pub -t 'hello/topic' -m 'hello MQTT'
```

With authentication
```
mosquitto_pub -t 'hello/topic' -m 'hello MQTT' -u <user> -P <password>
```

You should see
```
hello/topic hello MQTT
```
print out in the first terminal.

## Setup simulator venv
```
cd ~/telemetry-pipeline/simulator

python3 -m venv .venv
```

activate
```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run
```
python src/simulator.py
```

## Test simulator venv

```
export MQTT_USERNAME=<username>
export MQTT_PASSWORD=<password>

python src/simulator.py
```

To store the username and password
add the file
```
simulator/.env
```

with the following:
```
MQTT_USERNAME=<user>
MQTT_PASSWORD=<password>
```

then next time you can run
```
python src/simulator.py
```

## Setup consumer venv
```
cd ~/telemetry-pipeline/consumer

python3 -m venv .venv
```

activate
```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

To store the username and password
add the file
```
simulator/.env
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

Run the 
```
python src/main.py
```