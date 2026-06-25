from collections import defaultdict, deque
import random
import time

SEED = 42
random.seed(SEED)


class BurstDetector:
    def __init__(self, window_seconds=10, threshold=3, seed=42):
        random.seed(seed)
        self.window = window_seconds
        self.threshold = threshold
        self.state = {}

    def check(self, event):
        vehicle_id = event.get("vehicle_id")
        action = event.get("action", "UNKNOWN")

        key = (vehicle_id, action)

        if key not in self.state:
            self.state[key] = {"count": 0}

        self.state[key]["count"] += 1

        return (
            event.get("speed", 0) > 120
            or event.get("threat_signal", 0) == 1
            or self.state[key]["count"] >= self.threshold
        )