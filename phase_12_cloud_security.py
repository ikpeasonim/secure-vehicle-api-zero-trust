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

# phase_12_cloud_security.py
def main():
    print("Phase 12: Cloud Security")
    from time import sleep
    sleep(0.1)
    print("Phase 12 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")