# 🚗 Secure Vehicle API: Zero Trust Security Operations Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-API-green)
![Security](https://img.shields.io/badge/Security-Zero%20Trust-red)
![SOC](https://img.shields.io/badge/SOC-Simulation-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Executive Summary

Secure Vehicle API: Zero Trust Security Operations Platform is a cybersecurity engineering project that demonstrates the evolution of a vulnerable vehicle control API into a Zero Trust–aligned Security Operations ecosystem.

The project progresses through twenty security phases covering:

- Authentication
- Authorization
- Detection Engineering
- Threat Hunting
- Incident Response
- Threat Intelligence
- SOAR Automation
- Machine Learning Detection
- Cloud Security
- Identity Federation
- Kubernetes Security
- EDR Simulation
- Purple Team Operations
- AI-Assisted SOC Analysis

The vehicle API serves as the attack surface while the Security Operations Center (SOC) components provide visibility, detection, investigation, response, and reporting capabilities.

This repository is intended as a cybersecurity engineering and SOC simulation platform for demonstrating modern defensive security concepts rather than a production vehicle control system.

---

## Architecture

```mermaid
flowchart TD

A[Vehicle API]

B[Authentication]
C[Authorization]

D[Detection Engineering]
E[Threat Intelligence]
F[Threat Hunting]

G[SOAR Automation]
H[Incident Response]

I[Executive Reporting]
J[SOC Dashboard]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I
I --> J
```

## Documentation

| Document                    | Description                         |
| --------------------------- | ----------------------------------- |
| Security Engineering Report | docs/SECURITY_ENGINEERING_REPORT.md |
| Zero Trust Maturity Matrix  | docs/ZERO_TRUST_MATURITY_MATRIX.md  |
| MITRE ATT&CK Mapping        | docs/MITRE_MAPPING.md               |
| Security Policy             | SECURITY.md                         |
| Project License             | LICENSE                             |

---

## Key Features

### Zero Trust Security Controls

- API Authentication
- Role-Based Authorization
- Least Privilege Enforcement
- Identity Federation
- Security Policy Validation

### Security Operations

- Detection Engineering
- Threat Hunting
- Incident Response
- SOAR Automation
- Executive Reporting

### Advanced Analytics

- Threat Intelligence Correlation
- Machine Learning Anomaly Detection
- Attack Path Analysis
- Attack Heatmap Generation
- Security Metrics Engine

### Modern Security Platforms

- Cloud Security Simulation
- Kubernetes Security Controls
- Endpoint Detection & Response Simulation
- Purple Team Operations
- AI SOC Analyst

---

## Phase Progression

| Phase | Capability |
|---------|---------|
| Phase 01 | Vulnerable Vehicle API |
| Phase 02 | Authentication |
| Phase 03 | Authorization |
| Phase 04 | SIEM Detection |
| Phase 05 | Detection Engineering |
| Phase 06 | Threat Hunting |
| Phase 07 | Incident Response |
| Phase 08 | Threat Intelligence |
| Phase 09 | SOAR Automation |
| Phase 10 | Detection Engine |
| Phase 11 | ML Anomaly Detection |
| Phase 12 | Cloud Security |
| Phase 13 | Attack Path Analysis |
| Phase 14 | Attack Heatmap |
| Phase 15 | Executive Reporting |
| Phase 16 | Identity Federation |
| Phase 17 | Kubernetes Security |
| Phase 18 | EDR Simulation |
| Phase 19 | Purple Team Operations |
| Phase 20 | AI SOC Analyst |

---

## Screenshots

# 📸 Security Analytics Intelligence Layer

> **Executive Summary:**  
This section visualizes SOC telemetry, detection engineering outputs, behavioral analytics, and machine learning–driven anomaly detection across the Secure Vehicle API environment.

---

## 🧭 SOC Command Dashboard

<p align="center">
  <img src="screenshots/phase10_soc_dashboard.png" width="850"/>
</p>

**Key Insights:**
- Unified SOC operational visibility  
- Real-time alert aggregation  
- Multi-layer security monitoring  

---

## 🔥 MITRE ATT&CK Coverage Heatmap

<p align="center">
  <img src="screenshots/phase14_attack_heatmap.png" width="850"/>
</p>

**Key Insights:**
- Maps detections to adversary techniques  
- Identifies coverage gaps  
- Enables purple team validation  

---

## 📊 API Behavioral Analytics

<p align="center">
  <img src="screenshots/requests_per_endpoint.png" width="850"/>
</p>

**Key Insights:**
- Detects abnormal endpoint usage  
- Establishes baseline traffic behavior  
- Identifies abuse patterns  

---

## 🚗 Identity-Based Access Distribution

<p align="center">
  <img src="screenshots/requests_per_vehicle.png" width="850"/>
</p>

**Key Insights:**
- Tracks identity-level access patterns  
- Supports least privilege validation  
- Detects anomalous identity concentration  

---

## ⚠️ Security Failure & Attack Signals

<p align="center">
  <img src="screenshots/security_failures.png" width="850"/>
</p>

**Key Insights:**
- Highlights authentication failures  
- Detects brute-force patterns  
- Supports incident investigation  

---

## 🤖 ML-Based Anomaly Detection Engine

<p align="center">
  <img src="screenshots/phase11_ml_detection.png" width="850"/>
</p>

**Key Insights:**
- Detects statistical outliers  
- Flags behavioral anomalies  
- Enhances SOC triage prioritization  

---

## Installation

```bash
git clone https://github.com/switice/secure-vehicle-api-zero-trust.git

cd secure-vehicle-api-zero-trust

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Running the Platform

### Detection Engine

```bash
python phase_10_detection_engine.py
```

### SOC Dashboard

```bash
python soc_dashboard.py
```

---

## Running Tests

```bash
pytest
```

Coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

---

## Technologies Used

- Python
- Flask
- Pandas
- Plotly
- Matplotlib
- Scikit-Learn
- REST APIs
- Docker
- GitHub Actions

---

## License

MIT License

---

## 🤝 Project Collaboration

| Contributor            | Focus Area                                                                            | LinkedIn                                           | GitHub                           |
| ---------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------- |
| Chukwuemeke Ikpeasonim | Cybersecurity Engineering, SOC Operations, Detection Engineering, Zero Trust Security | https://www.linkedin.com/in/chukwuemeke-ikpeasonim | https://github.com/switice       |
| Christina James        | Security Architecture, Identity & Access Management                                   | https://www.linkedin.com/in/christinanjames        | https://github.com/phoenyxcipher |

### Collaboration Acknowledgment

Secure Vehicle API: Zero Trust Security Operations Platform was collaboratively developed by Chukwuemeke Ikpeasonim and Christina James.

The project combines expertise in:

* Zero Trust Architecture
* Identity & Access Management
* Detection Engineering
* Threat Hunting
* Incident Response
* Security Operations
* Security Architecture

The platform demonstrates the evolution of a vulnerable API into a layered security ecosystem featuring authentication, authorization, detection engineering, threat intelligence, SOAR automation, identity federation, cloud security, Kubernetes security, EDR simulation, purple team operations, and AI-assisted SOC analysis.
