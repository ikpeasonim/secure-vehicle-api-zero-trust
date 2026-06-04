import requests
import json
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

# ---------------------------------
# THREAT INTELLIGENCE FEED
# ---------------------------------
KNOWN_BAD_IDENTITIES = {
    "developer": {
        "threat_actor": "Simulated Insider Threat",
        "severity": "HIGH",
        "mitre": "T1078",
        "description": "Valid account abuse detected"
    },

    "unknown": {
        "threat_actor": "Anonymous Threat Actor",
        "severity": "CRITICAL",
        "mitre": "T1190",
        "description": "Public-facing application abuse"
    }
}

# ---------------------------------
# FETCH LOGS
# ---------------------------------
def fetch_logs():

    try:

        response = requests.get(
            f"{BASE_URL}/logs",
            headers={"X-API-KEY": "dev-key-123"},
            timeout=5
        )

        if response.status_code != 200:
            print("[ERROR] Failed to retrieve logs")
            return []

        data = response.json()

        if isinstance(data, dict) and "logs" in data:
            return data["logs"]

        elif isinstance(data, list):
            return data

        return []

    except Exception as e:
        print(f"[ERROR] {e}")
        return []

# ---------------------------------
# IOC CORRELATION ENGINE
# ---------------------------------
def correlate_iocs(logs):

    findings = []

    for log in logs:

        identity = log.get("role", "unknown")
        vehicle = log.get("vehicle_id", "unknown")
        reason = log.get("reason")
        timestamp = log.get("timestamp")

        if identity in KNOWN_BAD_IDENTITIES:

            intel = KNOWN_BAD_IDENTITIES[identity]

            finding = {
                "timestamp": timestamp,
                "identity": identity,
                "vehicle": vehicle,
                "severity": intel["severity"],
                "threat_actor": intel["threat_actor"],
                "mitre_technique": intel["mitre"],
                "description": intel["description"],
                "event_reason": reason
            }

            findings.append(finding)

    return findings

# ---------------------------------
# GENERATE REPORT
# ---------------------------------
def generate_report(findings):

    if not findings:
        print("[INFO] No IOC correlations detected")
        return

    print("\n==============================")
    print("THREAT INTELLIGENCE REPORT")
    print("==============================\n")

    for item in findings:

        print(f"Time: {item['timestamp']}")
        print(f"Identity: {item['identity']}")
        print(f"Vehicle: {item['vehicle']}")
        print(f"Threat Actor: {item['threat_actor']}")
        print(f"Severity: {item['severity']}")
        print(f"MITRE Technique: {item['mitre_technique']}")
        print(f"Description: {item['description']}")
        print(f"Reason: {item['event_reason']}")
        print("-" * 40)

    report_name = (
        f"threat_intelligence_report_"
        f"{datetime.now().strftime('%H%M%S')}.json"
    )

    with open(report_name, "w") as f:
        json.dump(findings, f, indent=4)

    print(f"\n[SAVED] {report_name}")

# ---------------------------------
# MAIN
# ---------------------------------
if __name__ == "__main__":

    print("[INFO] Starting Threat Intelligence Engine...\n")

    logs = fetch_logs()

    print(f"[INFO] Logs Retrieved: {len(logs)}")

    findings = correlate_iocs(logs)

    print(f"[INFO] Threat Matches: {len(findings)}")

    generate_report(findings)

