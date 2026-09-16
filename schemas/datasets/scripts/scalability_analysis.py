"""Reproduce Figure 4 (scalability) from scalability_raw.csv."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scalability_raw.csv")
fig, ax = plt.subplots()
for metric, style in [("log_decision", "s-"), ("code_gen", "^-")]:
    ax.plot(df["n_subsystems"], df[metric], style, label=metric)
ax.set_xlabel("Number of Integrated Sub-systems")
ax.set_ylabel("Time (normalized)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
fig.savefig("scalability.png", dpi=300)
print("Saved scalability.png")
