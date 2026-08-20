---
name: analyze-experiment
description: Analyze experiment evidence and turn supported conclusions into scoped findings.
---

# Analyze experiment

1. Read the target experiment record and its linked config, results, and artifact manifest. Confirm that the run actually completed.
2. Check comparability: code/data versions, splits, baselines, seeds, sample counts, exclusions, and metric definitions.
3. Reproduce material calculations when feasible. Report uncertainty and missing evidence; do not over-interpret point estimates.
4. Separate observations from explanations. Actively test plausible confounds and contradictory evidence.
5. Update the experiment interpretation, then create or revise a single-claim `F*/README.md` when warranted.
6. Link every finding to evidence, scope its generality, and update `research/INDEX.md`, `research/NOW.md`, and relevant paper claims.

If inputs are incomplete or incomparable, report the smallest concrete rerun or validation needed instead of forcing a conclusion.
