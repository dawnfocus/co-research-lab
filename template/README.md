# Project name

> Replace this line with the project's one-sentence research objective.

This is a private, GitHub-first workspace for human–AI collaborative research. It keeps implementation, evidence, decisions, and publication material connected without loading the entire repository into every AI session.

## Start here

1. Fill in [`.agents/context/project.md`](.agents/context/project.md).
2. Set the current objective in [`research/NOW.md`](research/NOW.md).
3. Add durable sources and records to [`research/INDEX.md`](research/INDEX.md).
4. Run `python3 .agents/harness/check_workspace.py`.

AI agents must follow [`AGENTS.md`](AGENTS.md), including its progressive read order and write-back protocol.

## Workspace map

```text
open/       Publishable code, configs, tests, scripts, and assets
research/   Private, Git-tracked research memory and evidence records
.agents/    Project context, task skills, and lightweight harnesses
storage/    Data, models, external artifacts, and runs; ignored by Git
_trash/     Disposable files; ignored by Git
```

## Research loop

```text
question -> experiment -> finding -> report/paper claim -> open release
                |             ^
                v             |
           storage/runs ------+
```

- An experiment records what was attempted and how to reproduce it.
- A finding states what the evidence supports, including limitations and counterevidence.
- A report assembles findings for a decision, milestone, submission, or release.
- `open/` contains only reviewed, publishable material.

## Privacy boundary

Keep this working repository private. `research/` is intentionally versioned but is never a public-release source. Publish `open/` to a separate public repository or artifact; do not make this repository public after private material has entered its Git history.
