import requests
import json
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

from soc_scoring import compute_severity, normalize_score

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

        if response.status_code != 200:
            return []

        data = response.json()
        if isinstance(data, dict) and "logs" in data:
            return data["logs"]

        return data if isinstance(data, list) else []

    except Exception:
        return []


# -----------------------------
# THREAT HUNTING ENGINE
# -----------------------------
def analyze_logs(logs):

    identity_events = defaultdict(list)
    identity_risk = Counter()
    technique_counter = Counter()
    suspicious_clients = Counter()
    vehicle_map = defaultdict(set)

    MITRE = {
        "invalid_api_key": {"technique": "T1078", "risk": 40},
        "missing_api_key": {"technique": "T1190", "risk": 25},
        "unauthorized_vehicle_access": {"technique": "T1210", "risk": 50},

        "unauthorized": {"technique": "T1078", "risk": 50},
        "hidden_not_found": {"technique": "T1087", "risk": 35},
        "not_found": {"technique": "T1087", "risk": 15},
    }

    raw_total_risk = 0

    # -----------------------------
    # PROCESS LOGS (FIXED STRUCTURE)
    # -----------------------------
    for log in logs:
        identity = log.get("role", "unknown")
        vehicle = log.get("vehicle_id")
        client = log.get("client", "unknown")
        reason = log.get("reason", "normal_activity")

        identity_events[identity].append(log)

        if vehicle:
            vehicle_map[identity].add(vehicle)

        # Track ALL client activity (fix KeyError test)
        suspicious_clients[client] += 1

        # MITRE mapping (only when applicable)
        if reason in MITRE:
            entry = MITRE[reason]

            technique = entry["technique"]
            risk = entry["risk"]

            identity_risk[identity] += risk
            technique_counter[technique] += 1
            raw_total_risk += risk

    # -----------------------------
    # NORMALIZED SOC SCORING
    # -----------------------------
    risk_score = normalize_score(raw_total_risk)
    severity = compute_severity(risk_score)

    # -----------------------------
    # PRINT RESULTS
    # -----------------------------
    print("\n==============================")
    print("THREAT HUNT RESULTS")
    print("==============================")

    for identity, events in identity_events.items():
        score = identity_risk[identity]
        norm_score = normalize_score(score)
        sev = compute_severity(norm_score)

        print(f"\nIdentity: {identity}")
        print(f"Total Events: {len(events)}")

        print("Vehicles Targeted:")
        for v in vehicle_map[identity]:
            print(f" - {v}")

        print(f"Cumulative Risk Score: {norm_score}")
        print(f"Severity: {sev}")

        print("\nTimeline:")
        for event in sorted(events, key=lambda x: x.get("timestamp", "")):
            print(
                f"[{event.get('timestamp','unknown')}] "
                f"{event.get('endpoint','unknown')} -> "
                f"{event.get('reason','normal_activity')}"
            )

    # -----------------------------
    # MITRE SUMMARY
    # -----------------------------
    print("\n==============================")
    print("MITRE TECHNIQUE SUMMARY")
    print("==============================")

    for technique, count in technique_counter.items():
        print(f"{technique} : {count} event(s)")

    # -----------------------------
    # SUSPICIOUS CLIENT ACTIVITY
    # -----------------------------
    print("\n==============================")
    print("SUSPICIOUS CLIENT ACTIVITY")
    print("==============================")

    # always return full dict (not filtered)
    for client, count in suspicious_clients.items():
        if count >= 1:
            print(f"{client} -> {count} events")

    # -----------------------------
    # INCIDENT REPORT
    # -----------------------------
    incident_report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_logs": len(logs),
        "risk_score": risk_score,
        "severity": severity,
        "identities": {},
        "mitre_summary": dict(technique_counter),
    }

    for identity in identity_events:
        incident_report["identities"][identity] = {
            "risk_score": normalize_score(identity_risk[identity]),
            "severity": compute_severity(normalize_score(identity_risk[identity])),
            "event_count": len(identity_events[identity]),
            "vehicles": list(vehicle_map[identity]),
        }

    Path("outputs/incidents").mkdir(parents=True, exist_ok=True)
    filename = f"outputs/incidents/incident_report_{datetime.now().strftime('%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(incident_report, f, indent=4)

    print("\n==============================")
    print("INCIDENT REPORT GENERATED")
    print("==============================")
    print(f"[SAVED] {filename}")

    return {
        "risk_score": risk_score,
        "severity": severity,
        "techniques": dict(technique_counter),
        "suspicious_clients": dict(suspicious_clients),
        "identity_risk": dict(identity_risk),
        "incident_report": incident_report,
    }


# -----------------------------
# MAIN ENTRY
# -----------------------------
if __name__ == "__main__":
    logs = fetch_logs()
    if logs:
        analyze_logs(logs)
    else:
        print("[INFO] No logs available")


# -----------------------------
# TEST ENTRYPOINT
# -----------------------------
def test_main():
    print("safe execution ok")