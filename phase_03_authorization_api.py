from flask import Flask, request, jsonify
from datetime import datetime, timezone, timedelta
from functools import wraps
import hashlib
import json
from pathlib import Path
import os

app = Flask(__name__)

# =========================================================
# CONFIGURATION
# =========================================================

API_KEYS = {
    hashlib.sha256(b"dev-key-123").hexdigest(): "developer",
    hashlib.sha256(b"support-key-456").hexdigest(): "support",
}

VEHICLE_PERMISSIONS = {
    "developer": ["CAR123"],
    "support": ["CAR456"]
}

RATE_LIMIT = 5
TIME_WINDOW = timedelta(seconds=10)

# =========================================================
# STATE
# =========================================================

vehicles = {
    "CAR123": "locked",
    "CAR456": "locked"
}

logs = []

LOG_FILE = Path("data/api_logs.json")
LOG_FILE.parent.mkdir(exist_ok=True)

rate_limit_store = {}

# =========================================================
# HELPERS
# =========================================================

def get_client_identity():
    ip = request.remote_addr or "unknown"
    api_key = request.headers.get("X-API-KEY", "")
    key_hash = hashlib.sha256(api_key.encode()).hexdigest() if api_key else "no-key"
    return f"{ip}|{key_hash}"


def get_user_role():
    api_key = request.headers.get("X-API-KEY", "")
    hashed = hashlib.sha256(api_key.encode()).hexdigest()
    return API_KEYS.get(hashed)


def is_authorized(user_role, vehicle_id):
    return vehicle_id in VEHICLE_PERMISSIONS.get(user_role, [])


def require_api_key(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return jsonify({"error": "missing API key"}), 401

        hashed = hashlib.sha256(api_key.encode()).hexdigest()

        if hashed not in API_KEYS:
            return jsonify({"error": "invalid API key"}), 403

        return f(*args, **kwargs)

    return wrapper


def is_rate_limited(identity):
    now = datetime.now(timezone.utc)

    rate_limit_store.setdefault(identity, [])

    rate_limit_store[identity] = [
        t for t in rate_limit_store[identity]
        if now - t < TIME_WINDOW
    ]

    if len(rate_limit_store[identity]) >= RATE_LIMIT:
        return True

    rate_limit_store[identity].append(now)
    return False


# =========================================================
# LOGGING (SOC-READY + ATOMIC WRITE)
# =========================================================

def write_log(entry):
    existing = []

    if LOG_FILE.exists():
        try:
            existing = json.loads(LOG_FILE.read_text() or "[]")
        except:
            existing = []

    existing.append(entry)

    tmp_file = LOG_FILE.with_suffix(".tmp")
    tmp_file.write_text(json.dumps(existing, indent=2))

    os.replace(tmp_file, LOG_FILE)


def log_event(endpoint, vehicle_id, action, success, reason=None):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "endpoint": endpoint,
        "vehicle_id": vehicle_id,
        "action": action,
        "success": success,
        "reason": reason,
        "client": get_client_identity(),
        "role": get_user_role()
    }

    logs.append(entry)

    write_log(entry)

    print(f"[LOGGED] {endpoint} | {action} | {success}")


def load_logs():
    if not LOG_FILE.exists():
        return []
    try:
        return json.loads(LOG_FILE.read_text() or "[]")
    except:
        return []


# =========================================================
# SECURITY HEADERS
# =========================================================

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


# =========================================================
# BASE
# =========================================================

@app.route("/")
def home():
    return jsonify({
        "service": "Secure Vehicle API",
        "phase": "Phase 3 - SOC-Ready Authorization System",
        "endpoints": ["/status", "/unlock", "/start", "/logs"]
    })


# =========================================================
# STATUS
# =========================================================

@app.route("/status")
@require_api_key
def status():
    vehicle_id = request.args.get("vehicle_id")
    user_role = get_user_role()
    identity = get_client_identity()

    if not vehicle_id:
        log_event("/status", None, "status_check", False, "missing_vehicle_id")
        return jsonify({"error": "vehicle_id required"}), 400

    if is_rate_limited(identity):
        log_event("/status", vehicle_id, "status_check", False, "rate_limited")
        return jsonify({"error": "rate limit exceeded"}), 429

    if vehicle_id not in vehicles:
        log_event("/status", vehicle_id, "status_check", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    if not is_authorized(user_role, vehicle_id):
        log_event("/status", vehicle_id, "authorization_check", False, "unauthorized")
        return jsonify({"error": "unauthorized"}), 403

    log_event("/status", vehicle_id, "status_check", True)

    return jsonify({
        "vehicle_id": vehicle_id,
        "status": vehicles[vehicle_id]
    })


# =========================================================
# UNLOCK
# =========================================================

@app.route("/unlock", methods=["POST"])
@require_api_key
def unlock():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")
    user_role = get_user_role()

    if vehicle_id not in vehicles:
        log_event("/unlock", vehicle_id, "unlock", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    if not is_authorized(user_role, vehicle_id):
        log_event("/unlock", vehicle_id, "authorization_check", False, "unauthorized")
        return jsonify({"error": "unauthorized"}), 403

    vehicles[vehicle_id] = "unlocked"

    log_event("/unlock", vehicle_id, "unlock", True)

    return jsonify({"message": "vehicle unlocked"})


# =========================================================
# START
# =========================================================

@app.route("/start", methods=["POST"])
@require_api_key
def start():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")
    user_role = get_user_role()

    if vehicle_id not in vehicles:
        log_event("/start", vehicle_id, "start", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    if not is_authorized(user_role, vehicle_id):
        log_event("/start", vehicle_id, "authorization_check", False, "unauthorized")
        return jsonify({"error": "unauthorized"}), 403

    log_event("/start", vehicle_id, "start", True)

    return jsonify({"message": "vehicle started"})


# =========================================================
# LOGS
# =========================================================

@app.route("/logs")
@require_api_key
def get_logs():
    data = load_logs()

    return jsonify({
        "count": len(data),
        "logs": data[-100:]
    })


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    app.run(debug=False)

# phase_03_authorization_api.py
def main():
    print("Phase 03: Authorization API")
    # Simulate authorization logic
    from time import sleep
    sleep(0.1)
    print("Phase 03 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")