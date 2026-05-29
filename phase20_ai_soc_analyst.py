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