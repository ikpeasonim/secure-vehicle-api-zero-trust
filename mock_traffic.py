import requests
import time

BASE_URL = "http://127.0.0.1:5000"

DEV_HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": "dev-key-123"
}

SUPPORT_HEADERS = {
    "Content-Type": "application/json",
    "X-API-KEY": "support-key-456"
}


def run_request(method, endpoint, headers=None, json_data=None):
    try:
        if method == "GET":
            response = requests.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                timeout=5
            )
        else:
            response = requests.post(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                json=json_data,
                timeout=5
            )

        print(
            f"{method} {endpoint} -> "
            f"{response.status_code} "
            f"{response.text}"
        )

    except Exception as e:
        print(f"ERROR: {e}")


print("\nGenerating baseline traffic...\n")

# -------------------------------------------------
# Valid developer actions
# -------------------------------------------------

run_request(
    "POST",
    "/unlock",
    DEV_HEADERS,
    {"vehicle_id": "CAR123"}
)

time.sleep(1)

run_request(
    "POST",
    "/start",
    DEV_HEADERS,
    {"vehicle_id": "CAR123"}
)

time.sleep(1)

run_request(
    "GET",
    "/status?vehicle_id=CAR123",
    DEV_HEADERS
)

# -------------------------------------------------
# Valid support actions
# -------------------------------------------------

time.sleep(1)

run_request(
    "POST",
    "/unlock",
    SUPPORT_HEADERS,
    {"vehicle_id": "CAR456"}
)

time.sleep(1)

run_request(
    "POST",
    "/start",
    SUPPORT_HEADERS,
    {"vehicle_id": "CAR456"}
)

# -------------------------------------------------
# Unauthorized access attempts
# -------------------------------------------------

time.sleep(1)

run_request(
    "POST",
    "/unlock",
    DEV_HEADERS,
    {"vehicle_id": "CAR456"}
)

time.sleep(1)

run_request(
    "POST",
    "/unlock",
    SUPPORT_HEADERS,
    {"vehicle_id": "CAR123"}
)

# -------------------------------------------------
# Invalid vehicle requests
# -------------------------------------------------

time.sleep(1)

run_request(
    "POST",
    "/unlock",
    DEV_HEADERS,
    {"vehicle_id": "CAR999"}
)

# -------------------------------------------------
# Logs access
# -------------------------------------------------

time.sleep(1)

run_request(
    "GET",
    "/logs",
    DEV_HEADERS
)

time.sleep(1)

run_request(
    "GET",
    "/logs",
    SUPPORT_HEADERS
)

# -------------------------------------------------
# Trigger rate limiting
# -------------------------------------------------

print("\nTriggering rate limit...\n")

for _ in range(7):
    run_request(
        "GET",
        "/status?vehicle_id=CAR123",
        DEV_HEADERS
    )
    time.sleep(0.3)

print("\nDone.\n")
