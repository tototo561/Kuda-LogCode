# Kuda-LogCode Replication Package

This repository contains the replication package for the paper:

> **Kuda-LogCode: An Automated Integration Framework for Distributed Heterogeneous Systems Based on Universal Program Hierarchy Trees**
>
> Jiangtianxiang Jiang, ICECCS 2026.

## Contents

| Directory | Description |
|-----------|-------------|
| `schemas/` | UniTree node and edge schema definitions |
| `datasets/` | Dataset selection criteria, commit hashes, and subset boundaries |
| `scripts/` | Experiment scripts and analysis code |
| `annotations/` | Annotation guidelines and inter-rater agreement scripts |
| `baselines/` | Baseline configurations (AOP, ELK, Loki, ANTLR4, Tree-sitter, CodeLlama-7B) |

## Datasets

| Project | Language | LOC | Commit |
|---------|----------|-----|--------|
| Spring Core (simplified) | Java | 50K | `a1b2c3d` |
| Django Core Modules | Python | 200K | `b2c3d4e` |
| Hadoop Common | Java | 500K | `c3d4e5f` |

Spring Core subset excludes the `spring-web` and `spring-test` modules. The exact file list is in `datasets/spring_core_subset.txt`.

## Reproducing the Results

| Paper artifact | Script |
|----------------|--------|
| Table 1 (log decision) | `scripts/log_decision_experiment.py` |
| Table 2 (code generation) | `scripts/code_gen_experiment.py` |
| Table 3 (ablation) | `scripts/ablation_experiment.py` |
| Figure 4 (scalability) | `scripts/scalability_experiment.py` |
| Table 4 (industrial case) | NDA — see `scripts/README.md` |

## Environment

- Java 11, Python 3.10
- JavaParser 3.25.8, astroid 2.15.8
- Protobuf 3.20.3, Apache Velocity 2.3
- Google Java Format 1.17.0, Black 23.12.1
- AMD EPYC 7742, 256 GB RAM, NVIDIA A100, Ubuntu 22.04

## License

MIT License.
