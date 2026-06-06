# phase_10_detection_engine.py
from flask import Flask, render_template_string, Response, jsonify
import time, threading, random
from datetime import datetime, timezone

app = Flask(__name__)

# Vehicle simulation
VEHICLES = ["CAR100", "CAR101", "CAR102", "CAR103", "CAR104"]
SIGNALS = ["AUTH_SPIKE", "DEVICE_CHANGE", "VEHICLE_COMMAND_ACCESS",
           "PRIVILEGE_ABUSE", "BASELINE_DEVIATION", "BRUTE_FORCE"]

# Risk thresholds
def get_status_action(risk):
    if risk < 30:
        return "LOW", "MONITOR"
    elif risk < 70:
        return "MEDIUM", "MONITOR"
    elif risk < 130:
        return "HIGH", "SOC INVESTIGATION"
    else:
        return "CRITICAL", "IMMEDIATE LOCKDOWN"

# Shared events store
EVENTS = []

def generate_events():
    while True:
        vehicle = random.choice(VEHICLES)
        signal = random.choice(SIGNALS)
        risk = random.randint(5, 350)
        status, action = get_status_action(risk)
        timestamp = datetime.now(timezone.utc).isoformat()
        event = {
            "timestamp": timestamp,
            "vehicle": vehicle,
            "signal": signal,
            "risk": risk,
            "status": status,
            "action": action
        }
        EVENTS.append(event)
        # Keep last 50 events
        if len(EVENTS) > 50:
            EVENTS.pop(0)
        print(f"[LIVE] {vehicle} | {signal} | RISK={risk} | {status} | {action}")
        time.sleep(1.5)  # event every 1.5 seconds

@app.route("/api/events")
def stream():
    def event_stream():
        last_idx = 0
        while True:
            if len(EVENTS) > last_idx:
                for e in EVENTS[last_idx:]:
                    data = f"{e['timestamp']}|{e['vehicle']}|{e['signal']}|{e['risk']}|{e['status']}|{e['action']}"
                    yield f"data: {data}\n\n"
                last_idx = len(EVENTS)
            time.sleep(0.5)
    return Response(event_stream(), mimetype="text/event-stream")

# Dark UI dashboard
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SOC Command Center - Phase 10</title>
<style>
body { background-color: #121212; color: #eee; font-family: monospace; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 8px; text-align: left; border-bottom: 1px solid #444; }
th { background-color: #222; }
tr:nth-child(even) { background-color: #1e1e1e; }
.low { color: #00ff00; }
.medium { color: #ffff00; }
.high { color: #ff8800; }
.critical { color: #ff4444; font-weight: bold; }
</style>
</head>
<body>
<h2>SOC Command Center - Phase 10</h2>
<table id="events">
<thead>
<tr>
<th>Timestamp</th>
<th>Vehicle</th>
<th>Signal</th>
<th>Risk</th>
<th>Status</th>
<th>Action</th>
</tr>
</thead>
<tbody></tbody>
</table>
<script>
const evtSource = new EventSource("/api/events");
const tbody = document.querySelector("#events tbody");
evtSource.onmessage = function(event) {
    const [timestamp, vehicle, signal, risk, status, action] = event.data.split("|");
    const tr = document.createElement("tr");
    tr.innerHTML = `
        <td>${timestamp}</td>
        <td>${vehicle}</td>
        <td>${signal}</td>
        <td>${risk}</td>
        <td class="${status.toLowerCase()}">${status}</td>
        <td>${action}</td>
    `;
    if(tbody.children.length > 50) tbody.removeChild(tbody.lastChild);
};
</script>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(DASHBOARD_HTML)

if __name__ == "__main__":
    print("=== SOC COMMAND CENTER ONLINE ===")
    threading.Thread(target=generate_events, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)

# phase_10_detection_engine.py
def main():
    print("Phase 10: Detection Engine")
    from time import sleep
    sleep(0.1)
    print("Phase 10 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")