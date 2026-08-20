# Project working agreement

This repository is a human–AI research workspace. Optimize for traceable evidence, reproducibility, and future reporting—not only the immediate task.

## Default read order

At the start of a task, read only:

1. `AGENTS.md`
2. `research/NOW.md`
3. `research/INDEX.md`
4. `.agents/context/project.md`

Do not scan the whole repository by default. Expand context only through the routing below or when a concrete dependency requires it.

## Task routing

- Experiment design or execution: read `.agents/context/experimentation.md`, then `.agents/skills/run-experiment/SKILL.md`, then only the relevant code/config/experiment record.
- Experiment analysis: read the relevant `research/experiments/E*/` and `research/findings/F*/`, then `.agents/skills/analyze-experiment/SKILL.md`.
- Literature work: read `research/literature/INDEX.md`, then `.agents/skills/review-literature/SKILL.md`.
- Implementation: read only the relevant parts of `open/`, plus linked experiment or finding records.
- Reporting or paper work: read the relevant `research/reports/R*/`, `research/findings/F*/`, and `research/paper/` files.
- Public release: read `.agents/skills/prepare-release/SKILL.md`; release only a reviewed export of `open/` to a new repository.

## Evidence rules

- Never invent citations, measurements, runs, files, requirements, or conclusions.
- Mark statements as verified fact, interpretation, assumption, or open question when the distinction matters.
- Every material result must point to an experiment, finding, source, code revision, or artifact locator.
- Raw outputs in `storage/` are not durable knowledge. Distill decision-relevant evidence into `research/`.
- A failed or contradictory result is evidence; preserve it rather than silently overwriting it.

## Write-back protocol

Before declaring substantive work complete:

1. Keep `README.md` (default Chinese) and `README.en.md` semantically aligned when project-level documentation changes.
2. Put publishable implementation in `open/` and verify it.
3. Record experimental work in `research/experiments/E*/README.md`.
4. Promote supported conclusions to `research/findings/F*/README.md`; do not bury conclusions only in logs.
5. Update `research/INDEX.md` when a durable record is added or its status changes.
6. Update `research/NOW.md` when priorities, blockers, or next actions change.
7. Append major decisions or course corrections to `research/LOG.md`.
8. State what was verified and what remains unverified.

## Privacy and publication

- Treat everything outside `open/` as non-public by default.
- Do not copy secrets, restricted data, private citations/notes, or unreleased claims into `open/`.
- Keep large data, models, external checkouts, caches, and run artifacts under `storage/`; Git ignores them by default.
- Public release is an explicit review step, never an automatic consequence of completing a task.
