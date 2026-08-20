---
name: prepare-release
description: Audit and export only reviewed public material from open/ into a new public repository.
---

# Prepare public release

Public release is a deliberate boundary crossing. The private working repository must remain private.

1. Identify the release purpose, reviewed findings/reports, intended audience, and exact working revision.
2. Build a manifest of files under `open/`. Reject symlinks or generated references that escape `open/`.
3. Audit every file for secrets, credentials, personal paths, private endpoints, restricted data, non-redistributable assets, license conflicts, anonymization failures, and unreleased claims.
4. Verify public setup and reproduction commands in a clean environment when feasible. Record any unverified requirement explicitly.
5. Make `open/README.md`, licensing, citation, dependency, data-access, and expected-result information self-contained for an external reader.
6. Copy the **contents** of `open/` into a brand-new, empty release directory or repository. Do not copy the private repository's `.git/`, `research/`, `.agents/`, `storage/`, or `_trash/`.
7. Inspect the complete public tree and staged diff before any remote push. Confirm that the destination is the intended new public repository.
8. Create or push the public repository only with explicit human authorization. Record the released revision and URL in a private report or decision log.

Passing automated secret scans is not sufficient evidence that a release is safe; human review of content, claims, rights, and privacy remains required.
