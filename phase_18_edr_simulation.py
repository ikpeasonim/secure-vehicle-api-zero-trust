import pandas as pd

telemetry = [
    ["powershell.exe", "EncodedCommand Detected", "HIGH"],
    ["cmd.exe", "Suspicious Process Spawn", "MEDIUM"],
    ["reg.exe", "Registry Persistence Added", "HIGH"],
    ["malware.exe", "Simulated Malware Execution", "CRITICAL"]
]

df = pd.DataFrame(
    telemetry,
    columns=["process", "behavior", "severity"]
)

print("\n=== EDR TELEMETRY ===\n")
print(df)

# phase_18_edr_simulation.py
def main():
    print("Phase 18: EDR Simulation")
    from time import sleep
    sleep(0.1)
    print("Phase 18 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")