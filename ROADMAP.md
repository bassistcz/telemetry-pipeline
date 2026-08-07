# Telemetry Pipeline Roadmap

## Project Goal

Build a modular telemetry platform capable of ingesting simulated and real sensor data, validating messages, storing readings, and visualising system state.

### Future Direction

- Support physical IoT devices
- Fault injection and resilience testing
- Digital Twin experimentation
- Operational dashboards
- Learn modern software engineering practices through iterative development

---

# Current Architecture

```text
Sensor Simulator
        │
        ▼
 MQTT Broker
 (Mosquitto)
        │
        ▼
 MQTT Consumer
        │
        ├── Validate Message
        ├── Process Message
        └── Persist Reading
                │
                ▼
            SQLite
                │
                ▼
        Dashboard / Analytics
```

---

# Milestones

## v0.1 – Pipeline Foundation ✅

**Goal**

Prove telemetry can flow end-to-end.

### Completed

- [x] Initial repository structure
- [x] Docker Compose environment
- [x] Mosquitto MQTT broker
- [x] Python sensor simulator
- [x] MQTT publishing
- [x] MQTT consumer
- [x] JSON schema validation
- [x] Sensor-specific schemas
- [x] Basic message processing

---

## v0.2 – Data Persistence

**Goal**

Store validated telemetry for historical analysis.

### Tasks

- [ ] Design SQLite schema
- [ ] Persist validated readings
- [ ] Separate persistence into its own module
- [ ] Add database abstraction layer

---

## v0.3 – Observability

**Goal**

Understand what the system is doing.

### Tasks

- [ ] Structured logging
- [ ] Message processing metrics
- [ ] Error reporting
- [ ] Sensor status monitoring
- [ ] Grafana dashboard

---

## v0.4 – Multiple Devices

**Goal**

Support multiple independent telemetry sources.

### Tasks

- [ ] Multiple simulated sensors
- [ ] Additional sensor types
- [ ] Sensor registry
- [ ] Device metadata
- [ ] Heartbeat messages

---

## v0.5 – Reliability & Security

**Goal**

Move towards production-quality engineering.

### Tasks

- [ ] MQTT authentication
- [ ] TLS encryption
- [ ] Configuration improvements
- [ ] Retry handling
- [ ] Health checks
- [ ] Graceful shutdown

---

## v0.6 – Fault Injection & Digital Twin

**Goal**

Simulate realistic operating environments.

### Tasks

- [ ] Random sensor failures
- [ ] Network interruptions
- [ ] Invalid telemetry generation
- [ ] Battery drain simulation
- [ ] Expected operating ranges
- [ ] Alert generation

---

# Engineering Improvements

These are ongoing improvements rather than milestone-specific work.

- [ ] Unit tests
- [ ] Integration tests
- [ ] Continuous Integration (GitHub Actions)
- [ ] Improve documentation
- [ ] Code refactoring
- [ ] Packaging and releases

---

# Long-Term Ideas

- Physical sensors (Raspberry Pi Pico, ESP32, Arduino)
- Sensor implementations in multiple languages (Python, C++, C, Rust, Ada)
- PostgreSQL or InfluxDB backend
- REST API
- Web frontend
- Kubernetes deployment
- Cloud deployment
- Digital Twin visualisation
- Machine learning for anomaly detection

---

# Current Priority

The recommended next steps are:

1. Persist readings to SQLite
2. Refactor persistence into its own module
3. Add structured logging
4. Add unit tests
5. Build an initial dashboard