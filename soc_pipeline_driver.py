import random
import numpy as np
from datetime import datetime, timezone

# -----------------------------
# DETERMINISM (GLOBAL SEED)
# -----------------------------
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# -----------------------------
# IMPORTS
# -----------------------------
from soc_baselines import VehicleBaseline
from soc_burst import BurstDetector

from phase_07_incident_response import incident_response
from phase_08_threat_intelligence_correlations import correlate_iocs
from phase_05_detection_engineering import analyze_event as detect_engine
from phase_06_threat_hunting import analyze_logs as threat_hunt
from phase_04_siem_detection import process_event as siem_process

import soc_dashboard
import verify_security_pipeline
import visualizations

from soc_mitre import tag_mitre
from soc_severity import escalate_severity


# -----------------------------
# GLOBAL STATE
# -----------------------------
baseline_store = VehicleBaseline()
burst_detector = BurstDetector(seed=SEED)


# -----------------------------
# STRICT SOC CONTRACT ENFORCER
# -----------------------------
def enforce_contract(output):
    """
    Forces ALL modules into stable SOC schema:
    {
        "risk_score": int,
        "signals": list,
        "metadata": dict
    }
    """

    if output is None:
        return {"risk_score": 0, "signals": [], "metadata": {}}

    if isinstance(output, list):
        return {"risk_score": 0, "signals": output, "metadata": {}}

    if isinstance(output, dict):
        return {
            "risk_score": int(output.get("risk_score", 0) or 0),
            "signals": output.get("signals", []) or [],
            "metadata": output.get("metadata", {})
        }

    return {"risk_score": 0, "signals": [], "metadata": {}}


# -----------------------------
# EVENT BUILDER
# -----------------------------
def build_event(vehicle_id, force_modes=None):
    force_modes = force_modes or {}

    return {
        "vehicle_id": vehicle_id,
        "action": force_modes.get("action", "DRIVE"),
        "speed": force_modes.get("speed", 50),
        "threat_signal": force_modes.get("threat_signal", 0),
        "location": "zone-A",
        "timestamp": force_modes.get(
            "timestamp",
            datetime.now(timezone.utc).isoformat()
        )
    }


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def run_soc_cycle(vehicle_id, force_modes=None):
    force_modes = force_modes or {}

    event = build_event(vehicle_id, force_modes)

    # -----------------------------
    # BASELINE
    # -----------------------------
    baseline_store.update(event)
    baseline = baseline_store.get_baseline(vehicle_id)
    baseline_anomaly = len(baseline) == 0 or force_modes.get("force_anomaly", False)

    # -----------------------------
    # PIPELINE STAGES (FORCED CONTRACT)
    # -----------------------------
    siem = enforce_contract(siem_process(event))
    detect = enforce_contract(detect_engine(event))
    hunt = enforce_contract(threat_hunt([event]))
    intel = enforce_contract(correlate_iocs([event]))

    # -----------------------------
    # BURST DETECTION (DETERMINISTIC)
    # -----------------------------
    burst = burst_detector.check(event) or force_modes.get("force_burst", False)

    if force_modes.get("force_intel_miss"):
        intel = {"risk_score": 0, "signals": [], "metadata": {"ioc_match": False}}

    # -----------------------------
    # RISK AGGREGATION
    # -----------------------------
    risk_score = (
        siem["risk_score"]
        + detect["risk_score"]
        + hunt["risk_score"]
        + intel["risk_score"]
    )

    # -----------------------------
    # MITRE TAGGING
    # -----------------------------
    mitre = tag_mitre(event)

    # -----------------------------
    # SEVERITY ENGINE
    # -----------------------------
    severity = escalate_severity(
        risk_score,
        burst=burst,
        baseline_anomaly=baseline_anomaly
    )

    # -----------------------------
    # INCIDENT RESPONSE
    # -----------------------------
    incident = enforce_contract(incident_response([event]))

    if force_modes.get("force_incident"):
        incident["metadata"]["forced"] = True

    # -----------------------------
    # SAFE SIDE EFFECTS
    # -----------------------------
    try:
        visualizations.run_all()
    except Exception:
        pass

    try:
        soc_dashboard.generate_dashboard([event])
    except Exception:
        pass

    try:
        verify_security_pipeline.run_pipeline()
    except Exception:
        pass

    # -----------------------------
    # FINAL OUTPUT (CLEAN CONTRACT)
    # -----------------------------
    return {
        "timestamp": event["timestamp"],
        "event": event,

        "baseline": dict(baseline),
        "baseline_anomaly": baseline_anomaly,

        "burst_detected": burst,

        "mitre": mitre,
        "risk_score": risk_score,
        "severity": severity,

        "intel": intel,
        "incident": incident,

        "alert": severity in ["HIGH", "CRITICAL"]
    }