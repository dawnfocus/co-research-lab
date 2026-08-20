# Storage

Local or externally synchronized artifacts that should not enter Git:

- `data/` — raw or processed datasets
- `models/` — checkpoints and weights
- `runs/` — experiment outputs, preferably grouped by experiment ID
- `external/` — external repositories or downloaded resources
- `cache/` — reproducible caches

Important artifacts must be addressable from an experiment record using a stable locator, version, checksum, or manifest. This README and the directory skeleton are tracked; contents are ignored.
