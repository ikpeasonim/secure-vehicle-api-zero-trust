import json
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load historical SOC metrics
history_file = "soc_metrics_history.jsonl"

records = []
with open(history_file) as f:
    for line in f:
        records.append(json.loads(line))

df = pd.DataFrame(records)

# Convert timestamps
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -----------------------------
# 1️⃣ SOC Health Score Over Time
# -----------------------------
fig_health = px.line(
    df, x='timestamp', y='soc_health_score',
    title="SOC Health Score Over Time",
    markers=True
)
fig_health.write_html("dashboard_health.html")

# -----------------------------
# 2️⃣ Total Events, Alerts, Incidents Over Time
# -----------------------------
fig_events = px.line(
    df, x='timestamp',
    y=['total_events', 'alerts', 'incidents'],
    title="Events / Alerts / Incidents Over Time",
    markers=True
)
fig_events.write_html("dashboard_events.html")

# -----------------------------
# 3️⃣ Top Attack Vectors Over Time
# -----------------------------
# Flatten attack vectors for historical visualization
attack_records = []

for rec in records:
    ts = rec.get("timestamp")

    vectors = rec.get("top_attack_vectors", [])

    # ensure valid structure
    if isinstance(vectors, list) and len(vectors) > 0:
        for item in vectors:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                attack_records.append({
                    "timestamp": ts,
                    "attack_vector": item[0],
                    "count": item[1]
                })

df_attack = pd.DataFrame(attack_records)

if df_attack.empty:
    print("No attack vector data available yet.")
else:
    fig_attack = px.bar(
        df_attack,
        x='timestamp',
        y='count',
        color='attack_vector',
        title="Top Attack Vectors Over Time",
        barmode='group'
    )
    fig_attack.write_html("dashboard_attack_vectors.html")

print("Dashboards generated:")
print(" - dashboard_health.html")
print(" - dashboard_events.html")
print(" - dashboard_attack_vectors.html")
