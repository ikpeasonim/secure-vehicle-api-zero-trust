import requests
import pandas as pd
from sklearn.ensemble import IsolationForest

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

response = requests.get(
    f"{BASE_URL}/logs",
    headers=HEADERS
)

data = response.json()

logs = data.get("logs", [])

if not logs:
    print("No logs available")
    exit()

df = pd.DataFrame(logs)

df["success_numeric"] = df["success"].astype(int)

features = df[["success_numeric"]]

model = IsolationForest(
    contamination=0.2,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

print("\n=== ANOMALY DETECTION RESULTS ===")

print(df[
    [
        "timestamp",
        "role",
        "reason",
        "anomaly"
    ]
])