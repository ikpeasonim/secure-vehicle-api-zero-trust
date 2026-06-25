from flask import Flask, render_template, request, redirect, session, jsonify
from flask_socketio import SocketIO

from soc_pipeline import process_pipeline
from event_bus import EventBus
from soc_dashboard import ingest_pipeline_results
from collections import defaultdict
from collections import defaultdict, deque
import time

auth_spike_store = defaultdict(lambda: deque(maxlen=20))

car_state = defaultdict(lambda: {
    "risk_score": 0,
    "severity": "LOW"
})

app = Flask(__name__)
app.secret_key = "dev-secret-key"

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

bus = EventBus()

# =========================
# CAR STATE (HEATMAP DATA)
# =========================
car_state = {
    "CAR100": {"risk": 0, "severity": "LOW"},
    "CAR101": {"risk": 0, "severity": "LOW"},
    "CAR102": {"risk": 0, "severity": "LOW"},
    "CAR103": {"risk": 0, "severity": "LOW"},
    "CAR104": {"risk": 0, "severity": "LOW"},
}

# =========================================================
# AUTH
# =========================================================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form.get("username", "analyst")
        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/")
def root():
    return redirect("/login")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/soc")
def soc_dashboard():
    return render_template("soc_dashboard.html")

@app.route("/heatmap")
def heatmap():
    return jsonify(car_state)

@app.route("/heatmap-ui")
def heatmap_ui():
    return render_template("heatmap.html")

def test_app_boot():
    import app

    if hasattr(app, "app"):
        _ = app.app


# =========================================================
# HEALTH CHECK
# =========================================================
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "events": bus.size()
    })


# =========================================================
# LOG STREAM
# =========================================================
@app.route("/logs")
def logs():
    return jsonify({
        "logs": bus.latest(100)
    })


# =========================================================
# VALIDATION (FIXED)
# =========================================================
def validate_event(event: dict) -> dict:
    return {
        "user": event.get("user", "unknown"),
        "action": event.get("action", "unknown"),
        "vehicle_id": event.get("vehicle_id", "unknown"),
        "auth": bool(event.get("auth", False))
    }


# =========================================================
# INGEST PIPELINE (FIXED)
# =========================================================
@app.route("/ingest", methods=["POST"])
def ingest():
    try:
        raw_event = request.json or {}

        event = validate_event(raw_event)
        result = process_pipeline(event)

        normalized = {
            "user": event["user"],
            "action": event["action"],
            "vehicle_id": event["vehicle_id"],
            "auth": event["auth"],
            "risk_score": result.get("risk_score", 0),
            "severity": result.get("severity", "LOW"),
            "alert": result.get("alert", False),
            "timestamp": result.get("timestamp")
        }


        normalized = {
            "user": event["user"],
            "action": event["action"],
            "vehicle_id": event["vehicle_id"],
            "risk_score": result.get("risk_score", 0),
            "severity": result.get("severity", "LOW"),
            "alert": result.get("alert", False),
            "timestamp": result.get("timestamp")
        }

        # Emit CAR-level dashboard update
        socketio.emit("car_update", {
            "vehicle_id": normalized["vehicle_id"],
            "risk_score": normalized["risk_score"],
            "severity": normalized["severity"],
            "action": normalized["action"],
            "timestamp": normalized["timestamp"]
        })

        car_state[normalized["vehicle_id"]] = {
           "risk_score": normalized["risk_score"],
            "severity": normalized["severity"]
        }

        if normalized["action"] in ["AUTH_SPIKE", "BRUTE_FORCE", "VEHICLE_COMMAND_ACCESS"]:
            auth_spike_store[normalized["vehicle_id"]].append({
             "time": time.time(),
            "action": normalized["action"]
            })

        # Event bus
        bus.publish(normalized)

        # SOC dashboard ingestion
        ingest_pipeline_results(normalized)

        # realtime stream
        socketio.emit("soc_event", normalized)

        return jsonify({
            "status": "ok",
            "event": normalized
        })

    except Exception as e:
        print("❌ INGEST ERROR:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
    spike = compute_spike(normalized["vehicle_id"])

    socketio.emit("auth_spike_wave", {
        "vehicle_id": normalized["vehicle_id"],
        "count": spike["count"],
        "intensity": spike["intensity"],
        "is_spike": spike["is_spike"],
        "timestamp": normalized["timestamp"]
        })
    # =========================
    # UPDATE CAR HEATMAP STATE
    # =========================
    car_id = normalized["vehicle_id"]

    if car_id in car_state:
        car_state[car_id]["risk"] += normalized["risk_score"]
        car_state[car_id]["severity"] = normalized["severity"]


# =========================================================
# SOCKET EVENTS
# =========================================================
@socketio.on("connect")
def on_connect():
    print("🔌 Client connected")


@socketio.on("disconnect")
def on_disconnect():
    print("❌ Client disconnected")


# =========================================================
# START SERVER
# =========================================================
if __name__ == "__main__":
    print("🚀 SOC COMMAND CENTER STARTING...")

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )

def compute_spike(vehicle_id):
    events = auth_spike_store[vehicle_id]
    now = time.time()

    # events in last 10 seconds
    recent = [e for e in events if now - e["time"] <= 10]

    return {
        "count": len(recent),
        "intensity": min(len(recent) * 20, 100),
        "is_spike": len(recent) >= 3
    }

def test_main():
    return True
