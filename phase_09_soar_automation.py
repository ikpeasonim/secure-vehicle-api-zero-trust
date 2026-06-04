import requests
import json
import time
from collections import defaultdict
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

API_HEADERS = {
    "X-API-KEY": "dev-key-123"
}

# -----------------------------
# SOAR PLAYBOOK CONFIGURATION
# -----------------------------
RISK_SCORES = {
    "missing_api_key": 40,
    "invalid_api_key": 50,
    "unauthorized_vehicle_access": 75
}

CRITICAL_THRESHOLD = 200

# -----------------------------
# TRACKING STRUCTURES
# -----------------------------
identity_risk = defaultdict(int)
contained_identities = set()

# -----------------------------
# FETCH LOGS
# -----------------------------
def fetch_logs():

    try:
        response = requests.get(
            f"{BASE_URL}/logs",
            headers=API_HEADERS,
            timeout=5
        )

        if response.status_code != 200:
            print("[ERROR] Failed to retrieve logs")
            return []

        data = response.json()

        if isinstance(data, dict) and "logs" in data:
            return data["logs"]

        return []

    except Exception as e:
        print(f"[ERROR] {e}")
        return []

# -----------------------------
# CONTAINMENT ACTION
# -----------------------------
def execute_containment(identity, reason):

    containment_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "identity": identity,
        "containment_action": "API_KEY_DISABLED",
        "reason": reason,
        "status": "EXECUTED"
    }

    contained_identities.add(identity)

    print("\n==============================")
    print("[SOAR ACTION EXECUTED]")
    print("==============================")
    print(json.dumps(containment_event, indent=4))

    filename = (
        f"containment_{identity}_"
        f"{datetime.now().strftime('%H%M%S')}.json"
    )

    with open(filename, "w") as f:
        json.dump(containment_event, f, indent=4)

    print(f"[SAVED] {filename}")

# -----------------------------
# PROCESS EVENTS
# -----------------------------
def process_logs(logs):

    for log in logs:

        identity = log.get("role", "unknown")
        reason = log.get("reason")

        if not reason:
            continue

        risk = RISK_SCORES.get(reason, 0)

        identity_risk[identity] += risk

        print("\n==============================")
        print("[SOAR ANALYSIS]")
        print("==============================")
        print(f"Identity: {identity}")
        print(f"Reason: {reason}")
        print(f"Risk Added: {risk}")
        print(f"Cumulative Risk: {identity_risk[identity]}")

        if (
            identity_risk[identity] >= CRITICAL_THRESHOLD
            and identity not in contained_identities
        ):

            print("\n[CRITICAL]")
            print(f"Identity '{identity}' exceeded threshold")

            execute_containment(identity, reason)

# -----------------------------
# MAIN LOOP
# -----------------------------
print("\n====================================")
print("PHASE 9 — SOAR AUTOMATION ENGINE")
print("====================================")

processed = set()

while True:

    logs = fetch_logs()

    new_logs = []

    for log in logs:

        log_id = (
            f"{log.get('timestamp')}_"
            f"{log.get('role')}_"
            f"{log.get('reason')}"
        )

        if log_id not in processed:
            processed.add(log_id)
            new_logs.append(log)

    process_logs(new_logs)

    print(
        f"\n[HEARTBEAT] "
        f"{datetime.now().strftime('%H:%M:%S')} "
        f"| SOAR ACTIVE..."
    )

    time.sleep(5)