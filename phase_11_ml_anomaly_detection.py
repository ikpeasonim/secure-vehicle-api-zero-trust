import requests
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import os

BASE_URL = "http://127.0.0.1:5000"
HEADERS = {"X-API-KEY": "dev-key-123"}

# -------------------------
# FUNCTION TO FETCH LOGS
# -------------------------
def fetch_logs():
    try:
        response = requests.get(
            f"{BASE_URL}/logs",
            headers=HEADERS,
            timeout=5
        )

        if response.status_code != 200:
            print(
                f"[ERROR] Log endpoint returned "
                f"{response.status_code}"
            )
            return []

        data = response.json()

        if isinstance(data, dict):
            return data.get("logs", [])

        return []

    except Exception as e:
        print(f"[ERROR] Failed to fetch logs: {e}")
        return []

# -------------------------
# FUNCTION TO RUN ANOMALY DETECTION
# -------------------------
def run_once():
    logs = fetch_logs()
    if not logs:
        print("[INFO] No logs available for anomaly detection")
        return

    df = pd.DataFrame(logs)
    if "success" not in df.columns:
        df["success"] = 1  # fallback if missing
    df["success_numeric"] = df["success"].astype(int)
    features = df[["success_numeric"]]

    # ML MODEL
    model = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = model.fit_predict(features)

    print("\n=== ANOMALY DETECTION RESULTS ===")
    print(df[["timestamp", "role", "reason", "anomaly"]].head(10))  # print top 10 only

    # VISUALIZATION (optional)
    os.makedirs("screenshots", exist_ok=True)
    plt.figure(figsize=(12, 6))
    normal = df[df['anomaly'] == 1]
    anomalies = df[df['anomaly'] == -1]
    plt.scatter(normal.index, normal["success_numeric"], color='blue', label='Normal')
    plt.scatter(anomalies.index, anomalies["success_numeric"], color='red', label='Anomaly')
    plt.title("ML Anomaly Detection Results")
    plt.xlabel("Event Index")
    plt.ylabel("Success (0/1)")
    plt.legend()
    plt.savefig("screenshots/phase11_ml_detection.png")
    plt.close()
    print("[INFO] Visualization saved to screenshots/phase11_ml_detection.png")

# -------------------------
# SAFE MAIN FOR PYTEST
# -------------------------
def main():
    print("Phase 11: ML Anomaly Detection")
    run_once()
    print("Phase 11 completed safely")

# -------------------------
# ONLY RUN LIVE WHEN SCRIPT EXECUTED DIRECTLY
# -------------------------
def run_live():
    import time
    while True:
        run_once()
        time.sleep(5)

if __name__ == "__main__":
    run_live()

# -------------------------
# PYTEST HOOK
# -------------------------
def test_main():
    """Used by SOC pytest runner"""
    main()
    print("safe execution ok")