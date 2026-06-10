import time
import random
import requests

EVENTS = [
    "BRUTE_FORCE",
    "AUTH_SPIKE",
    "DEVICE_CHANGE",
    "BASELINE_DEVIATION",
    "PRIVILEGE_ABUSE",
    "VEHICLE_COMMAND_ACCESS"
]

VEHICLES = ["CAR100", "CAR101", "CAR102", "CAR103", "CAR104"]


def generate_event():
    return {
        "user": "analyst",
        "action": random.choice(EVENTS),
        "vehicle_id": random.choice(VEHICLES),
        "auth": True
    }


url = "http://localhost:5000/ingest"

for i in range(20):  # prevent infinite loop
    try:
        r = requests.post(url, json=generate_event(), timeout=5)

        print("\n--- EVENT ---")
        print("STATUS:", r.status_code)
        print("RAW:", r.text)

        if r.headers.get("content-type", "").startswith("application/json"):
            print("JSON:", r.json())

    except Exception as e:
        print("Request failed:", str(e))

    time.sleep(0.5)