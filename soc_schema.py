from datetime import datetime, timezone
from soc_scoring import normalize_score, compute_severity

def normalize_stage_output(output, stage_name="unknown"):
    """
    Enforces a strict SOC output contract across all pipeline stages.
    """

    if isinstance(output, dict):
        return {
            "risk_score": int(output.get("risk_score", 0) or 0),
            "signals": output.get("signals", []) or [],
            "metadata": output.get("metadata", {}) or {
                "stage": stage_name
            }
        }

    if isinstance(output, list):
        return {
            "risk_score": 0,
            "signals": output,
            "metadata": {"stage": stage_name}
        }

    return {
        "risk_score": 0,
        "signals": [],
        "metadata": {"stage": stage_name}
    }

def build_event(
    *,
    risk_score: int,
    event_type: str,
    identity: str,
    vehicle_id=None,
    technique=None,
    attack=None,
    source_phase="unknown",
    enriched=False,
    metadata=None
):
    score = normalize_score(risk_score)
    severity = compute_severity(score)

    return {
        "risk_score": score,
        "severity": severity,
        "event_type": event_type,
        "technique": technique,
        "attack": attack,
        "identity": identity,
        "vehicle_id": vehicle_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_phase": source_phase,
        "enriched": enriched,
        "metadata": metadata or {}
    }
