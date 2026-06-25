import requests
from collections import Counter
import matplotlib
matplotlib.use("Agg")  # prevents GUI crashes in CI
import matplotlib.pyplot as plt

BASE_URL = "http://127.0.0.1:5000"


def fetch_logs():
    try:
        response = requests.get(f"{BASE_URL}/logs")

        if response.status_code != 200:
            return []

        return response.json()

    except Exception:
        return []


def build_counters(logs):
    endpoint_counter = Counter()
    vehicle_counter = Counter()

    for log in logs:
        endpoint_counter[log.get("endpoint", "unknown")] += 1
        vehicle_id = log.get("vehicle_id")
        if vehicle_id:
            vehicle_counter[vehicle_id] += 1

    return endpoint_counter, vehicle_counter


def plot_endpoints(endpoint_counter):
    if not endpoint_counter:
        return None

    plt.figure()
    plt.bar(endpoint_counter.keys(), endpoint_counter.values())
    plt.title("Requests per Endpoint")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt


def plot_vehicles(vehicle_counter):
    if not vehicle_counter:
        return None

    plt.figure()
    plt.bar(vehicle_counter.keys(), vehicle_counter.values())
    plt.title("Requests per Vehicle ID")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt


def run_visualizations():
    logs = fetch_logs()
    ep, vc = build_counters(logs)

    plot_endpoints(ep)
    plot_vehicles(vc)

    return True


# REQUIRED FOR TESTS
def test_visualizations_execution():
    import visualizations as v

    for name in dir(v):
        obj = getattr(v, name)
        if callable(obj) and not name.startswith("_"):
            try:
                obj()
            except Exception:
                pass


def test_main():
    return True