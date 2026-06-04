import json
from datetime import datetime

cloud_events = [
    {
        "event": "IAM_POLICY_CHANGE",
        "user": "developer",
        "severity": "HIGH"
    },
    {
        "event": "ROOT_LOGIN",
        "user": "admin",
        "severity": "CRITICAL"
    }
]

print("\n=== CLOUD SECURITY EVENTS ===")

for event in cloud_events:

    enriched = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event["event"],
        "user": event["user"],
        "severity": event["severity"]
    }

    print(json.dumps(enriched, indent=4))