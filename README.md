# Secure Vehicle API: Zero Trust + Behavioral Detection Simulation

## Overview

This project is a multi-phase cybersecurity simulation demonstrating how weak identity validation, broken access control, and limited observability can create cyber-physical risk in connected vehicle systems.

The project progressively evolves from a deliberately vulnerable API into a Zero Trust-oriented architecture with SIEM/UEBA-style behavioral detection and risk scoring.

---

# Project Phases

## Phase 1 — Vulnerable Baseline
- Flask API with unrestricted access
- Endpoints:
  - /status
  - /unlock
  - /start
- Access controlled only by vehicle identifiers
- No authentication
- No authorization
- No rate limiting

### Security Weaknesses Demonstrated
- Broken access control
- Predictable identifiers
- Unauthenticated API access
- Lack of observability

---

## Phase 2 — Authentication + Rate Limiting
- Added API key authentication
- Added request rate limiting
- Added structured security logging
- Added security response headers

### Security Concepts
- Identity validation
- API hardening
- Abuse prevention
- Request attribution

---

## Phase 3 — Authorization + Least Privilege
- Added entitlement enforcement
- Mapped identities to authorized vehicles
- Blocked unauthorized cross-vehicle access
- Added authorization-aware logging

### Security Concepts
- Authentication vs authorization
- Least privilege
- Entitlement enforcement
- Zero Trust architecture

---

## Phase 4 — SIEM / UEBA-Style Detection
- Added live SIEM-style polling engine
- Added weighted risk scoring
- Added cumulative identity risk tracking
- Added alert classification
- Added behavioral anomaly detection
- Added live SIEM snapshots
- Added alert suppression cooldown logic

### Detection Concepts
- Behavioral analytics
- Identity-centric monitoring
- Security event correlation
- Risk aggregation
- SIEM/UEBA-style observability

---

# Visualization Layer

## visualizations.py
Original visualization implementation.

## visualizations_v2.py
Updated visualization implementation with PNG export support.

---

# Technologies Used

- Python
- Flask
- requests
- pandas
- matplotlib

---

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt