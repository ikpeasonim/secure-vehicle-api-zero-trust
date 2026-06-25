from collections import defaultdict


class VehicleBaseline:
    """
    Tracks normal behavior patterns per vehicle.
    Used for anomaly detection in SOC pipeline.
    """

    def __init__(self):
        # vehicle_id -> action -> count
        self.event_counts = defaultdict(lambda: defaultdict(int))

        # optional metadata for future anomaly scoring
        self.total_events = defaultdict(int)

    def update(self, event: dict):
        vehicle = event.get("vehicle_id")
        action = event.get("action", "UNKNOWN")

        self.event_counts[vehicle][action] += 1
        self.total_events[vehicle] += 1

    def get_baseline(self, vehicle_id: str) -> dict:
        """
        Returns structured baseline instead of raw defaultdict.
        This is important for normalization consistency.
        """

        actions = self.event_counts.get(vehicle_id, {})

        return {
            "vehicle_id": vehicle_id,
            "total_events": self.total_events.get(vehicle_id, 0),
            "actions": dict(actions)
        }