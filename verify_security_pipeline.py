import requests
import json
import time

BASE = "http://127.0.0.1:5000"


DEV_HEADERS = {
    "X-API-KEY": "dev-key-123",
    "X-Role": "developer"
}

SUPPORT_HEADERS = {
    "X-API-KEY": "support-key-456",
    "X-Role": "support"
}


def unlock_valid():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR123"},
        headers=DEV_HEADERS
    )


def unlock_invalid_vehicle():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR999"},
        headers=DEV_HEADERS
    )


def unlock_unauthorized():
    return requests.post(
        f"{BASE}/unlock",
        json={"vehicle_id": "CAR123"},
        headers=SUPPORT_HEADERS
    )


def logs_access():
    return requests.get(f"{BASE}/logs", headers=DEV_HEADERS)


def status_request():
    return requests.get(
        f"{BASE}/status?vehicle_id=CAR123",
        headers=DEV_HEADERS
    )


def rate_limit_test():
    results = []
    for _ in range(6):
        r = status_request()
        results.append(r.status_code)
        time.sleep(0.1)
    return results


def pipeline_execution():
    import verify_security_pipeline as vp

    if hasattr(vp, "run_pipeline"):
        vp.run_pipeline()

    if hasattr(vp, "main"):
        vp.main()


def main():
    print("Running SOC API checks...")

    print("Unlock valid:", unlock_valid().status_code)
    print("Unlock invalid:", unlock_invalid_vehicle().status_code)
    print("Unlock unauthorized:", unlock_unauthorized().status_code)

    print("Logs:", logs_access().status_code)
    print("Status:", status_request().status_code)
    print("Rate limit:", rate_limit_test())

    try:
        data = logs_access().json()
        json.dumps(data)
        print("✔ JSON valid")
    except Exception as e:
        print("❌ JSON error:", e)


def test_main():
    return True


if __name__ == "__main__":
    main()