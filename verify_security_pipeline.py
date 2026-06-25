import requests
import json
import time

BASE = "http://127.0.0.1:5000"

# =========================
# AUTH HEADERS
# =========================

DEV_HEADERS = {
    "X-API-KEY": "dev-key-123",
    "X-Role": "developer"
}

SUPPORT_HEADERS = {
    "X-API-KEY": "support-key-456",
    "X-Role": "support"
}

# =========================
# UTIL
# =========================

def print_result(name, resp, expected_status=None):
    print(f"\n== {name} ==")
    print("Status:", resp.status_code)

    try:
        print("Body:", resp.json())
    except Exception:
        print("Body:", resp.text)

    if expected_status is not None:
        if resp.status_code != expected_status:
            print(f"❌ Expected {expected_status}, got {resp.status_code}")


# =========================
# REQUESTS
# =========================

def test_unlock_valid():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR123"},
        headers=DEV_HEADERS
    )

def test_unlock_invalid_vehicle():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR999"},
        headers=DEV_HEADERS
    )

def test_unlock_unauthorized():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR123"},
        headers=SUPPORT_HEADERS
    )

def test_logs_access():
    return requests.get(
        f"{BASE}/logs",
        headers=DEV_HEADERS
    )

def test_status_valid():
    return requests.get(
        f"{BASE}/status?vehicle_id=CAR123",
        headers=DEV_HEADERS
    )

def test_status_rate_limit():
    results = []

    for i in range(6):
        r = requests.get(
            f"{BASE}/status?vehicle_id=CAR123",
            headers=DEV_HEADERS
        )
        results.append(r.status_code)
        time.sleep(0.1)

    return results

def test_pipeline_execution():
    import verify_security_pipeline as vp

    if hasattr(vp, "run_pipeline"):
        vp.run_pipeline()

    if hasattr(vp, "main"):
        vp.main()

# =========================
# MAIN
# =========================

def main():

    print("\n--- PHASE 1: Unlock behavior ---")

    print_result("Valid unlock", test_unlock_valid(), 200)
    print_result("Invalid vehicle (should be 404)", test_unlock_invalid_vehicle(), 404)
    print_result("Unauthorized role (should be 403)", test_unlock_unauthorized(), 403)

    print("\n--- PHASE 2: Logs access control ---")

    print_result("Logs access", test_logs_access(), 200)

    print("\n--- PHASE 3: Status + rate limiting ---")

    print_result("Valid status", test_status_valid(), 200)

    print("Rate limit test results:")
    print(test_status_rate_limit())

    print("\n--- PHASE 4: JSON integrity check ---")

    logs_resp = test_logs_access()

    try:
        data = logs_resp.json()
        json.dumps(data)
        print("✔ Logs JSON is valid and serializable")
    except Exception as e:
        print("❌ JSON error:", e)

    print("\n--- DONE ---")


if __name__ == "__main__":
    main()

def test_main():
    return True
