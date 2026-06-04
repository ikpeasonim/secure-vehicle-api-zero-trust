import matplotlib.pyplot as plt

techniques = [
    "T1078",
    "T1190",
    "T1210",
    "T1021"
]

scores = [8, 6, 9, 4]

plt.figure(figsize=(8, 5))

plt.bar(techniques, scores)

plt.title("MITRE ATT&CK Heatmap")
plt.xlabel("Technique")
plt.ylabel("Detection Coverage")

plt.savefig("attack_heatmap.png")

print("[SAVED] attack_heatmap.png")