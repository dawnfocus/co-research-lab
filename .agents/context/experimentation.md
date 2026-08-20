# Experimentation context

Stable rules for experiments in this project. Add domain-specific requirements without duplicating individual experiment plans.

## Minimum reproducibility record

Every completed experiment should identify:

- code revision and working-tree deviations;
- data/source version and split;
- configuration and exact command;
- environment, relevant hardware, and dependencies;
- random seeds or repetition strategy;
- primary metrics and uncertainty where applicable;
- artifact location and enough metadata to detect mix-ups;
- failures and deviations from the planned protocol.

## Lifecycle

`planned -> running -> completed | failed -> analyzed -> finding`

Do not edit a record to make an old run appear consistent with a new protocol. Record the deviation, create a new experiment when comparability changes materially, and preserve negative results.

## Storage convention

Place large run outputs under `storage/runs/E###-short-name/`. Commit only compact, decision-relevant summaries or publishable assets. If external storage is used, record an immutable locator, version, or checksum when feasible.
