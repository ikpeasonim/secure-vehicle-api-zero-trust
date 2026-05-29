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