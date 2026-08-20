---
name: run-experiment
description: Plan, execute, monitor, and record a reproducible project experiment.
---

# Run experiment

1. Read `.agents/context/experimentation.md` and the relevant `E*/README.md`; create a record from `_template` if the experiment is new.
2. State the question, hypothesis, decision rule, primary metric, baseline, and resource limit before execution.
3. Verify code, data, config, environment, and output destination. Do a cheap smoke test when feasible.
4. Run the smallest experiment that can resolve the stated uncertainty. Preserve exact commands and deviations.
5. Store bulky outputs in `storage/runs/<experiment-id>/`; do not commit them.
6. Update the experiment record with observed results, failures, artifact locators, and verification status.
7. If the evidence supports a durable claim, create or update a finding. Update `research/INDEX.md` and `research/NOW.md` as needed.

Never fabricate a run or infer completion from a launched process. Distinguish planned, running, completed, failed, and analyzed states.
