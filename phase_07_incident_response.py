import requests
import json
from collections import defaultdict, Counter
from datetime import datetime
import time

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

# -----------------------------
# RISK THRESHOLDS
# -----------------------------
MEDIUM_THRESHOLD = 50
HIGH_THRESHOLD = 100
CRITICAL_THRESHOLD = 150

# -----------------------------
# MITRE ATT&CK MAPPING
# -----------------------------
MITRE_MAPPING = {

    "invalid_api_key": {
        "technique": "T1078",
        "attack": "Valid Accounts",
        "risk": 40
    },

    "missing_api_key": {
        "technique": "T1190",
        "attack": "Exploit Public-Facing Application",
        "risk": 25
    },

    "unauthorized_vehicle_access": {
        "technique": "T1210",
        "attack": "Exploitation of Remote Services",
        "risk": 50
    }
}

# -----------------------------
# FETCH LOGS
# -----------------------------
def fetch_logs():

    try:

        response = requests.get(
            f"{BASE_URL}/logs",
            headers=HEADERS,
            timeout=5
        )

        print(f"[INFO] STATUS CODE: {response.status_code}")

        if response.status_code != 200:
            print("[ERROR] Failed to fetch logs")
            return []

        data = response.json()

        # Wrapped structure
        if isinstance(data, dict) and "logs" in data:
            logs = data["logs"]

        elif isinstance(data, list):
            logs = data

        else:
            print("[ERROR] Unexpected log format")
            return []

        print(f"[INFO] LOG COUNT: {len(logs)}")

        return logs

    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
        return []

# -----------------------------
# CLASSIFY SEVERITY
# -----------------------------
def classify_severity(score):

    if score >= CRITICAL_THRESHOLD:
        return "CRITICAL"

    elif score >= HIGH_THRESHOLD:
        return "HIGH"

    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"

    else:
        return "LOW"

# -----------------------------
# INCIDENT RESPONSE ENGINE
# -----------------------------
def incident_response(logs):

    identity_risk = Counter()
    identity_events = defaultdict(list)
    blocked_identities = set()

    # -----------------------------
    # PROCESS LOGS
    # -----------------------------
    for log in logs:

        identity = log.get("role", "unknown")
        reason = log.get("reason")
        vehicle = log.get("vehicle_id")
        timestamp = log.get("timestamp")

        identity_events[identity].append(log)

        # -----------------------------
        # APPLY RISK SCORING
        # -----------------------------
        if reason in MITRE_MAPPING:

            risk = MITRE_MAPPING[reason]["risk"]

            identity_risk[identity] += risk

            technique = MITRE_MAPPING[reason]["technique"]

            attack = MITRE_MAPPING[reason]["attack"]

            print("\n==============================")
            print("[SECURITY EVENT]")
            print("==============================")

            print(f"Time: {timestamp}")
            print(f"Identity: {identity}")
            print(f"Vehicle: {vehicle}")
            print(f"Reason: {reason}")
            print(f"MITRE Technique: {technique}")
            print(f"Attack Name: {attack}")
            print(f"Risk Added: {risk}")
            print(
                f"Cumulative Risk: "
                f"{identity_risk[identity]}"
            )

    # -----------------------------
    # INCIDENT REVIEW
    # -----------------------------
    print("\n==============================")
    print("SOC INCIDENT REVIEW")
    print("==============================")

    for identity, score in identity_risk.items():

        severity = classify_severity(score)

        print(f"\nIdentity: {identity}")
        print(f"Risk Score: {score}")
        print(f"Severity: {severity}")

        # -----------------------------
        # AUTO-CONTAINMENT
        # -----------------------------
        if severity == "CRITICAL":

            blocked_identities.add(identity)

            print("\n[CONTAINMENT ACTION]")
            print(
                f"Identity '{identity}' "
                f"temporarily blocked"
            )

            print(
                "Recommended Action: "
                "Disable API key immediately"
            )

        elif severity == "HIGH":

            print("\n[ESCALATION]")
            print(
                f"Identity '{identity}' "
                f"requires analyst review"
            )

        elif severity == "MEDIUM":

            print("\n[MONITORING]")
            print(
                f"Identity '{identity}' "
                f"flagged for observation"
            )

    # -----------------------------
    # EXPORT INCIDENT REPORT
    # -----------------------------
    report = {
        "generated_at": datetime.utcnow().isoformat(),
        "blocked_identities": list(blocked_identities),
        "incidents": []
    }

    for identity, score in identity_risk.items():

        severity = classify_severity(score)

        incident = {
            "identity": identity,
            "risk_score": score,
            "severity": severity,
            "event_count": len(identity_events[identity]),
            "events": identity_events[identity]
        }

        report["incidents"].append(incident)

    filename = (
        f"soc_incident_report_"
        f"{datetime.now().strftime('%H%M%S')}.json"
    )

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print("\n==============================")
    print("INCIDENT REPORT GENERATED")
    print("==============================")

    print(f"[SAVED] {filename}")

# -----------------------------
# HEARTBEAT MONITOR
# -----------------------------
def heartbeat():

    while True:

        current_time = datetime.now().strftime("%H:%M:%S")

        print(
            f"\n[HEARTBEAT] "
            f"{current_time} | "
            f"SOC monitoring active..."
        )

        logs = fetch_logs()

        if logs:
            incident_response(logs)

        else:
            print("[INFO] No logs available")

        time.sleep(15)

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    print("\n==============================")
    print("PHASE 7 INCIDENT RESPONSE")
    print("==============================")

    heartbeat()

# phase_07_incident_response.py
def main():
    print("Phase 07: Incident Response")
    from time import sleep
    sleep(0.1)
    print("Phase 07 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")