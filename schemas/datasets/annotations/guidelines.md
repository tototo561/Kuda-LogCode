# Annotation Guidelines

## Task

Annotators label two things:
1. **Useful log** — a log statement that helps identify the root cause of a fault.
2. **Semantically equivalent code** — generated code that behaves identically to the reference.

## Protocol

- Three annotators with 3+ years of Java/Python experience.
- Each annotator works independently.
- Disagreements resolved by majority vote.
- Inter-rater agreement measured with Cohen's kappa.

## Results

- Cohen's kappa for "useful log": 0.86
- Cohen's kappa for "semantically equivalent code": 0.83

## Examples

### Useful log
```java
logger.error("Failed to connect to DB: {}", e.getMessage());
