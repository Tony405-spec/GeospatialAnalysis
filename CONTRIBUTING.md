# Contributing

Thank you for improving this geospatial analysis project. Contributions should keep the notebook, data, and documentation reproducible for future users.

## Before You Start

- Open or reference an issue for meaningful changes.
- Keep each pull request focused on one problem.
- Avoid committing generated maps, local exports, Python caches, or notebook checkpoints.
- Do not include private datasets, API keys, tokens, credentials, or location data that cannot be shared publicly.

## Geospatial Review Checklist

For changes that affect spatial analysis:

- Document the coordinate reference system used by any new dataset.
- Confirm latitude and longitude columns are in the expected order.
- Validate coordinate ranges before creating geometries.
- Reproject before distance, area, nearest-neighbor, or buffer calculations.
- Explain projection choices when they affect analytical results.

## Data Changes

Small public reference datasets are acceptable when they are needed to reproduce examples. For new data files, document:

- Source and license.
- Schema and units.
- CRS or coordinate assumptions.
- Any filtering or cleaning steps.

## Testing and Validation

Run the most relevant checks for your change. Examples:

```bash
python -m py_compile <script.py>
python -m pytest
```

If a notebook is changed, restart the kernel and run the affected cells before opening a pull request.
