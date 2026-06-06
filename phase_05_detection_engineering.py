import requests
import time
from collections import defaultdict
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

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

identity_risk = defaultdict(int)
processed_events = set()


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

            identity_risk[identity] += mapping["score"]

            print(f"[{mapping['severity']}] {identity} risk = {identity_risk[identity]}")


# -----------------------------
# SAFE ENTRYPOINT (NO LOOP)
# -----------------------------
def main():
    print("Phase 05 safe run start")

    logs = fetch_logs()
    process_logs(logs)

    print("Phase 05 completed (single run)")


def test_main():
    print("safe execution ok")


if __name__ == "__main__":
    # ONLY runs when executed directly, NOT in pytest
    while True:
        logs = fetch_logs()
        process_logs(logs)
        print(f"[HEARTBEAT] {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(5)