"""Compute Table 1 statistics from log_decision_raw.csv."""
import pandas as pd
from scipy.stats import wilcoxon

df = pd.read_csv("log_decision_raw.csv")
methods = df["method"].unique()
ours = df[df["method"] == "Kuda-LogCode"]

for m in methods:
    sub = df[df["method"] == m]
    med = sub["redundancy"].median()
    iqr = sub["redundancy"].quantile(0.75) - sub["redundancy"].quantile(0.25)
    print(f"{m:25s} median={med:6.2f}  IQR={iqr:5.2f}")

# Wilcoxon between ours and each baseline
for m in methods:
    if m == "Kuda-LogCode":
        continue
    sub = df[df["method"] == m]
    stat, p = wilcoxon(ours["redundancy"], sub["redundancy"])
    print(f"Kuda-LogCode vs {m:25s} p = {p:.4g}")
