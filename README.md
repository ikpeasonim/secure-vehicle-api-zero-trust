# 🚗 Secure Vehicle API: Zero Trust SOC Simulation Platform

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SOC Simulation](https://img.shields.io/badge/SOC-Simulation-red)
![Zero Trust](https://img.shields.io/badge/Zero%20Trust-Architecture-green)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-darkred)
![Machine Learning](https://img.shields.io/badge/ML-Anomaly%20Detection-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Tests](https://github.com/switice/secure-vehicle-api-zero-trust/actions/workflows/python-tests.yml/badge.svg)

> **Project Status:** ✅ Portfolio Ready | Zero Trust Security Platform | SOC Engineering Demonstration | Version 1.0.0

---

A cybersecurity engineering portfolio project demonstrating the evolution of a vulnerable API into a Zero Trust, SOC-driven security ecosystem through authentication, authorization, detection engineering, SIEM analytics, threat intelligence correlation, SOAR automation, cloud security monitoring, and AI-assisted security operations.

---
# 🚀 Overview

Secure Vehicle API is a multi-phase cybersecurity simulation platform that demonstrates how a vulnerable API environment evolves into a mature Security Operations Center (SOC) ecosystem using Zero Trust security principles.

This project models real-world cybersecurity engineering workflows including:

* API security hardening
* Authentication and authorization
* SIEM detection engineering
* UEBA behavioral analytics
* Threat hunting
* SOAR automation
* Threat intelligence correlation
* Machine learning anomaly detection
* Cloud security monitoring
* Identity attack path analysis
* MITRE ATT&CK heatmapping
* Executive security reporting
* Identity federation and SSO
* Kubernetes security monitoring
* Endpoint Detection & Response (EDR)
* Purple team automation
* AI-assisted SOC workflows

---

# ⭐ Portfolio Highlights

- 20-phase cybersecurity engineering progression
- Zero Trust API security model
- Authentication and authorization controls
- SIEM and UEBA analytics
- Detection engineering aligned to MITRE ATT&CK
- Threat hunting workflows
- Incident response automation
- Threat intelligence correlation
- SOAR playbook simulation
- Machine learning anomaly detection
- Cloud security monitoring
- Kubernetes security analysis
- EDR telemetry simulation
- Purple team validation
- AI-assisted SOC analyst workflows
- GitHub Actions CI/CD pipeline
- Docker containerization

---

# 🧭 System Design Philosophy

This project simulates how modern Security Operations Centers evolve from vulnerable infrastructure into layered security ecosystems.

The architecture progressively introduces:

* Telemetry ingestion
* Detection engineering
* Threat intelligence correlation
* SOAR automation
* Behavioral analytics
* Machine learning detection
* Identity security
* Cloud security monitoring
* Endpoint monitoring
* Purple team validation
* AI-assisted analyst workflows

---

# 🏗️ Architecture Overview

```mermaid
flowchart TD

    U[Users] --> API[Secure Vehicle API]

    API --> AUTH[Authentication Layer]
    API --> AUTHZ[Authorization Layer]

    AUTH --> SOC
    AUTHZ --> SOC

    subgraph SOC[Security Operations Layer]
        SIEM[SIEM Detection]
        DET[Detection Engineering]
        TH[Threat Hunting]
        IR[Incident Response]
        TI[Threat Intelligence]
        SOAR[SOAR Automation]
        ML[ML Anomaly Detection]
        AI[AI SOC Analyst]
    end

    SOC --> MON

    subgraph MON[Monitoring & Reporting]
        DASH[SOC Dashboard]
        HEAT[MITRE ATT&CK Heatmap]
        EXEC[Executive Reporting]
        METRICS[Security Metrics]
    end

    MON --> INFRA

    subgraph INFRA[Infrastructure Security]
        CLOUD[Cloud Security]
        FED[Identity Federation]
        K8S[Kubernetes Security]
        EDR[EDR Simulation]
    end
```

This architecture demonstrates the progression from a vulnerable API to a mature Zero Trust security operations platform incorporating detection engineering, threat intelligence correlation, SOAR automation, machine learning analytics, and infrastructure security controls.

---


# 🔄 End-to-End SOC Pipeline

```text
Vehicle API
    ↓
Authentication
    ↓
Authorization
    ↓
Security Logging
    ↓
SIEM Analytics
    ↓
Detection Engineering
    ↓
Threat Hunting
    ↓
SOAR Automation
    ↓
Threat Intelligence Correlation
    ↓
Machine Learning Anomaly Detection
    ↓
Executive Security Reporting
```

---

## Architecture

```mermaid
flowchart LR

User[Authorized User]

API[Vehicle API]

AUTH[Authentication Layer]

AUTHZ[Authorization Layer]

SIEM[SIEM Detection]

DET[Detection Engine]

SOC[SOC Command Center]

IR[Incident Response]

SOAR[SOAR Automation]

AI[AI SOC Analyst]

VEH[Vehicle Systems]

User --> API

API --> AUTH

AUTH --> AUTHZ

AUTHZ --> VEH

AUTH --> SIEM

AUTHZ --> SIEM

SIEM --> DET

DET --> SOC

SOC --> IR

IR --> SOAR

SOAR --> AI
```
---

# 🎯 Project Objectives

This repository demonstrates practical cybersecurity engineering concepts across multiple domains:

* Zero Trust Architecture
* Detection Engineering
* SIEM Analytics
* UEBA Behavioral Analytics
* Threat Hunting
* SOAR Automation
* Threat Intelligence Correlation
* Cloud Security Monitoring
* Identity Security
* Endpoint Detection & Response
* Kubernetes Security
* Purple Team Operations
* AI-Assisted SOC Operations

---

# 💼 Cybersecurity Skills Demonstrated

* Security Operations Center (SOC)
* SIEM Engineering
* UEBA Analytics
* Detection Engineering
* Threat Hunting
* Threat Intelligence Correlation
* Incident Response
* SOAR Automation
* MITRE ATT&CK Mapping
* Cloud Security Monitoring
* Identity Security
* Kubernetes Security
* Endpoint Detection & Response (EDR)
* Machine Learning Security Analytics
* Security Visualization & Reporting
* AI-Assisted Security Operations
  
---

# 🛡️ Project Phases

---

## Phase 01 — Vulnerable Baseline

### Implementation

* Flask API with unrestricted access
* Public vehicle control endpoints
* No authentication
* No authorization
* No rate limiting

### Security Concepts

* Broken access control
* API exposure risks
* Attack surface analysis
* Identity absence risks

---

## Phase 02 — Authentication + Rate Limiting

### Implementation

* API key authentication
* Request rate limiting
* Structured security logging
* Security header enforcement

### Security Concepts

* Authentication workflows
* API hardening
* Abuse prevention
* Request attribution

---

## Phase 03 — Authorization + Least Privilege

### Implementation

* Identity-to-vehicle mapping
* Access policy enforcement
* Cross-vehicle access prevention
* Authorization-aware telemetry

### Security Concepts

* Authorization models
* Least privilege
* Zero Trust enforcement
* Identity segmentation

---

## Phase 04 — SIEM / UEBA Detection

### Implementation

* SIEM-style telemetry aggregation
* UEBA behavioral analytics
* Identity risk scoring
* Alert classification engine

### Security Concepts

* SIEM analytics
* UEBA monitoring
* Behavioral baselining
* Event correlation

---

## Phase 05 — Detection Engineering + MITRE ATT&CK

### Implementation

* ATT&CK technique mapping
* Detection rule logic
* Event correlation workflows
* Severity-based detections

### Security Concepts

* Detection engineering
* MITRE ATT&CK alignment
* Threat modeling
* Detection lifecycle management

---

## Phase 06 — Threat Hunting

### Implementation

* IOC investigation workflows
* Historical telemetry analysis
* Behavioral anomaly discovery
* Threat pattern analysis

### Security Concepts

* Threat hunting methodologies
* IOC-based investigations
* Behavioral analytics
* Adversary tracking

---

## Phase 07 — SOC Incident Response Automation

### Implementation

* Automated alert triage
* Incident severity scoring
* Response recommendation engine
* Workflow automation

### Security Concepts

* Incident response lifecycle
* SOC orchestration
* Alert prioritization
* Security operations automation

---

## Phase 08 — Threat Intelligence Correlation

### Implementation

* IOC matching engine
* Threat feed enrichment
* Reputation analysis
* Intelligence-driven detections

### Security Concepts

* Threat intelligence pipelines
* IOC enrichment
* Adversary infrastructure analysis
* Intelligence correlation

---

## Phase 09 — SOAR Automation

### Implementation

* Automated containment logic
* Identity quarantine simulation
* API key disablement
* Response playbook execution

### Security Concepts

* SOAR workflows
* Automated remediation
* Containment strategies
* Security orchestration

---

## Phase 10 — SOC Dashboarding

### Implementation

* SOC analytics dashboards
* Event trend visualization
* Alert aggregation views
* Monitoring interfaces

### Security Concepts

* Security visualization
* Telemetry analytics
* Operational monitoring
* SOC observability

---

## Phase 11 — Machine Learning Anomaly Detection

### Implementation

* Isolation Forest anomaly detection
* Behavioral outlier scoring
* Risk confidence analysis
* Statistical anomaly modeling

### Security Concepts

* Machine learning security analytics
* Behavioral anomaly detection
* Statistical deviation analysis
* ML-driven detection workflows

---

## Phase 12 — Cloud Security Simulation

### Implementation

* IAM abuse simulation
* Cloud audit event logging
* Privilege escalation scenarios
* Cloud monitoring telemetry

### Security Concepts

* Cloud security posture
* IAM monitoring
* Identity-based cloud attacks
* Cloud threat detection

---

## Phase 13 — Identity Attack Path Analysis

### Implementation

* Identity attack graph simulation
* Privilege escalation path analysis
* Lateral movement mapping
* Trust relationship modeling

### Security Concepts

* Identity attack paths
* Lateral movement analysis
* Trust exploitation
* Identity-centric defense

---

## Phase 14 — MITRE ATT&CK Heatmap Visualization

### Implementation

* ATT&CK coverage heatmaps
* Technique scoring
* Detection visualization
* Threat coverage analysis

### Security Concepts

* ATT&CK coverage analysis
* Detection visibility
* Threat modeling visualization
* Security maturity assessment

---

## Phase 15 — Executive Security Reporting

### Implementation

* SOC KPI reporting
* Incident trend summaries
* Executive dashboards
* Security posture reporting

### Security Concepts

* Executive reporting
* Risk communication
* SOC metrics
* Strategic security analytics

---

# 🚀 Advanced Expansion Phases

---

## Phase 16 — Identity Federation + SSO

### Implementation

* JWT token federation
* OAuth-style identity workflows
* MFA simulation
* Session validation
* Token expiration analysis
* Session hijacking detection

### Security Concepts

* Identity federation
* SSO trust boundaries
* Session security
* Token abuse detection
* Identity attack prevention

---

## Phase 17 — Kubernetes Security

### Implementation

* Kubernetes audit logging
* RBAC misconfiguration detection
* Container runtime monitoring
* Service account abuse detection
* Cluster event telemetry

### Security Concepts

* Container security
* Kubernetes RBAC
* Runtime security monitoring
* Cloud-native security
* Cluster attack analysis

---

## Phase 18 — EDR Simulation

### Implementation

* Endpoint telemetry generation
* Process execution monitoring
* Registry persistence detection
* Simulated malware execution
* Host alert scoring

### Security Concepts

* Endpoint Detection & Response
* Behavioral monitoring
* Persistence analysis
* Threat telemetry correlation
* Host-based detections

---

## Phase 19 — Purple Team Automation

### Implementation

* ATT&CK adversary emulation
* Detection validation workflows
* Automated technique replay
* Detection coverage scoring
* ATT&CK testing automation

### Security Concepts

* Purple teaming
* Adversary emulation
* Detection validation
* SOC readiness testing
* ATT&CK-based assessments

---

## Phase 20 — AI-Assisted SOC Analyst

### Implementation

* AI alert summarization
* Automated triage recommendations
* Threat prioritization engine
* Investigation assistance workflows
* AI-assisted incident analysis

### Security Concepts

* AI-assisted SOC operations
* LLM-powered security workflows
* Security automation
* Analyst augmentation
* AI-driven investigation support

---

# 🔥 Sample Detection Scenarios

This platform includes simulations for modern SOC detection workflows such as:

* Unauthorized vehicle unlock attempts
* API abuse and brute-force detection
* Identity-based anomaly detection
* Impossible travel scenarios
* Suspicious JWT token reuse
* Session hijacking behavior
* Kubernetes RBAC escalation attempts
* Service account abuse
* PowerShell persistence activity
* Malware execution telemetry
* Threat intelligence IOC correlation
* AI-prioritized incident scoring

---

# 🧠 Real-World Technology Alignment

| Security Domain     | Real-World Technology Alignment              |
| ------------------- | -------------------------------------------- |
| SIEM Analytics      | Splunk, Microsoft Sentinel                   |
| Identity Federation | Okta, Microsoft Entra ID, Ping Identity      |
| SOAR Automation     | Cortex XSOAR, Splunk SOAR                    |
| Endpoint Security   | CrowdStrike, SentinelOne, Microsoft Defender |
| Kubernetes Security | Falco, Prisma Cloud                          |
| Threat Intelligence | MISP, Recorded Future                        |
| Cloud Security      | AWS GuardDuty, Azure Defender                |
| UEBA Analytics      | Exabeam, Securonix                           |

---

# 📸 Screenshots

## SOC Dashboard

![SOC Dashboard](screenshots/phase10_soc_dashboard.png)

---

## ATT&CK Heatmap

![ATTACK Heatmap](screenshots/phase14_attack_heatmap.png)

---

# 🧰 Technologies Used

* Python
* Flask
* pandas
* matplotlib
* scikit-learn
* requests
* JSON
* REST APIs

---

# 🔍 Security Domains Demonstrated

* Zero Trust Architecture
* SIEM Monitoring
* UEBA Analytics
* Detection Engineering
* MITRE ATT&CK Mapping
* Threat Hunting
* Incident Response
* SOAR Automation
* Threat Intelligence
* Cloud Security
* Identity Security
* Machine Learning Security Analytics
* Kubernetes Security
* Endpoint Detection & Response
* Purple Team Operations
* AI-Assisted SOC Workflows

---

# 📂 Repository Structure

```text
.
├── .github/
│   └── workflows/
├── auth/
├── data/
├── docs/
├── outputs/
├── reports/
├── static/
├── templates/
├── tests/
│   └── data/
├── app.py
├── soc_dashboard.py
├── soc_pipeline.py
├── soc_command_center.py
├── event_bus.py
├── analyze_logs.py
├── Dockerfile
├── SECURITY.md
├── README.md
└── phase_01 ... phase_20
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/switice/secure-vehicle-api-zero-trust.git
cd secure-vehicle-api-zero-trust
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Project Phases

## Example

```bash
python phase_10_soc_dashboard.py
```

---

## Additional Examples

```bash
python phase_10_soc_dashboard.py
python phase_11_ml_anomaly_detection.py
python phase_12_cloud_security.py
python phase_14_attack_heatmap.py
python phase_15_executive_reporting.py
python phase_16_identity_federation.py
python phase_17_kubernetes_security.py
python phase_18_edr_simulation.py
```

---

# 🚀 CI/CD Pipeline

This repository includes GitHub Actions workflow automation for:

* Dependency installation
* Python linting
* Automated testing
* CI validation workflows

Workflow file:

```text
.github/workflows/python-app.yml
```

---

# 🧪 Testing

Run the test suite:

```bash
pytest
```

Run coverage analysis:

```bash
pytest --cov=. --cov-report=term-missing
```

The repository includes unit and integration tests validating API security controls, SOC workflows, detection logic, and supporting analytics components.

---

# 📊 Project Impact

This platform demonstrates practical SOC engineering capability across multiple cybersecurity domains, including:

* Detection engineering
* Threat intelligence correlation
* UEBA analytics
* SOAR automation
* Identity security
* Cloud monitoring
* Machine learning security analytics
* Executive security reporting
* Kubernetes security monitoring
* EDR simulation
* Purple team operations
* AI-assisted SOC workflows

The project simulates how modern Security Operations Centers evolve from vulnerable infrastructure into layered, intelligence-driven security ecosystems.

---

# 🎥 Future Enhancements

* Interactive SOC web dashboard
* Real-time streaming telemetry
* ATT&CK coverage analytics dashboard
* Threat intelligence API integrations
* Security data lake architecture
* Multi-tenant SOC simulation
* Advanced AI investigation assistant
* Automated attack replay framework

---

# 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

# 🤝 Project Collaboration

## Chukwuemeke Ikpeasonim

Cybersecurity Engineer | SOC Operations | Detection Engineering | Zero Trust Security

LinkedIn: https://www.linkedin.com/in/chukwuemeke-ikpeasonim

GitHub: https://github.com/switice

---

## Christina James

Cybersecurity Professional | Security Architecture | Identity & Access Management

LinkedIn: https://www.linkedin.com/in/christinanjames

GitHub: https://github.com/phoenyxcipher

---

## Collaboration Acknowledgment

Secure Vehicle API is a collaborative cybersecurity engineering project designed and developed by Chukwuemeke Ikpeasonim and Christina James.

The project combines expertise in security operations, security architecture, identity and access management, detection engineering, and Zero Trust security principles to simulate the evolution of a vulnerable API environment into a modern SOC-driven security ecosystem.

Key areas of collaboration included:

* Security architecture and platform design
* Zero Trust strategy and implementation concepts
* Identity-centric security controls and access governance
* Authentication and authorization model development
* Detection engineering and threat detection methodologies
* Security design reviews and technical validation
* SOC workflows, monitoring, and incident response concepts
* Project planning, direction, and continuous improvement

The resulting platform demonstrates the progression of a vulnerable API environment into a layered security architecture incorporating authentication, authorization, telemetry generation, SIEM analytics, UEBA monitoring, threat hunting workflows, SOAR automation, threat intelligence correlation, cloud security monitoring, identity security concepts, endpoint telemetry simulation, Kubernetes security monitoring, and AI-assisted SOC capabilities.

The project serves as a practical cybersecurity engineering portfolio that showcases the evolution of security controls, detection capabilities, and operational workflows across a modern Zero Trust security model while emphasizing real-world cybersecurity engineering practices.

This collaboration reflects a shared commitment to advancing cybersecurity education, defensive security engineering, modern security operations, and the practical application of Zero Trust principles in simulated enterprise environments.


---

# ⭐ Security Engineering Outcomes

This project demonstrates the ability to:

* Design and secure API-driven systems
* Build detection engineering workflows
* Develop SIEM and UEBA analytics pipelines
* Automate SOC response actions using SOAR principles
* Correlate threat intelligence with behavioral telemetry
* Simulate cloud and identity-based attack scenarios
* Visualize security metrics and executive KPIs
* Apply MITRE ATT&CK techniques for detection coverage analysis
* Explore AI-assisted SOC workflows
* Build end-to-end cybersecurity monitoring solutions
---
