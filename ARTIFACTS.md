# Generated Artifacts Policy

This repository keeps source notebooks, scripts, and small documented reference data in version control. Generated files should be recreated from the analysis workflow instead of committed.

## Commit

- Source notebooks and scripts.
- Small reference datasets that are required to reproduce the examples.
- Documentation that explains schemas, assumptions, and workflow steps.

## Do Not Commit

- Python cache directories such as `__pycache__/`.
- Jupyter checkpoint folders.
- Exported maps and plots unless they are intentionally curated documentation assets.
- Derived geospatial layers such as shapefiles, GeoJSON exports, and GeoPackage outputs.
- Local archives or temporary workspace files.

## Recommended Output Locations

Use `outputs/` for generated analysis results and `exports/` for maps or GIS layers. These folders are ignored by Git so experiments can be rerun locally without creating noisy commits.
