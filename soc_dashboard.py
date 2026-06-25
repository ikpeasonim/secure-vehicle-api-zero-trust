import json
from collections import defaultdict, Counter
from datetime import datetime, UTC
import matplotlib.pyplot as plt


# =========================================================
# STORAGE (SOC MEMORY LAYER)
# =========================================================
events = []

def test_dashboard_execution():
    import soc_dashboard as d

    # call ANY public function that exists
    for name in dir(d):
        if not name.startswith("_"):
            fn = getattr(d, name)
            if callable(fn):
                try:
                    fn()
                except TypeError:
                    pass

# =========================================================
# INGEST
# =========================================================
def ingest_pipeline_results(result: dict):
    """Receives normalized SOC event stream"""
    events.append(result)


# =========================================================
# METRICS ENGINE
# =========================================================
def compute_metrics():

    risk_timeline = []
    severity_count = Counter()
    event_types = Counter()
    technique_count = Counter()
    identity_risk = defaultdict(int)

    for e in events:

        risk = e.get("risk_score", 0)
        severity = e.get("severity", "LOW")
        event_type = e.get("event_type", "unknown")
        identity = e.get("identity", "unknown")
        technique = e.get("technique", "T0000")

        risk_timeline.append(risk)
        severity_count[severity] += 1
        event_types[event_type] += 1
        identity_risk[identity] += risk

        if isinstance(technique, list):
            for t in technique:
                technique_count[t] += 1
        else:
            technique_count[technique] += 1

    return {
        "risk_timeline": risk_timeline,
        "severity_count": severity_count,
        "event_types": event_types,
        "identity_risk": identity_risk,
        "technique_count": technique_count
    }


# =========================================================
# PLOTS
# =========================================================
def plot_risk_timeline(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data, marker="o")
    plt.title("SOC Risk Timeline")
    plt.grid()
    plt.tight_layout()
    plt.savefig("soc_risk_timeline.png")
    plt.close()


def plot_severity_distribution(data):
    plt.figure(figsize=(6, 4))
    plt.bar(data.keys(), data.values())
    plt.title("Severity Distribution")
    plt.tight_layout()
    plt.savefig("soc_severity_distribution.png")
    plt.close()


def plot_event_types(data):
    plt.figure(figsize=(8, 4))
    plt.bar(data.keys(), data.values())
    plt.title("Event Types")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("soc_event_types.png")
    plt.close('all')


def plot_identity_risk(data):
    plt.figure(figsize=(8, 4))
    plt.bar(data.keys(), data.values())
    plt.title("Identity Risk Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("soc_identity_risk.png")
    plt.close('all')


def plot_mitre(data):
    plt.figure(figsize=(8, 4))
    plt.bar(data.keys(), data.values())
    plt.title("MITRE ATT&CK Coverage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("soc_mitre.png")
    plt.close('all')


# =========================================================
# DASHBOARD EXPORT
# =========================================================
def export_dashboard():

    if not events:
        print("No SOC events available")
        return

    metrics = compute_metrics()

    plot_risk_timeline(metrics["risk_timeline"])
    plot_severity_distribution(metrics["severity_count"])
    plot_event_types(metrics["event_types"])
    plot_identity_risk(metrics["identity_risk"])
    plot_mitre(metrics["technique_count"])

    report = {
        "generated_at": datetime.now(UTC).isoformat(),
        "total_events": len(events),
        "summary": {
            "total_risk": sum(metrics["risk_timeline"]),
            "max_risk": max(metrics["risk_timeline"])
        }
    }

    with open("soc_dashboard_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n📊 SOC DASHBOARD GENERATED")


# =========================================================
# RUNNER
# =========================================================
def run_dashboard(pipeline_results):
    for r in pipeline_results:
        ingest_pipeline_results(r)

    export_dashboard()


# =========================================================
# TEST (FIXED)
# =========================================================
def test_main():
    sample = {
        "risk_score": 50,
        "severity": "HIGH",
        "event_type": "test",
        "identity": "user1",
        "technique": "T1078"
    }

    ingest_pipeline_results(sample)

    assert len(events) > 0
    assert events[-1]["identity"] == "user1"

    print("TEST PASSED")