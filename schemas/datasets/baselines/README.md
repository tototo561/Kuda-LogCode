# Baselines

## Log Decision

| Baseline | Configuration |
|----------|---------------|
| Traditional hard-coded | Manual `logger.info` at method entry/exit |
| AOP hardwiring | AspectJ 1.9.7 pointcut at every public method |
| ELK Centralized | Elasticsearch 8.10, Logstash 8.10, Kibana 8.10 |
| Loki Centralized | Loki 2.9, Grafana 10.1 |

## Code Generation

| Baseline | Version | Notes |
|----------|---------|-------|
| Manual conversion | N/A | Human developer, 50 loc/h average |
| ANTLR4 | 4.13.0 | Java grammar + Python grammar |
| Tree-sitter | 0.20.8 | java + python parsers |
| CodeLlama-7B | Meta release | No fine-tuning |
| CPG-based | Joern 2.0 | AST+CFG+PDG |
| Rascal | 0.34.0 | Java/Python refactoring |
