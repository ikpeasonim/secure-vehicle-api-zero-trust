import requests
import time
from collections import defaultdict
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

# -----------------------------
# MITRE ATT&CK MAPPING
# -----------------------------
ATTACK_MAPPING = {
    "invalid_api_key": {
        "technique": "T1078",
        "name": "Valid Accounts",
        "severity": "HIGH",
        "score": 40
    },

    "missing_api_key": {
        "technique": "T1190",
        "name": "Exploit Public-Facing Application",
        "severity": "MEDIUM",
        "score": 20
    },

    "unauthorized_vehicle_access": {
        "technique": "T1210",
        "name": "Exploitation of Remote Services",
        "severity": "HIGH",
        "score": 50
    }
}

# -----------------------------
# RISK TRACKING
# -----------------------------
identity_risk = defaultdict(int)

processed_events = set()

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
            print("[ERROR] Unable to fetch logs")
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

# -----------------------------
# DETECTION ENGINE
# -----------------------------
def process_logs(logs):

    for log in logs:

        timestamp = log.get("timestamp")
        reason = log.get("reason")
        identity = log.get("role", "unknown")
        vehicle_id = log.get("vehicle_id", "unknown")

        unique_event = f"{timestamp}-{reason}-{identity}"

        if unique_event in processed_events:
            continue

        processed_events.add(unique_event)

        if reason in ATTACK_MAPPING:

            mapping = ATTACK_MAPPING[reason]

            technique = mapping["technique"]
            attack_name = mapping["name"]
            severity = mapping["severity"]
            score = mapping["score"]

            identity_risk[identity] += score

            print("\n==============================")
            print(f"[{severity} ALERT]")
            print("==============================")

            print(f"Time: {timestamp}")
            print(f"Identity: {identity}")
            print(f"Vehicle: {vehicle_id}")
            print(f"Reason: {reason}")

            print(f"MITRE Technique: {technique}")
            print(f"Attack Name: {attack_name}")

            print(f"Risk Added: {score}")
            print(f"Cumulative Risk: {identity_risk[identity]}")

            # Escalation
            if identity_risk[identity] >= 100:

                print("\n[CRITICAL]")
                print(
                    f"Identity '{identity}' "
                    f"exceeded critical risk threshold!"
                )

# -----------------------------
# MAIN LOOP
# -----------------------------
print("\n🛡️ STARTING PHASE 5 DETECTION ENGINE\n")

while True:

    logs = fetch_logs()

    process_logs(logs)

    print(
        f"\n[HEARTBEAT] "
        f"{datetime.now().strftime('%H:%M:%S')} "
        f"| Monitoring active..."
    )

    time.sleep(5)