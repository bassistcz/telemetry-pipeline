# telemetry-pipeline
A small telemetry ingestion pipeline using MQTT, Python, SQLite and Docker.

## Setup
Clone repo

Run

```
 sudo docker compose -p mqtt5 up -d
```

test if broker is up, by running
```
$ docker ps
```

should see something like this
```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                                                                      NAMES
92000e1b3c33   eclipse-mosquitto    "/docker-entrypoint.…"   43 seconds ago   Up 41 seconds   0.0.0.0:1883->1883/tcp, [::]:1883->1883/tcp, 0.0.0.0:9001->9001/tcp, [::]:9001->9001/tcp   mqtt5
```

add a password

```
$ docker exec -it mqtt5 sh
```

add password for user
```
mosquitto_passwd /mosquitto/config/pwfile <username>
```

restart container
```
sudo docker restart <container id>
```
