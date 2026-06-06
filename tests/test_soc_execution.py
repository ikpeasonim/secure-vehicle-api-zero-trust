import importlib
import pytest

PHASES = [
    "phase_01_vulnerable_api",
    "phase_02_authenticated_api",
    "phase_03_authorization_api",
    "phase_04_siem_detection",
    "phase_05_detection_engineering",
    "phase_06_threat_hunting",
    "phase_07_incident_response",
    "phase_08_threat_intelligence_correlations",
    "phase_09_soar_automation",
    "phase_10_detection_engine",
    "phase_11_ml_anomaly_detection",
    "phase_12_cloud_security",
    "phase_13_attack_path_analysis",
    "phase_14_attack_heatmap",
    "phase_15_executive_reporting",
    "phase_16_identity_federation",
    "phase_17_kubernetes_security",
    "phase_18_edr_simulation",
    "phase_19_purple_team",
    "phase_20_ai_soc_analyst",
]

@pytest.mark.parametrize("phase", PHASES)
def test_soc_phases_execute_fast(phase):
    """
    Import each phase module and call the safe test_main() function only.
    This avoids starting servers or infinite loops.
    """
    try:
        module = importlib.import_module(phase)
    except Exception as e:
        pytest.fail(f"Failed to import {phase}: {e}")

    if hasattr(module, "test_main"):
        try:
            module.test_main()  # ✅ safe call
        except Exception as e:
            pytest.fail(f"{phase}.test_main() raised an exception: {e}")
    else:
        pytest.fail(f"{phase} has no test_main() function defined.")
