from datetime import datetime, timezone

from soc_pipeline import process_pipeline


def make_event(**overrides):
    base = {
        "vehicle_id": "CAR_TEST",
        "action": "drive",
        "speed": 50,
        "threat_signal": 0,
        "location": "zone-A",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    base.update(overrides)
    return base


def test_pipeline_normal_flow():
    event = make_event()
    result = process_pipeline(event)

    assert result["event"]["vehicle_id"] == "CAR_TEST"
    assert "stages" in result


def test_pipeline_burst_flow():
    # force burst via repeated calls
    event = make_event(threat_signal=0)

    for _ in range(5):
        process_pipeline(event)

    result = process_pipeline(event)
    assert result["burst_detected"] is True or result["severity"] in ["HIGH", "CRITICAL"]


def test_pipeline_anomaly_flow():
    # missing baseline trigger
    event = make_event(vehicle_id="NEW_CAR_UNKNOWN")

    result = process_pipeline(event)
    assert "baseline" in result


def test_pipeline_high_speed_risk_flow():
    event = make_event(speed=200, threat_signal=1)

    result = process_pipeline(event)

    assert result["risk_score"] >= 0
    assert result["severity"] in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]


def test_pipeline_intel_and_incident_flow():
    event = make_event(speed=120, threat_signal=1)

    result = process_pipeline(event)

    assert "stages" in result
    assert "intel" in result["stages"]
    assert "incident" in result["stages"]
