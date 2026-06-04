attack_simulations = [
    {
        "technique": "T1059",
        "name": "Command and Scripting Interpreter",
        "detection": "SUCCESS"
    },
    {
        "technique": "T1078",
        "name": "Valid Accounts",
        "detection": "SUCCESS"
    },
    {
        "technique": "T1021",
        "name": "Remote Services",
        "detection": "PARTIAL"
    }
]

print("\n=== PURPLE TEAM AUTOMATION ===\n")

for attack in attack_simulations:
    print(
        f"{attack['technique']} | "
        f"{attack['name']} | "
        f"Detection: {attack['detection']}"
    )