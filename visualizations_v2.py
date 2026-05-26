import requests
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

# -----------------------------
# FETCH LOGS
# -----------------------------
def fetch_logs():

    try:
        response = requests.get(
            f"{BASE_URL}/logs",
            headers={"X-API-KEY": "dev-key-123"},
            timeout=5
        )

        print(f"[INFO] STATUS CODE: {response.status_code}")

        if response.status_code != 200:
            print("[ERROR] Failed to fetch logs")
            return []

        data = response.json()

        print(f"[DEBUG] RESPONSE TYPE: {type(data)}")

        if isinstance(data, dict) and "logs" in data:
            logs = data["logs"]

        elif isinstance(data, list):
            logs = data

        else:
            print("[ERROR] Unexpected response structure")
            return []

        print(f"[DEBUG] LOG COUNT: {len(logs)}")

        return logs

    except Exception as e:
        print(f"[ERROR] {e}")
        return []


# -----------------------------
# LOAD LOGS
# -----------------------------
logs = fetch_logs()

# -----------------------------
# COUNTERS
# -----------------------------
endpoint_counter = Counter()
vehicle_counter = Counter()
failure_counter = Counter()

# -----------------------------
# PROCESS LOGS
# -----------------------------
for log in logs:

    endpoint = log.get("endpoint", "unknown")
    vehicle_id = log.get("vehicle_id", "unknown")

    reason = (
        log.get("reason")
        or log.get("failure_reason")
    )

    endpoint_counter[endpoint] += 1

    if vehicle_id:
        vehicle_counter[vehicle_id] += 1

    if reason:
        failure_counter[reason] += 1


# -----------------------------
# ENDPOINT GRAPH
# -----------------------------
if endpoint_counter:

    plt.figure(figsize=(8, 5))

    plt.bar(
        list(endpoint_counter.keys()),
        list(endpoint_counter.values())
    )

    plt.title("Requests per Endpoint")
    plt.xlabel("Endpoint")
    plt.ylabel("Request Count")

    plt.tight_layout()

    endpoint_file = (
        f"requests_per_endpoint_"
        f"{datetime.now().strftime('%H%M%S')}.png"
    )

    plt.savefig(endpoint_file)

    print(f"[SAVED] {endpoint_file}")

    plt.close()


# -----------------------------
# VEHICLE GRAPH
# -----------------------------
if vehicle_counter:

    plt.figure(figsize=(8, 5))

    plt.bar(
        list(vehicle_counter.keys()),
        list(vehicle_counter.values())
    )

    plt.title("Requests per Vehicle")
    plt.xlabel("Vehicle ID")
    plt.ylabel("Request Count")

    plt.tight_layout()

    vehicle_file = (
        f"requests_per_vehicle_"
        f"{datetime.now().strftime('%H%M%S')}.png"
    )

    plt.savefig(vehicle_file)

    print(f"[SAVED] {vehicle_file}")

    plt.close()


# -----------------------------
# FAILURE GRAPH
# -----------------------------
if failure_counter:

    plt.figure(figsize=(9, 5))

    plt.bar(
        list(failure_counter.keys()),
        list(failure_counter.values())
    )

    plt.title("Security Failure Events")
    plt.xlabel("Failure Type")
    plt.ylabel("Event Count")

    plt.tight_layout()

    failure_file = (
        f"security_failures_"
        f"{datetime.now().strftime('%H%M%S')}.png"
    )

    plt.savefig(failure_file)

    print(f"[SAVED] {failure_file}")

    plt.close()


# -----------------------------
# SUMMARY
# -----------------------------
print("\n=== VISUALIZATION COMPLETE ===")
print(f"Total Logs: {len(logs)}")
print(f"Endpoints: {len(endpoint_counter)}")
print(f"Vehicles: {len(vehicle_counter)}")
print(f"Failure Types: {len(failure_counter)}")