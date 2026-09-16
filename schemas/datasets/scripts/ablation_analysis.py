"""Compute Table 3 statistics from ablation_raw.csv."""
import pandas as pd

df = pd.read_csv("ablation_raw.csv")
for cfg in df["configuration"].unique():
    sub = df[df["configuration"] == cfg]
    print(f"{cfg:30s} log_acc={sub['log_acc'].median():5.2f}  "
          f"code_acc={sub['code_acc'].median():5.2f}  "
          f"build_time={sub['build_time'].median():6.2f}")
