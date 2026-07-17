# SentinelLog

A lightweight Security Log Analysis Framework built in Python for detecting suspicious activity in web server access logs.

SentinelLog parses Apache-style access logs, aggregates request statistics, identifies malicious behavior, assigns risk scores, and generates actionable security insights.

Designed as a portfolio project demonstrating cybersecurity fundamentals, object-oriented design, efficient data structures, and modular detection logic.

---

## Features

### Log Parsing

- Parses Apache access logs
- Creates structured Request objects
- Aggregates activity per IP address

### Detection Engine

Currently implemented:

- Brute Force Detection
- Reconnaissance Detection

Planned:

- Directory Enumeration
- Burst Traffic Detection
- Credential Stuffing Detection
- HTTP Method Abuse
- Risk-Based Alert Prioritization

### Risk Scoring

Every IP receives a cumulative risk score based on triggered detections.

Example:

203.0.113.50

Risk Score: 45

Detections:
- Brute Force
- Reconnaissance

---

## Project Structure

```
SentinelLog/
│
├── __main__.py
├── parser.py
├── detection.py
├── models.py
├── sample_access.log
└── README.md
```

---

## Architecture

```
              Apache Log
                   │
                   ▼
             Parser Module
                   │
                   ▼
           Request Objects
                   │
                   ▼
            IP Aggregation
                   │
                   ▼
          Detection Modules
                   │
                   ▼
            Risk Assessment
                   │
                   ▼
          Security Findings
```

---

## Detection Logic

### Brute Force Detection

Flags IP addresses with excessive failed authentication attempts.

Indicators:

- Large number of HTTP 401 responses
- Configurable threshold

---

### Reconnaissance Detection

Detects attempts to discover sensitive resources.

Examples:

- /.env
- /admin
- /.git
- /config.php
- /backup.zip

The detector tracks unique sensitive resources requested by each IP.

---

## Data Structures

The project intentionally uses efficient data structures.

### Request Object

Represents a single HTTP request.

Stores:

- IP Address
- Timestamp
- HTTP Method
- Resource
- Status Code
- Response Size

---

### IP Object

Aggregates statistics for each IP.

Stores:

- Total Requests
- Successful Requests
- Failed Requests
- 404 Responses
- Risk Score
- Detection Flags
- Suspicious Resources

---

### Hash Table

A Python dictionary maps

```
IP Address
        ↓
IP Object
```

allowing O(1) lookups during analysis.

---

## Complexity

Parsing

O(n)

Brute Force Detection

O(number of IPs)

Reconnaissance Detection

O(number of Requests)

---

## Future Improvements

- CLI interface
- JSON report generation
- HTML reports
- Multiple log format support
- Real-time monitoring
- Configurable detection rules
- Unit testing
- Logging
- Timestamp-based analysis
- Plugin-based detector architecture

---

## Example Output

```
=========================================
Security Analysis Report
=========================================

High Risk IP

203.0.113.50

Risk Score: 45

Detections

✓ Brute Force
✓ Reconnaissance

Evidence

Failed Logins : 30

Sensitive Resources

/admin
/.env
/.git
/config.php
```

---

## Technologies

- Python 3
- Object-Oriented Programming
- Dictionaries (Hash Tables)
- Modular Architecture

---

## Why This Project?

This project was built to demonstrate practical cybersecurity concepts beyond simple scripting.

It focuses on:

- Secure software design
- Efficient data processing
- Detection engineering
- Modular architecture
- Clean code practices

rather than simply parsing log files.

---

## License

MIT License
