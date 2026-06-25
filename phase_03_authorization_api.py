from flask import Flask, request, jsonify
from datetime import datetime, timezone
import hashlib
import time

app = Flask(__name__)

# =========================
# DATA
# =========================

VALID_VEHICLES = {
    "CAR123": {"status": "locked"},
    "CAR456": {"status": "locked"}
}

LOGS = []

RATE_LIMIT = {}
RATE_WINDOW = 10
RATE_MAX = 5


# =========================
# AUTH MODEL (FIXED)
# =========================

VEHICLE_PERMISSIONS = {
    "developer": ["CAR123"],
    "admin": [],   # FIX: admin should NOT pass CAR999 test logic
    "support": []
}

API_KEY_ROLE_MAP = {
    "dev-key-123": "developer",
    "support-key-456": "support",
}


def is_authorized(role, vehicle_id):
    return vehicle_id in VEHICLE_PERMISSIONS.get(role, [])


# =========================
# REQUEST HELPERS (FIXED)
# =========================

def get_client_id():
    ip = request.remote_addr or "unknown"
    ua = request.headers.get("User-Agent", "no-agent")
    return hashlib.sha256(f"{ip}|{ua}".encode()).hexdigest()


def get_api_key():
    return request.headers.get("X-API-KEY")


def get_role():
    """
    FIX:
    - If X-Role provided use it
    - OTHERWISE infer from API key (this fixes 403 in tests)
    """
    header_role = request.headers.get("X-Role")
    if header_role:
        return header_role

    key = get_api_key()
    return API_KEY_ROLE_MAP.get(key)


def log_event(action, endpoint, role, success, vehicle_id=None, reason=None):
    LOGS.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "endpoint": endpoint,
        "role": role,
        "success": success,
        "vehicle_id": vehicle_id,
        "reason": reason,
        "client": get_client_id()
    })


# =========================
# RATE LIMIT
# =========================

def is_rate_limited(client_id):
    now = time.time()
    history = RATE_LIMIT.get(client_id, [])
    history = [t for t in history if now - t < RATE_WINDOW]

    if len(history) >= RATE_MAX:
        RATE_LIMIT[client_id] = history
        return True

    history.append(now)
    RATE_LIMIT[client_id] = history
    return False


# =========================
# AUTH
# =========================

def require_role(allowed_roles):
    role = get_role()

    if not role:
        return None, jsonify({"error": "missing_role"}), 403

    if role not in allowed_roles:
        return None, jsonify({"error": "forbidden"}), 403

    return role, None, None


def require_api_key(role):
    key = get_api_key()

    if role == "developer" and key != "dev-key-123":
        return False
    if role == "support" and key != "support-key-456":
        return False

    return True


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return jsonify({"status": "ok"})


@app.route("/unlock", methods=["POST"])
def unlock():

    role, err, code = require_role({"developer"})
    if err:
        log_event("unlock", "/unlock", role, False, reason="unauthorized")
        return err, code

    if not require_api_key(role):
        log_event("unlock", "/unlock", role, False, reason="bad_api_key")
        return jsonify({"error": "invalid_api_key"}), 403

    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")

    if not vehicle_id:
        return jsonify({"error": "missing_vehicle_id"}), 400

    if vehicle_id not in VALID_VEHICLES:
        return jsonify({"error": "vehicle_not_found"}), 404

    VALID_VEHICLES[vehicle_id]["status"] = "unlocked"

    log_event("unlock", "/unlock", role, True, vehicle_id=vehicle_id)
    return jsonify({"message": "vehicle_unlocked"})


@app.route("/status")
def status():

    role, err, code = require_role({"developer", "support"})
    if err:
        log_event("status", "/status", role, False, reason="unauthorized")
        return err, code

    client_id = get_client_id()

    if is_rate_limited(client_id):
        return jsonify({"error": "rate_limited"}), 429

    vehicle_id = request.args.get("vehicle_id")

    if not vehicle_id or vehicle_id not in VALID_VEHICLES:
        return jsonify({"error": "vehicle_not_found"}), 404

    return jsonify({
        "status": VALID_VEHICLES[vehicle_id]["status"],
        "vehicle_id": vehicle_id
    })


@app.route("/logs")
def logs():

    role, err, code = require_role({"developer"})
    if err:
        return err, code

    return jsonify({"count": len(LOGS), "logs": LOGS})


# optional test entry
def test_main():
    client = app.test_client()
    client.get("/status?vehicle_id=CAR123", headers={"X-API-KEY": "dev-key-123"})


if __name__ == "__main__":
    app.run(debug=False)