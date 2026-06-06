import json
import glob
from datetime import datetime
from collections import Counter

EVENT_FILES = glob.glob("soc_events.json*")


def load_events():
    events = []

    for file in EVENT_FILES:
        try:
            with open(file) as f:
                if file.endswith(".jsonl"):
                    for line in f:
                        if line.strip():
                            events.append(json.loads(line))
                else:
                    data = json.load(f)
                    if isinstance(data, list):
                        events.extend(data)
                    else:
                        events.append(data)
        except Exception as e:
            print(f"[WARN] failed loading {file}: {e}")

    return events


# ✅ MUST exist BEFORE usage
events = load_events()

# -----------------------------
# NORMALIZATION (IMPORTANT FIX)
# -----------------------------
for e in events:
    e["timestamp"] = e.get("last_event_time")
    e["type"] = (
        "incident" if e.get("severity") in ["HIGH", "CRITICAL"]
        else "alert" if e.get("severity") == "MEDIUM"
        else "event"
    )
    e["attack_vector"] = (e.get("signals") or ["unknown"])[0]
    e["mitre"] = "T0000"


# -----------------------------
# CORE METRICS
# -----------------------------
total_events = len(events)
alerts = [e for e in events if e.get("type") == "alert"]
incidents = [e for e in events if e.get("type") == "incident"]

attack_vectors = Counter(e.get("attack_vector", "unknown") for e in events)
techniques = Counter(e.get("mitre", "T0000") for e in events)

# -----------------------------
# SOC HEALTH SCORE
# -----------------------------
alert_ratio = len(alerts) / (total_events + 1)
incident_ratio = len(incidents) / (total_events + 1)

soc_health_score = round(
    (1 - alert_ratio * 0.5 - incident_ratio * 0.7) * 100,
    2
)

# -----------------------------
# REPORT
# -----------------------------
report = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "total_events": total_events,
    "alerts": len(alerts),
    "incidents": len(incidents),
    "top_attack_vectors": attack_vectors.most_common(5),
    "top_mitre_techniques": techniques.most_common(5),
    "soc_health_score": soc_health_score,
    "risk_level": (
        "LOW" if soc_health_score > 80 else
        "MEDIUM" if soc_health_score > 50 else
        "HIGH"
    )
}

with open("soc_metrics.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))

with open("soc_metrics_history.jsonl", "a") as f:
    f.write(json.dumps(report) + "\n")

