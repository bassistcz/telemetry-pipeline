# Telemtry Pipeline V1
```
   Sensor Simulator (Temperature)
        |
        v
     MQTT Broker
    (Mosquitto)
        |
        v
 MQTT Consumer
        |
        +--> Validation
        |
        +--> Processing
        |
        v
    Persistence
    (SQLite)
        |
        v
 Visualisation
 ```