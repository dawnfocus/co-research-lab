#!/usr/bin/env python3
"""Validate the minimal co-research workspace contract."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "README.en.md",
    "AGENTS.md",
    ".gitignore",
    "assets/research-workflow-hero.png",
    "assets/workspace-flow.svg",
    "open/README.md",
    "research/INDEX.md",
    "research/NOW.md",
    "research/LOG.md",
    "research/experiments/_template/README.md",
    "research/findings/_template/README.md",
    "research/reports/_template/README.md",
    "research/literature/INDEX.md",
    "research/paper/claims.md",
    "research/paper/story.md",
    ".agents/context/project.md",
    ".agents/context/experimentation.md",
    ".agents/skills/run-experiment/SKILL.md",
    ".agents/skills/analyze-experiment/SKILL.md",
    ".agents/skills/review-literature/SKILL.md",
    ".agents/skills/prepare-release/SKILL.md",
)

REQUIRED_DIRS = (
    "open/src",
    "open/configs",
    "open/scripts",
    "open/tests",
    "open/assets",
    "storage/data",
    "storage/models",
    "storage/runs",
    "storage/external",
    "storage/cache",
    "_trash",
)

IGNORED_PROBES = (
    "storage/data/probe.bin",
    "storage/models/probe.bin",
    "storage/runs/probe.bin",
    "storage/external/probe.bin",
    "storage/cache/probe.bin",
    "_trash/probe.bin",
)


def git_ignores(root: Path, relative_path: str) -> bool | None:
    result = subprocess.run(
        ["git", "check-ignore", "--quiet", relative_path],
        cwd=root,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    return None


def main() -> int:
    default_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    args = parser.parse_args()
    root = args.root.resolve()

    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            errors.append(f"missing file: {relative_path}")
    for relative_path in REQUIRED_DIRS:
        if not (root / relative_path).is_dir():
            errors.append(f"missing directory: {relative_path}")

    agents = root / "AGENTS.md"
    if agents.is_file():
        agents_text = agents.read_text(encoding="utf-8")
        for expected in ("research/NOW.md", "research/INDEX.md", ".agents/context/project.md"):
            if expected not in agents_text:
                errors.append(f"AGENTS.md does not route to: {expected}")

    readme_pairs = (
        ("README.md", "README.en.md"),
        ("README.en.md", "README.md"),
    )
    for source, target in readme_pairs:
        source_path = root / source
        if source_path.is_file() and target not in source_path.read_text(encoding="utf-8"):
            errors.append(f"{source} does not link to: {target}")

    if (root / "template").exists():
        errors.append("legacy template/ wrapper must not exist")

    ignore_results = {probe: git_ignores(root, probe) for probe in IGNORED_PROBES}
    if any(result is not None for result in ignore_results.values()):
        for probe, ignored in ignore_results.items():
            if ignored is False:
                errors.append(f"path is not ignored by Git: {probe}")

    if errors:
        print("Workspace check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Workspace check passed: {root}")
    if all(result is None for result in ignore_results.values()):
        print("Note: Git ignore probes were skipped because the root is not inside a Git repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
