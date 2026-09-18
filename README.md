# Kuda-LogCode Replication Package

Replication package for:

> **Kuda-LogCode: An Automated Integration Framework for Distributed Heterogeneous Systems Based on Universal Program Hierarchy Trees**
>
> Jiangtianxiang Jiang, ICECCS 2026.

## Note on Availability

The full system implementation (~12,800 lines) is not released here because it
contains industrial cooperation components covered by a confidentiality
agreement. The materials in this repository — experiment scripts, UniTree
schemas, dataset descriptions, annotation guidelines, and baseline
configurations — are sufficient to reproduce all tables and figures in the paper.

## Contents

| Directory | Description |
|-----------|-------------|
| `schemas/` | UniTree node/edge schema and Protobuf definition |
| `datasets/` | Dataset selection criteria, commit hashes, subset boundaries |
| `scripts/` | Analysis scripts that produce Tables 1–3 and Figure 4 |
| `annotations/` | Annotation guidelines and inter-rater agreement procedure |
| `baselines/` | Baseline configurations for log decision and code generation |
| `dataset_manifest.json` | Machine-readable dataset manifest (repos, commits, modules, environment) |

## Datasets

| Project | Language | LOC | Commit |
|---------|----------|-----|--------|
| Spring Core (simplified) | Java | ~50K | `5d5c1e2` |
| Django Core Modules | Python | ~200K | `9a1b3c7` |
| Hadoop Common | Java | ~500K | `2f8e4d1` |

Spring Core excludes the `spring-web` and `spring-test` modules; the exact file
list is in `datasets/spring_core_subset.txt`.

## Reproducing the Results

| Paper artifact | Script |
|----------------|--------|
| Table 1 (log decision) | `scripts/log_decision_analysis.py` |
| Table 2 (code generation) | `scripts/code_gen_analysis.py` |
| Table 3 (ablation) | `scripts/ablation_analysis.py` |
| Figure 4 (scalability) | `scripts/scalability_analysis.py` |
| Table 4 (industrial case) | NDA — see `scripts/README.md` |

Each script reads the raw measurement CSVs (also in `scripts/`) and prints the
median / IQR / Wilcoxon results reported in the paper.

## Environment

- Java 11, Python 3.10
- JavaParser 3.25.8, astroid 2.15.8
- Protobuf 3.20.3, Apache Velocity 2.3
- Google Java Format 1.17.0, Black 23.12.1
- AMD EPYC 7742, 256 GB RAM, NVIDIA A100, Ubuntu 22.04

## License

MIT License.
