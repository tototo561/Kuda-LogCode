"""Compute Table 2 statistics from code_gen_raw.csv."""
import pandas as pd
from scipy.stats import wilcoxon

df = pd.read_csv("code_gen_raw.csv")
ours = df[df["method"] == "Kuda-LogCode"]

for m in df["method"].unique():
    sub = df[df["method"] == m]
    med = sub["semantic_equiv"].median()
    iqr = sub["semantic_equiv"].quantile(0.75) - sub["semantic_equiv"].quantile(0.25)
    print(f"{m:25s} median={med:6.2f}  IQR={iqr:5.2f}")

for m in df["method"].unique():
    if m == "Kuda-LogCode":
        continue
    sub = df[df["method"] == m]
    stat, p = wilcoxon(ours["semantic_equiv"], sub["semantic_equiv"])
    print(f"Kuda-LogCode vs {m:25s} p = {p:.4g}")
