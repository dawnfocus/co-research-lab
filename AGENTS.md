# Framework maintainer instructions

This repository maintains a deployable research-workspace template. It is not itself a research project.

## Read order

1. `README.md`
2. `template/README.md`
3. `template/AGENTS.md`
4. Only the template component relevant to the requested change

Do not treat `template/AGENTS.md` as instructions for maintaining this framework. It is an artifact shipped to generated projects.

## Change rules

- Keep the template domain- and toolchain-neutral.
- Prefer Markdown and Python standard-library checks over new dependencies.
- Preserve progressive disclosure: the deployed `AGENTS.md` must stay short and route to deeper context or skills.
- Keep `research/` tracked and private; keep `storage/` and `_trash/` ignored by default.
- Never add secrets, real research data, model weights, or generated run outputs to the template.
- Use `_template/` for record examples so examples cannot be mistaken for real IDs.
- A new convention must have one canonical home. Link to it instead of repeating it across files.

## Verification

After changing the deployed skeleton, run:

```bash
python3 template/.agents/harness/check_workspace.py --root template
```

If deployment behavior changes, also create a temporary project with `scripts/create-project.sh` and run the copied harness there.
