# Harness

Deterministic helpers that make workspace conventions testable.

Run the dependency-free structural check from the project root:

```bash
python3 .agents/harness/check_workspace.py
```

Add project-specific checks only when they have a clear pass/fail contract. Research judgment belongs in records and review, not in a brittle validator.
