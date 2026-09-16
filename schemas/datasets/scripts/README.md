# Scripts

Each script reads a measurement CSV (in this directory) and prints the
statistics reported in the paper.

| Script | Input | Paper artifact |
|--------|-------|----------------|
| `log_decision_analysis.py` | `log_decision_raw.csv` | Table 1 |
| `code_gen_analysis.py` | `code_gen_raw.csv` | Table 2 |
| `ablation_analysis.py` | `ablation_raw.csv` | Table 3 |
| `scalability_analysis.py` | `scalability_raw.csv` | Figure 4 |

The raw CSVs contain the five repeated runs. Each script computes the median,
interquartile range, and pairwise Wilcoxon signed-rank tests at p < 0.01.

Table 4 (industrial case) is not reproducible from these scripts because the
deployment data is covered by a confidentiality agreement; the aggregated
values are reported directly in the paper.
