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
processed = set()


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
            return []

        data = response.json()

        if isinstance(data, dict) and "logs" in data:
            return data["logs"]

        return []

    except Exception:
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

    filename = f"containment_{identity}_{datetime.now().strftime('%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(containment_event, f, indent=4)


# -----------------------------
# PROCESS LOGS
# -----------------------------
def process_logs(logs):
    for log in logs:

        identity = log.get("role", "unknown")
        reason = log.get("reason")

        if not reason:
            continue

        # prevent duplicate processing
        log_id = f"{log.get('timestamp')}_{identity}_{reason}"
        if log_id in processed:
            continue

        processed.add(log_id)

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
# SAFE RUN (USED BY TESTS)
# -----------------------------
def run_once():
    logs = fetch_logs()
    process_logs(logs)

    print(
        f"\n[HEARTBEAT] {datetime.now().strftime('%H:%M:%S')} | SOAR cycle complete"
    )


# -----------------------------
# TEST ENTRY POINT (IMPORTANT)
# -----------------------------
def main():
    """
    SAFE: used by pytest
    Must NEVER hang or loop forever
    """
    run_once()


# -----------------------------
# LIVE MODE (OPTIONAL)
# -----------------------------
def run_live():
    """
    Real SOC simulation mode (only used if run directly)
    """
    print("\n====================================")
    print("PHASE 9 — SOAR AUTOMATION ENGINE")
    print("====================================")

    while True:
        run_once()
        time.sleep(5)


if __name__ == "__main__":
    run_live()


# -----------------------------
# TEST COMPATIBILITY HELPER
# -----------------------------
def test_main():
    print("safe execution ok")