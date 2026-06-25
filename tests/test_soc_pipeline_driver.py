from soc_pipeline_driver import run_soc_cycle


def test_driver_minimal_run():
    result = run_soc_cycle("CAR123")
    assert result is not None


def test_driver_force_all_branches():
    result = run_soc_cycle(
        "CAR999",
        force_modes={
            "force_burst": True,
            "force_anomaly": True,
            "force_incident": True,
            "force_intel_miss": True
        }
    )

    assert result["risk_score"] >= 0
    assert "severity" in result
