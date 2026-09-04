# Coordinate Reference System Notes

The `ke.csv` dataset stores Kenyan city locations as longitude and latitude columns:

- `lng`: longitude in decimal degrees.
- `lat`: latitude in decimal degrees.
- Assumed source CRS: WGS 84, EPSG:4326.

## Creating Geometry

When converting the CSV to a GeoDataFrame, create point geometry from `lng` first and `lat` second:

```python
kenya = gpd.GeoDataFrame(
    ke_data,
    geometry=gpd.points_from_xy(ke_data["lng"], ke_data["lat"]),
    crs="EPSG:4326",
)
```

Use `crs="EPSG:4326"` rather than the older `{"init": "epsg:4326"}` form.

## Distance and Area Operations

EPSG:4326 coordinates are angular degrees, so distance, area, and buffer operations should not be calculated directly in this CRS.

For display maps, EPSG:4326 is appropriate because Folium and web maps expect latitude/longitude inputs. For metric calculations, project to a suitable projected CRS first.

The notebook currently uses EPSG:3857 for buffering examples. That is convenient for web-map overlays, but Web Mercator distorts distance and area. For analytical work in Kenya, prefer a local projected CRS such as UTM zone 37S or 37N depending on the study area, or document why another projection is acceptable.

## Validation Checklist

- Confirm all `lat` values are between `-90` and `90`.
- Confirm all `lng` values are between `-180` and `180`.
- Confirm all records represent Kenya before applying Kenya-specific projections.
- Reproject before distance, area, nearest-neighbor, or buffering analysis.
