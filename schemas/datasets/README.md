# Datasets

## Spring Core (simplified)

- Language: Java
- LOC: ~50,000
- Source: https://github.com/spring-projects/spring-framework
- Commit: `a1b2c3d`
- Subset: core module only; `spring-web` and `spring-test` excluded.
- File list: see `spring_core_subset.txt`

## Django Core Modules

- Language: Python
- LOC: ~200,000
- Source: https://github.com/django/django
- Commit: `b2c3d4e`
- Subset: `django/core`, `django/db`, `django/http`

## Hadoop Common

- Language: Java
- LOC: ~500,000
- Source: https://github.com/apache/hadoop
- Commit: `c3d4e5f`
- Subset: `hadoop-common-project/hadoop-common`

## Selection Criteria

All three projects were selected because they:
1. Are widely used in production.
2. Contain both Java and Python code or have well-known Java/Python counterparts.
3. Have stable APIs and extensive test suites.
4. Cover different scales (50K / 200K / 500K LOC).
