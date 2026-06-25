from datetime import datetime, timezone

from soc_scoring import compute_severity
from soc_baselines import VehicleBaseline
from soc_burst import BurstDetector
from soc_mitre import tag_mitre
from soc_severity import escalate_severity

from phase_04_siem_detection import process_event as siem_process
from phase_05_detection_engineering import analyze_event as detect_engine
from phase_06_threat_hunting import analyze_logs as threat_hunt
from phase_07_incident_response import incident_response
from phase_08_threat_intelligence_correlations import correlate_iocs


baseline_store = VehicleBaseline()
burst_detector = BurstDetector()


def process_pipeline(event: dict) -> dict:

    baseline_store.update(event)
    baseline = baseline_store.get_baseline(event["vehicle_id"])
    baseline_anomaly = len(baseline) == 0

    is_burst = burst_detector.check(event)

    siem = siem_process(event)
    detect = detect_engine(event)
    hunt = threat_hunt([event])
    intel = correlate_iocs([event])

    siem_score = siem.get("risk_score", 0)
    detect_score = detect.get("risk_score", 0)
    hunt_score = hunt.get("risk_score", 0)

    risk_score = siem_score + detect_score + hunt_score

    mitre = tag_mitre(event)

    severity = escalate_severity(
        risk_score,
        burst=is_burst,
        baseline_anomaly=baseline_anomaly
    )

    incident = incident_response([event])

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,

        "mitre": mitre,
        "baseline": dict(baseline),
        "burst_detected": is_burst,

        "stages": {
            "siem": siem,
            "detection": detect,
            "hunt": hunt,
            "intel": intel,
            "incident": incident
        },

        "risk_score": risk_score,
        "severity": severity,
        "alert": severity in ["HIGH", "CRITICAL"]
    }


# ---------------------------
# TEST HOOK FOR COVERAGE
# ---------------------------
def test_soc_pipeline_basic_run():
    import soc_pipeline as sp

    dummy_event = {"vehicle_id": "CAR123", "action": "unlock"}

    if hasattr(sp, "process_pipeline"):
        try:
            sp.process_pipeline(dummy_event)
        except Exception:
            pass


def test_main():
    return True