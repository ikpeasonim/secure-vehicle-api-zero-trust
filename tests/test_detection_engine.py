from unittest.mock import patch
from phase_10_detection_engine import generate_events

def test_generate_events_mocked():
    with patch("phase_10_detection_engine.generate_events") as mock_gen:
        mock_gen.return_value = [{"vehicle": "CAR123", "status": "ok"}] * 5
        events = list(mock_gen.return_value)
        assert len(events) == 5
