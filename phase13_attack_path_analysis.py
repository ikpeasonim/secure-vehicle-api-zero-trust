attack_paths = {

    "developer": [
        "API Access",
        "Unauthorized Vehicle Access",
        "Privilege Escalation Attempt"
    ],

    "support": [
        "Vehicle Query",
        "Normal Operations"
    ]
}

print("\n=== ATTACK PATH ANALYSIS ===")

for identity, path in attack_paths.items():

    print(f"\nIdentity: {identity}")

    for step in path:
        print(f" -> {step}")