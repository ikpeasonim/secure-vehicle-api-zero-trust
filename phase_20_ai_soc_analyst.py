alerts = [
    {
        "alert": "Multiple Failed Logins",
        "severity": "HIGH"
    },
    {
        "alert": "Suspicious PowerShell Activity",
        "severity": "CRITICAL"
    }
]

print("\n=== AI-ASSISTED SOC ANALYST ===\n")

for alert in alerts:

    if alert["severity"] == "CRITICAL":
        recommendation = "Immediate containment recommended"

    elif alert["severity"] == "HIGH":
        recommendation = "Escalate to SOC analyst"

    else:
        recommendation = "Monitor activity"

    print(f"""
Alert: {alert['alert']}
Severity: {alert['severity']}
AI Recommendation: {recommendation}
""")
    
# phase_20_ai_soc_analyst.py
def main():
    print("Phase 20: AI SOC Analyst Simulation")
    from time import sleep
    sleep(0.1)
    print("Phase 20 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")