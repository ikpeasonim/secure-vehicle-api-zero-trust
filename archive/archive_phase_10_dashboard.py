import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

def fetch_logs():

    response = requests.get(
        f"{BASE_URL}/logs",
        headers=HEADERS
    )

    data = response.json()

    if isinstance(data, dict):
        return data.get("logs", [])

    return []

logs = fetch_logs()

if not logs:
    print("No logs found")
    exit()

df = pd.DataFrame(logs)

# -----------------------------
# REQUEST COUNTS
# -----------------------------
endpoint_counts = Counter(df["endpoint"])

plt.figure(figsize=(8, 5))
plt.bar(endpoint_counts.keys(), endpoint_counts.values())

plt.title("SOC Dashboard - Endpoint Activity")
plt.xlabel("Endpoint")
plt.ylabel("Requests")

dashboard_file = (
    f"soc_dashboard_"
    f"{datetime.now().strftime('%H%M%S')}.png"
)

plt.savefig(dashboard_file)

print(f"[SAVED] {dashboard_file}")