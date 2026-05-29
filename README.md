# Secure Vehicle API: Zero Trust + SOC Simulation Platform

![Python](https://img.shields.io/badge/Python-3.10-blue)
![SOC Simulation](https://img.shields.io/badge/SOC-Simulation-red)
![Zero Trust](https://img.shields.io/badge/Zero%20Trust-Architecture-green)

## Overview

This project is a multi-phase cybersecurity simulation that demonstrates how a vulnerable system evolves into a full Security Operations Center (SOC) pipeline.

It models real-world security engineering domains including:
- SIEM-based detection engineering
- UEBA behavioral analytics
- Threat intelligence correlation
- SOAR automation and response
- Machine learning anomaly detection
- Cloud security monitoring
- Identity attack path analysis
- Executive security reporting

---

## Project Type

✔ SOC Simulation Platform  
✔ Detection Engineering Lab  
✔ Threat Intelligence Pipeline  
✔ SOAR Automation System  
✔ Security Analytics Engine  

---

## TL;DR Architecture

This system simulates a full SOC pipeline:

- API Layer → Vehicle telemetry ingestion
- Detection Layer → SIEM + UEBA analytics
- Intelligence Layer → Threat feeds + IOC correlation
- Response Layer → SOAR automation + containment
- Analytics Layer → Dashboards + ML anomaly detection
- Reporting Layer → Executive security metrics

---

## Architecture Overview

![SOC Architecture](architecture_diagram.png)

---

# Project Phases

---

## Phase 1 — Vulnerable Baseline

### Implementation
- Flask API with unrestricted access
- Endpoints:
  - `/status`
  - `/unlock`
  - `/start`
- No authentication
- No authorization
- No rate limiting

### Security Weaknesses
- Broken access control
- Predictable identifiers
- Unauthenticated API access
- Lack of observability

### Security Concepts
- Attack surface exposure
- Identity absence risk
- API security fundamentals
- Access control failure patterns

---

## Phase 2 — Authentication + Rate Limiting

### Implementation
- API key authentication
- Rate limiting protection
- Structured logging
- Security headers

### Security Concepts
- Identity verification
- API hardening techniques
- Abuse prevention mechanisms
- Request attribution tracking
- Basic defensive controls

---

## Phase 3 — Authorization + Least Privilege

### Implementation
- Identity-to-vehicle mapping
- Access control enforcement
- Cross-vehicle access blocking
- Authorization-aware logging

### Security Concepts
- Authentication vs Authorization
- Least privilege principle
- Zero Trust architecture foundation
- Entitlement enforcement
- Access control policy design

---

## Phase 4 — SIEM / UEBA Detection

### Implementation
- Live SIEM-style event engine
- Behavioral anomaly detection
- Risk scoring per identity
- Alert classification system
- Identity-based monitoring

### Security Concepts
- SIEM (Security Information and Event Management)
- UEBA (User & Entity Behavior Analytics)
- Behavioral baselining
- Security event correlation
- Risk aggregation modeling
- Real-time detection logic

---

## Phase 5 — Detection Engineering + MITRE ATT&CK

### Implementation
- MITRE ATT&CK mapping
- Detection rule creation
- Event correlation logic
- Severity-based alerting

### Security Concepts
- MITRE ATT&CK framework usage
- Detection engineering lifecycle
- Threat classification models
- Security rule tuning
- Attack technique mapping

---

## Phase 6 — Threat Hunting

### Implementation
- IOC discovery workflows
- Behavioral anomaly investigation
- Historical event analysis
- Suspicious pattern detection

### Security Concepts
- Proactive threat hunting
- Hypothesis-driven investigation
- IOC-based detection
- Behavioral analytics
- Adversary tracking techniques

---

## Phase 7 — SOC Incident Response Automation

### Implementation
- Automated alert triage
- Incident classification engine
- Response recommendations
- Severity scoring system

### Security Concepts
- SOC workflows
- Incident lifecycle management
- Alert triage processes
- Response orchestration
- Security operations automation

---

## Phase 8 — Threat Intelligence Correlation

### Implementation
- IOC matching engine
- Threat feed enrichment
- IP reputation analysis
- Behavioral-to-threat mapping

### Security Concepts
- Threat intelligence integration
- IOC correlation techniques
- Adversary infrastructure analysis
- Enrichment pipelines
- Intelligence-driven detection

---

## Phase 9 — SOAR Automation

### Implementation
- Automated containment engine
- Identity quarantine simulation
- API key disablement
- Response playbooks

### Security Concepts
- SOAR (Security Orchestration Automation Response)
- Automated remediation
- Incident containment strategies
- Playbook execution
- Security automation workflows

---

## Phase 10 — SOC Dashboarding

### Implementation
- Security dashboards
- Event aggregation views
- SOC monitoring interface
- Trend visualization

### Security Concepts
- SOC visualization design
- Security telemetry analysis
- Operational monitoring
- Alert trend analysis
- Security observability

---

## Phase 11 — Machine Learning Anomaly Detection

### Implementation
- Isolation Forest detection model
- Behavioral anomaly scoring
- Outlier classification
- Confidence scoring

### Security Concepts
- Unsupervised anomaly detection
- Behavioral baselining
- Statistical deviation analysis
- ML-driven security analytics
- Adversarial behavior detection

---

## Phase 12 — Cloud Security Simulation

### Implementation
- IAM abuse simulation
- Cloud audit logs
- Privilege escalation scenarios
- Cloud monitoring events

### Security Concepts
- Cloud security posture
- IAM risk analysis
- Cloud audit logging
- Identity-based cloud attacks
- Cloud threat detection

---

## Phase 13 — Identity Attack Path Analysis

### Implementation
- Attack chain modeling
- Identity relationship mapping
- Lateral movement simulation
- Privilege escalation paths

### Security Concepts
- Identity attack graph modeling
- Lateral movement analysis
- Trust relationship exploitation
- Attack path discovery
- Identity-centric security

---

## Phase 14 — ATT&CK Heatmap Visualization

### Implementation
- MITRE ATT&CK coverage heatmap
- Technique scoring system
- Detection coverage visualization

### Security Concepts
- ATT&CK framework mapping
- Detection coverage analysis
- Threat modeling visualization
- Security maturity assessment

---

## Phase 15 — Executive Reporting

### Implementation
- SOC KPI dashboards
- Incident trend analysis
- Security posture summaries
- Executive reporting layer

### Security Concepts
- Security metrics reporting
- Executive-level SOC visibility
- Risk communication
- Operational security KPIs
- Strategic security analytics

---

# Screenshots

## Security Visualization Layer

All SOC analytics dashboards and security visualizations are available in `/screenshots`:

- SIEM dashboards
- Threat detection charts
- SOC heatmaps
- ML anomaly graphs
- Incident response flows
- Threat intelligence views
- Executive security reports

---

# Visualization Layer

## visualizations.py
Original visualization engine

## visualizations_v2.py
Enhanced version with PNG export support

---

# Technologies Used

- Python
- Flask
- pandas
- matplotlib
- requests

---

# Security Concepts Demonstrated

- Zero Trust Architecture
- SIEM Monitoring
- UEBA Behavioral Analytics
- Detection Engineering
- MITRE ATT&CK Mapping
- Threat Hunting
- Incident Response Automation
- Threat Intelligence Correlation
- SOAR Automation
- Machine Learning Security Analytics
- Cloud Security Simulation
- Identity Attack Path Analysis
- Executive SOC Reporting

---

# Repository Structure

```text
phase1_vulnerable_api.py
phase2_authenticated_api.py
phase3_authorization_api.py
phase4_siem_detection.py
phase5_detection_engineering.py
phase6_threat_hunting.py
phase7_incident_response.py
phase8_threat_intelligence_correlations.py
phase9_soar_automation.py
phase10_soc_dashboard.py
phase11_ml_anomaly_detection.py
phase12_cloud_security.py
phase13_attack_path_analysis.py
phase14_attack_heatmap.py
phase15_executive_reporting.py
```

---

## Visualization Layer

- visualizations.py — Original visualization engine
- visualizations_v2.py — Enhanced version with PNG export support

---

## Logs

analyze_logs.py

---

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Individual Phases

### Phase 1

```bash
python phase1_vulnerable_api.py
```

### Phase 2

```bash
python phase2_authenticated_api.py
```

### Phase 3

```bash
python phase3_authorization_api.py
```

### Phase 4

```bash
python phase4_siem_detection.py
```

### Phase 5

```bash
python phase5_detection_engineering.py
```

### Phase 6

```bash
python phase6_threat_hunting.py
```

### Phase 7

```bash
python phase7_incident_response.py
```

### Phase 8

```bash
python phase8_threat_intelligence_correlations.py
```

---

# Project Impact

This project demonstrates end-to-end SOC engineering capability, including:

- Detection engineering pipeline design
- Threat intelligence integration workflows
- Behavioral analytics (UEBA-style detection)
- SOAR automation and incident response logic
- Cloud and identity security modeling
- Executive SOC reporting and KPI tracking

It simulates how modern Security Operations Centers evolve from raw telemetry ingestion to automated threat detection and response systems.

--- 

# About

Zero Trust Vehicle API Security Project with Authentication, Authorization, SIEM Monitoring, Detection Engineering, Threat Hunting, Incident Response Automation, and Threat Intelligence Correlation.
