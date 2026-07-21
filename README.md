# SentinelLog

**SentinelLog** is a Python-based command-line security log analysis and threat detection tool designed to analyze web server access logs, identify suspicious behavior, and present security findings through a structured terminal interface.

SentinelLog parses log entries, builds per-IP activity profiles, applies rule-based detection techniques, and reports potentially suspicious behavior such as:

* Brute-force attempts
* Web reconnaissance
* Suspicious resource probing
* HTTP method abuse

The project is designed as a lightweight defensive cybersecurity tool and as a practical implementation of log analysis and rule-based threat detection concepts.

> **Current Version:** `0.1.0`

---

## Features

### Log Parsing and Validation

SentinelLog processes web server access logs and separates successfully parsed entries from malformed or unsupported entries.

The processing summary includes:

* Total log entries
* Valid log entries
* Invalid log entries
* Successfully parsed percentage

Example:

```text
╭──────────────── Log Processing Summary ────────────────╮
│                                                        │
│   Total Log Entries                         169        │
│   Valid Logs                                169        │
│   Invalid Logs                                0        │
│   Successfully Parsed                     100.0%       │
│                                                        │
╰────────────────────────────────────────────────────────╯
```

Malformed or unsupported entries are counted separately instead of being treated as successfully parsed requests.

---

### Per-IP Activity Tracking

SentinelLog creates an activity profile for each IP address encountered during analysis.

The analyzer can track information such as:

* Total requests
* Successful requests
* Failed authentication attempts
* HTTP `404 Not Found` responses
* Suspicious resources accessed
* Suspicious HTTP methods
* Triggered detections
* Flagged status
* Risk indicators

This allows SentinelLog to correlate multiple suspicious events with the same source IP instead of analyzing every request independently.

---

## Detection Engine

SentinelLog currently implements three primary detection mechanisms.

### 1. Brute-Force Detection

The brute-force detector identifies IP addresses generating repeated failed authentication attempts.

Repeated authentication failures can indicate behavior such as:

* Password guessing
* Credential attacks
* Automated login attempts
* Repeated unauthorized authentication attempts

Example detection output:

```text
BRUTE FORCE

Total Attempts:  49
Failed Attempts: 30
```

The detector evaluates authentication failures associated with each IP and flags activity when the configured detection conditions are met.

---

### 2. Reconnaissance Detection

Reconnaissance commonly occurs when an attacker attempts to discover sensitive resources, administrative interfaces, configuration files, or other useful information before attempting further exploitation.

SentinelLog tracks requests to potentially sensitive or commonly targeted resources such as:

```text
/admin
/phpmyadmin
/wp-admin
/.env
/config.php
/backup.zip
/server-status
/dashboard
```

The analyzer can also use repeated `404 Not Found` responses as an additional reconnaissance indicator.

A large proportion of `404` responses may indicate automated directory or resource enumeration, where an attacker attempts many possible paths to discover which resources exist.

Example:

```text
RECONNAISSANCE

┏━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Resource    ┃ Requests ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ /admin      │       15 │
│ /phpmyadmin │        1 │
│ /wp-admin   │        1 │
│ /.env       │        1 │
│ /config.php │        1 │
└─────────────┴──────────┘
```

This detector can help identify behavior consistent with:

* Administrative panel discovery
* Directory enumeration
* Resource enumeration
* Configuration-file probing
* Sensitive-file discovery
* Automated vulnerability scanning

---

### 3. HTTP Method Abuse Detection

SentinelLog can detect HTTP methods that are not included in the configured allowed-method list.

For example, a basic web application may normally expect:

```text
GET
POST
```

Requests using methods outside the configured allowlist are recorded as suspicious.

Depending on the application, these may include methods such as:

```text
PUT
DELETE
TRACE
CONNECT
PATCH
OPTIONS
```

These methods are **not inherently malicious**.

For example, REST APIs commonly use `PUT`, `PATCH`, and `DELETE`, while browsers may legitimately send `OPTIONS` requests for CORS preflight operations.

For this reason, the allowed-method configuration should reflect the application or server being analyzed.

SentinelLog records suspicious methods per IP and tracks how frequently each one occurs.

Example:

```text
HTTP METHOD ABUSE

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Suspicious Method ┃ Requests ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ TRACE             │        4 │
│ DELETE            │        2 │
└───────────────────┴──────────┘
```

---

## Security Alert Reporting

When suspicious activity is detected, SentinelLog flags the associated IP address and generates a security alert.

A single IP may trigger multiple detection categories.

Example:

```text
╭──────────────────── SECURITY ALERT ────────────────────╮
│ IP Address:  203.0.113.50                              │
│ Status:      FLAGGED                                   │
│ Detections:  Brute Force, Reconnaissance, Method Abuse │
╰────────────────────────────────────────────────────────╯
```

Detailed evidence for each triggered detection is displayed below the alert.

This makes it easier to identify cases where several suspicious behaviors originate from the same source.

---

## CLI Interface

SentinelLog uses the **Rich** Python library to provide a structured command-line interface.

When SentinelLog starts, it displays the application banner and asks the user to provide the path of the log file to analyze.

```text
╭──────────────────────── Security Analyzer ───────────────────────╮
│                                                                 │
│    SENTINELLOG                                                  │
│    Security Log Analysis & Detection Tool                       │
│                                                                 │
│    Version 0.1.0                                                │
│                                                                 │
╰──────────────────── Analyze • Detect • Assess ───────────────────╯

╭──────────────────────── Log File Selection ─────────────────────╮
│                                                                 │
│  Enter the path to the access log you want to analyze.          │
│  Example: C:\logs\access.log                                    │
│                                                                 │
╰─────────────────────────────────────────────────────────────────╯

Log file path:
```

The analysis workflow is:

```text
Start SentinelLog
       │
       ▼
Enter Log File Path
       │
       ▼
Validate File
       │
       ▼
Parse Log Entries
       │
       ▼
Build Per-IP Profiles
       │
       ▼
Run Detection Engine
       │
       ├── Brute Force
       ├── Reconnaissance
       └── HTTP Method Abuse
       │
       ▼
Display Analysis Results
```

---

## Project Structure

A simplified representation of the project structure:

```text
Security-Log-Analyzer/
│
├── sentinel/
│   ├── __init__.py
│   ├── __main__.py
│   ├── parser.py
│   ├── detection.py
│   └── ...
│
├── Test/
│   └── sample_access.log
│
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

The project uses three related names:

```text
Project / Distribution:  SentinelLog / sentinellog
Python Package:          sentinel
CLI Command:             sentinellog
```

The internal Python source package is therefore:

```text
sentinel/
```

while users launch the application using:

```bash
sentinellog
```

---

# Installation

## Requirements

SentinelLog requires:

* Python 3.10 or newer
* pip

Required Python dependencies, including `rich`, are installed automatically when declared through `pyproject.toml`.

---

## Option 1 — Install from Source

Clone the repository:

```bash
git clone https://github.com/hellice121/Security-Log-Analyzer.git
```

Enter the project directory:

```bash
cd Security-Log-Analyzer
```

### Create a Virtual Environment

Using a virtual environment is recommended to keep SentinelLog and its dependencies isolated.

Create one:

```bash
python -m venv .venv
```

### Activate the Virtual Environment

#### Windows — Command Prompt

```cmd
.venv\Scripts\activate.bat
```

#### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

Once activated, install SentinelLog:

```bash
python -m pip install .
```

Run the application:

```bash
sentinellog
```

---

## Option 2 — Development / Editable Installation

If you want to modify SentinelLog or contribute to the project, install it in editable mode.

Clone the repository:

```bash
git clone https://github.com/hellice121/Security-Log-Analyzer.git
```

Enter the repository:

```bash
cd Security-Log-Analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it using the appropriate command for your operating system.

Then install SentinelLog in editable mode:

```bash
python -m pip install -e .
```

Now run:

```bash
sentinellog
```

Editable mode means changes made to the Python source code are generally reflected the next time SentinelLog runs without reinstalling the package after every code change.

If packaging metadata or dependencies in `pyproject.toml` are changed, reinstalling may still be necessary.

---

## Running SentinelLog as a Python Module

SentinelLog can also be launched directly through its internal Python package:

```bash
python -m sentinel
```

This executes:

```text
sentinel/__main__.py
```

The normal user-facing CLI command remains:

```bash
sentinellog
```

---

## CLI Entry Point

The terminal command is configured through `pyproject.toml`.

```toml
[project.scripts]
sentinellog = "sentinel.__main__:main"
```

This creates the following execution flow:

```text
sentinellog
     │
     ▼
sentinel.__main__
     │
     ▼
main()
     │
     ▼
SentinelLog CLI
```

---

# Usage

Start SentinelLog:

```bash
sentinellog
```

The application will prompt:

```text
Log file path:
```

Enter the path to the access log you want to analyze.

### Windows Example

```text
F:\logs\access.log
```

### Linux Example

```text
/var/log/apache2/access.log
```

SentinelLog will then:

1. Validate the supplied file.
2. Parse supported log entries.
3. Count valid and invalid entries.
4. Build per-IP activity profiles.
5. Run the available detection modules.
6. Flag suspicious IP addresses.
7. Display supporting evidence in the terminal.

---

# Supported Log Format

SentinelLog currently targets structured web server access logs compatible with its parser.

A typical supported log entry contains information such as:

```text
IP Address
Identity / User Fields
Timestamp
HTTP Method
Requested Resource
HTTP Version
Status Code
Response Size
```

A simplified example:

```text
203.0.113.50 - - [timestamp] "POST /login HTTP/1.1" 401 512
```

Internally, SentinelLog converts raw log entries into structured request objects before sending them to the detection engine.

Conceptually:

```text
Raw Log Entry
      │
      ▼
Parser
      │
      ▼
Normalized Request Object
      │
      ▼
Detection Engine
```

This separation prevents individual detection modules from having to repeatedly clean or interpret raw log formatting.

Because access-log formats vary between Apache, Nginx, reverse proxies, frameworks, and custom applications, not every log format is currently guaranteed to be supported.

---

# Example Detection Scenario

Consider an IP producing activity similar to:

```text
POST /login        → repeated authentication failures
POST /login        → repeated authentication failures
GET /admin         → administrative resource probing
GET /phpmyadmin    → sensitive resource probing
GET /.env          → configuration discovery attempt
TRACE /            → unexpected HTTP method
```

SentinelLog correlates these events under the same IP profile.

The resulting detection may look like:

```text
IP Address: 203.0.113.50

Status:
FLAGGED

Detections:
- Brute Force
- Reconnaissance
- Method Abuse
```

Instead of manually examining large numbers of raw access-log entries, an analyst receives a summarized view of suspicious behavior along with supporting evidence.

---

# Detection Philosophy

SentinelLog is currently a **rule-based detection system**.

A detection should be interpreted as an indicator of suspicious behavior, not definitive proof that an IP address is malicious.

For example:

* Failed login attempts may come from a legitimate user who forgot a password.
* `404` responses may be generated by broken links or outdated bookmarks.
* Administrative paths may be accessed by legitimate administrators.
* `PUT`, `PATCH`, `DELETE`, and `OPTIONS` may be expected behavior for an API.

Detection accuracy therefore depends on:

* Appropriate thresholds
* Correct application configuration
* Understanding the environment being analyzed
* Correlation with additional security evidence

SentinelLog is intended to help identify activity that deserves further investigation.

---

# Current Limitations

SentinelLog is currently an early-stage project.

Current limitations include or may include:

* Limited supported access-log formats
* Rule-based detection
* No real-time monitoring
* No persistent database
* No SIEM integration
* No external threat-intelligence enrichment
* Limited correlation across multiple log sources
* Environment-specific thresholds may require tuning
* Performance optimization for very large log files is still limited

These limitations are expected to improve as the project develops.

---

# Roadmap

Potential future improvements include:

* Centralized configuration for thresholds and allowlists
* Improved risk scoring
* Time-window-based detection
* Burst/request-rate detection
* SQL injection indicators
* Path traversal detection
* Suspicious user-agent analysis
* Additional reconnaissance indicators
* Support for additional log formats
* CLI arguments and flags
* `--help` support
* `--version` support
* JSON report export
* CSV report export
* Improved analysis summaries
* Real-time or streaming log monitoring
* Automated unit and integration testing
* Performance improvements for large log files
* Additional detection modules

Roadmap items are planned or potential improvements and are not necessarily implemented in the current release.

---

# Testing the Installation

When testing packaging changes, it is recommended to install SentinelLog into a fresh virtual environment.

Create a clean environment:

```bash
python -m venv test-env
```

Activate it.

Then install SentinelLog from the repository:

```bash
python -m pip install .
```

Test the CLI command:

```bash
sentinellog
```

Also test the Python module directly:

```bash
python -m sentinel
```

For a stronger packaging test, change to a directory outside the repository and run:

```bash
sentinellog
```

If SentinelLog launches successfully outside the source directory, the package is less likely to be accidentally relying on imports or files available only from the repository working directory.

---

# Uninstallation

To remove SentinelLog from the currently active Python environment:

```bash
python -m pip uninstall sentinellog
```

This removes the installed Python distribution and generated CLI entry point.

It does **not** delete a separately cloned Git repository.

---

# Development Status

**Current Version:** `0.1.0`

SentinelLog is under active development.

Version `0.1.0` represents the initial working foundation of the project, including:

* Log parsing and validation
* Per-IP activity tracking
* Brute-force detection
* Reconnaissance detection
* HTTP method abuse detection
* CLI-based log file selection
* Rich terminal reporting
* Python package structure
* `sentinellog` CLI entry point

Detection logic, configuration, APIs, output formatting, and project structure may evolve in future releases.

---

# Contributing

Contributions, bug reports, testing, and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes.
4. Test the changes.
5. Commit with a descriptive commit message.
6. Push the branch to your fork.
7. Open a pull request.

When contributing detection logic, consider:

* False-positive behavior
* False-negative behavior
* Configurability
* Clear separation between parsing and detection
* Evidence collection
* Consistent detection naming
* Test cases for both legitimate and suspicious traffic

---

# Disclaimer

SentinelLog is intended for:

* Defensive cybersecurity
* Security log analysis
* Educational use
* Blue-team learning
* Authorized security research and experimentation

Detection results should be independently verified before taking security or administrative action.

Use SentinelLog only with systems, logs, and environments you own or are authorized to analyze.

---

# License

SentinelLog is licensed under the **MIT License**.

Copyright (c) 2026 **hellice121**

The MIT License permits use, copying, modification, merging, publishing, distribution, sublicensing, and selling copies of the software, subject to the conditions specified in the license.

See the `LICENSE` file in the repository for the complete license text.

---

# Author

Developed by **hellice121**

GitHub: `hellice121`

Repository:

```text
hellice121/Security-Log-Analyzer
```

SentinelLog is being developed as a practical cybersecurity project focused on understanding log analysis, detection engineering, attack-pattern identification, Python application architecture, and command-line security tooling.
