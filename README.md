# ***`Geospatial Analysis Project`***

**Exploratory and analytical project leveraging geospatial data to extract actionable insights through mapping, spatial statistics, and visualization.**

---

## Project Overview

This project demonstrates end-to-end **geospatial data analysis** using Python and GIS tools. It focuses on **spatial patterns, regional insights, and location-based trends** to support data-driven decision-making.

Key highlights:

- **Data Acquisition & Cleaning:** Imported and preprocessed geospatial datasets in CSV, GeoJSON, and shapefile formats.  
- **Spatial Analysis:** Conducted distance, clustering, and density analysis using **GeoPandas**, **Shapely**, and **PySAL**.  
- **Visualization & Mapping:** Created interactive maps with **Folium**, static plots with **Matplotlib/Seaborn**, and choropleth maps for regional trends.  
- **Insights:** Identified high-density areas, regional hotspots, and spatial correlations to guide business or urban planning decisions.

Dataset fields for `ke.csv` are documented in [`data_dictionary.md`](data_dictionary.md).

---

## Tools & Technologies

- Python (GeoPandas, Folium, Shapely, PySAL, Matplotlib, Seaborn)  
- QGIS / ArcGIS (optional for extra GIS workflows)  
- Jupyter Notebook for workflow documentation  
- GeoJSON / Shapefiles for spatial datasets
- CRS assumptions and projection guidance are documented in [`CRS.md`](CRS.md)

---

## Data Assumptions

`ke.csv` stores Kenya city coordinates as latitude and longitude in WGS84 (`EPSG:4326`). Use these raw coordinates for mapping and point display. Reproject to an appropriate projected CRS before calculating distances, buffers, or areas because degree units are not distance units.

Validate the CSV before analysis:

```bash
python -m pip install -r requirements.txt
python scripts/validate_ke_csv.py
python -m pytest
```

The validator checks required columns and confirms latitude values are within `-90..90` and longitude values are within `-180..180`.

---

## Project Structure

Contribution guidance is available in [`CONTRIBUTING.md`](CONTRIBUTING.md).
