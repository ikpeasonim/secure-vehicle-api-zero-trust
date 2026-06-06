import requests
import json
from collections import defaultdict, Counter
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
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

        print(f"[DEBUG] RESPONSE TYPE: {type(data)}")

        # Handle wrapped JSON format
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
# THREAT HUNTING ENGINE
# -----------------------------
def analyze_logs(logs):

    identity_activity = defaultdict(list)
    vehicle_targets = defaultdict(set)
    identity_risk = Counter()
    technique_counter = Counter()
    suspicious_clients = Counter()

    # MITRE Mapping
    mitre_mapping = {
        "invalid_api_key": {
            "technique": "T1078",
            "name": "Valid Accounts",
            "risk": 40
        },

        "missing_api_key": {
            "technique": "T1190",
            "name": "Exploit Public-Facing Application",
            "risk": 25
        },

        "unauthorized_vehicle_access": {
            "technique": "T1210",
            "name": "Exploitation of Remote Services",
            "risk": 50
        }
    }

    # -----------------------------
    # PROCESS LOGS
    # -----------------------------
    for log in logs:

        identity = log.get("role", "unknown")
        vehicle = log.get("vehicle_id", "unknown")
        client = log.get("client", "unknown")
        reason = log.get("reason")
        timestamp = log.get("timestamp")
        success = log.get("success")

        identity_activity[identity].append(log)

        if vehicle:
            vehicle_targets[identity].add(vehicle)

        suspicious_clients[client] += 1

        # Risk Scoring
        if reason in mitre_mapping:

            risk = mitre_mapping[reason]["risk"]

            identity_risk[identity] += risk

            technique = mitre_mapping[reason]["technique"]

            technique_counter[technique] += 1

    # -----------------------------
    # PRINT THREAT HUNT RESULTS
    # -----------------------------
    print("\n==============================")
    print("THREAT HUNT RESULTS")
    print("==============================")

    for identity, events in identity_activity.items():

        print(f"\nIdentity: {identity}")

        print(f"Total Events: {len(events)}")

        print("Vehicles Targeted:")

        for vehicle in vehicle_targets[identity]:
            print(f" - {vehicle}")

        print(f"Cumulative Risk Score: {identity_risk[identity]}")

        # Severity Classification
        if identity_risk[identity] >= 200:
            severity = "CRITICAL"

        elif identity_risk[identity] >= 100:
            severity = "HIGH"

        elif identity_risk[identity] >= 50:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        print(f"Severity: {severity}")

        # Timeline Reconstruction
        print("\nTimeline:")

        sorted_events = sorted(
            events,
            key=lambda x: x.get("timestamp", "")
        )

        for event in sorted_events:

            event_time = event.get("timestamp", "unknown")
            reason = event.get("reason", "normal_activity")
            endpoint = event.get("endpoint", "unknown")

            print(f"[{event_time}] {endpoint} -> {reason}")

    # -----------------------------
    # MITRE SUMMARY
    # -----------------------------
    print("\n==============================")
    print("MITRE TECHNIQUE SUMMARY")
    print("==============================")

    for technique, count in technique_counter.items():

        print(f"{technique} : {count} event(s)")

    # -----------------------------
    # SUSPICIOUS CLIENTS
    # -----------------------------
    print("\n==============================")
    print("SUSPICIOUS CLIENT ACTIVITY")
    print("==============================")

    for client, count in suspicious_clients.items():

        if count >= 3:

            print(f"{client} -> {count} events")

    # -----------------------------
    # EXPORT INCIDENT REPORT
    # -----------------------------
    incident_report = {
        "generated_at": datetime.utcnow().isoformat(),
        "total_logs": len(logs),
        "identities": {},
        "mitre_summary": dict(technique_counter)
    }

    for identity in identity_activity:

        incident_report["identities"][identity] = {
            "risk_score": identity_risk[identity],
            "vehicles_targeted": list(vehicle_targets[identity]),
            "event_count": len(identity_activity[identity]),
            "events": identity_activity[identity]
        }

    filename = (
        f"incident_report_"
        f"{datetime.now().strftime('%H%M%S')}.json"
    )

    with open(filename, "w") as f:
        json.dump(incident_report, f, indent=4)

    print("\n==============================")
    print("INCIDENT REPORT GENERATED")
    print("==============================")

    print(f"[SAVED] {filename}")


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    logs = fetch_logs()

    if not logs:
        print("[INFO] No logs available")

    else:
        analyze_logs(logs)

# phase_06_threat_hunting.py
def main():
    print("Phase 06: Threat Hunting")
    from time import sleep
    sleep(0.1)
    print("Phase 06 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")