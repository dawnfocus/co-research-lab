# Agent work layer

This directory contains provider-neutral, project-local instructions for AI-assisted work.

- `context/` stores stable project conventions that apply across tasks.
- `skills/` stores task-specific procedures loaded on demand.
- `harness/` stores deterministic checks and small automation helpers.

Keep `AGENTS.md` as a short router. Put stable domain context in `context/`, repeatable procedures in a skill, and objectively checkable rules in the harness. Do not use this directory as a second research notebook; evidence belongs in `research/`.

Project-local skills are deliberately explicit Markdown protocols. Agents that support automatic skill discovery may discover them; all other agents can follow the paths routed from `AGENTS.md`.
