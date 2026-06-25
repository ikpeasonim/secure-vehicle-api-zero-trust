from flask import Flask, render_template
from flask_socketio import SocketIO
from soc_pipeline import process_pipeline
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


def generate_events():
    sample_events = [
        {"user": "alice", "action": "unlock_vehicle", "vehicle_id": "V999", "auth": True},
        {"user": "bob", "action": "view_vehicle", "vehicle_id": "V123", "auth": True},
        {"user": "eve", "action": "unlock_vehicle", "vehicle_id": "V777", "auth": False},
    ]

    while True:
        for raw in sample_events:

            processed = process_pipeline(raw)

            socketio.emit("soc_event", processed)

            time.sleep(2)


if __name__ == "__main__":
    thread = threading.Thread(target=generate_events)
    thread.daemon = True
    thread.start()

    print("🚨 SOC COMMAND CENTER LIVE")
    socketio.run(app, host="0.0.0.0", port=5000)

def test_main():
    return True
