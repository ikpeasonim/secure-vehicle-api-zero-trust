import json
from datetime import datetime

events = [
    {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "RBAC_PRIVILEGE_ESCALATION",
        "user": "service-account-admin",
        "severity": "CRITICAL"
    },
    {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "CONTAINER_EXECUTION",
        "container": "vehicle-api-pod",
        "severity": "MEDIUM"
    },
    {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "KUBE_ADMIN_ACCESS",
        "user": "developer",
        "severity": "HIGH"
    }
]

print("\n=== KUBERNETES SECURITY EVENTS ===\n")

for event in events:
    print(json.dumps(event, indent=4))

# phase_17_kubernetes_security.py
def main():
    print("Phase 17: Kubernetes Security")
    from time import sleep
    sleep(0.1)
    print("Phase 17 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")