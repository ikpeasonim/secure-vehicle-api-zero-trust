import requests
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

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

# -------------------------
# DATAFRAME CREATION
# -------------------------
df = pd.DataFrame(logs)

df["success_numeric"] = df["success"].astype(int)

features = df[["success_numeric"]]

# -------------------------
# ML MODEL
# -------------------------
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

# -------------------------
# OUTPUT
# -------------------------
print("\n=== ANOMALY DETECTION RESULTS ===")

print(df[["timestamp", "role", "reason", "anomaly"]])

# -------------------------
# VISUALIZATION
# -------------------------
plt.figure(figsize=(12, 6))

feature_column = "success_numeric"

normal = df[df['anomaly'] == 1]
anomalies = df[df['anomaly'] == -1]

plt.scatter(
    normal.index,
    normal[feature_column],
    color='blue',
    label='Normal Activity'
)

plt.scatter(
    anomalies.index,
    anomalies[feature_column],
    color='red',
    label='Anomaly Detected'
)

plt.title("ML Anomaly Detection Results")
plt.xlabel("Event Index")
plt.ylabel("Success (0/1)")
plt.legend()

plt.savefig("screenshots/phase11_ml_detection.png")

print("\nVisualization saved to screenshots/phase11_ml_detection.png")