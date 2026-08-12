# Technical Decisions

This document records important architectural and technical decisions made during the development of the Telemetry Pipeline project.

The goal is to capture *why* decisions were made, not just *what* was implemented.

---

# Decision 001 - Use MQTT for telemetry transport

**Status:** Accepted

## Decision

Use MQTT as the messaging protocol between telemetry producers and consumers.

## Rationale

- Lightweight protocol designed for IoT.
- Decouples sensors from downstream consumers.
- Supports multiple publishers and subscribers.
- Easy to replace simulated sensors with physical devices later.

## Consequences

### Positive

- Highly scalable architecture.
- Real devices can be added with minimal changes.
- Components remain loosely coupled.

### Negative

- Requires running a broker.
- Adds another moving part to the system.

---

# Decision 002 - Use Mosquitto as the MQTT broker

**Status:** Accepted

## Decision

Use Eclipse Mosquitto running in Docker.

## Rationale

- Widely used MQTT broker.
- Lightweight.
- Easy to deploy.
- Excellent for development and learning.

## Future Considerations

Could later evaluate HiveMQ or EMQX for larger deployments.

---

# Decision 003 - Simulated sensors before physical hardware

**Status:** Accepted

## Decision

Develop against simulated telemetry before introducing physical sensors.

## Rationale

- Faster development.
- Repeatable testing.
- No hardware dependency.
- Easier debugging.

## Consequences

The simulator should eventually become just another telemetry source rather than special-case code.

---

# Decision 004 - Validate incoming telemetry

**Status:** Accepted

## Decision

Validate all incoming messages before processing.

## Rationale

- Reject malformed data early.
- Prevent invalid data reaching persistence.
- Keep processing logic simple.
- Make failures explicit.

---

# Decision 005 - Separate schemas by sensor type

**Status:** Accepted

## Decision

Maintain separate schemas for each sensor type.

## Rationale

Avoid one large schema attempting to support every possible sensor.

Examples:

- temperature
- humidity
- pressure
- battery
- GPS

Each sensor type can evolve independently.

---

# Decision 006 - Docker-first development

**Status:** Accepted

## Decision

Run infrastructure inside Docker.

## Rationale

- Consistent environments.
- Easy onboarding.
- Simple deployment.
- Closer to production workflows.

Current Docker services:

- Mosquitto

Future services:

- SQLite (if required)
- Grafana
- Prometheus
- InfluxDB
- PostgreSQL

---

# Decision 007 - SQLite for initial persistence

**Status:** Accepted

## Decision

Use SQLite for Version 1.

## Rationale

- Zero configuration.
- Easy inspection.
- Lightweight.
- Good enough for learning and local development.

## Future Considerations

Potential migration to:

- PostgreSQL
- InfluxDB
- TimescaleDB

---

# Decision 008 - Prioritise modularity over optimisation

**Status:** Accepted

## Decision

Prefer small, well-defined modules rather than highly optimised code.

## Rationale

The purpose of this project is to learn software engineering practices.

Readability and maintainability take priority over micro-optimisations.

---

# Decision 009 - Keep simulated and physical sensors interchangeable

**Status:** Proposed

## Decision

Design the simulator so that physical sensors publish identical message formats.

## Rationale

Consumers should not know whether telemetry originated from:

- Python simulator
- Raspberry Pi Pico
- ESP32
- Arduino
- Embedded C++
- Rust

Only the publisher changes.

---

# Decision 010 - Build iteratively

**Status:** Accepted

## Decision

Develop the system through small, working milestones.

## Rationale

Each milestone should leave the project in a runnable state.

Avoid large branches or extensive unfinished work.

The project should remain deployable after every milestone.
