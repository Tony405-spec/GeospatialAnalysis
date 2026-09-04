# Kenya Cities Data Dictionary

`ke.csv` contains city-level records for Kenya with geographic coordinates and population attributes.

## Fields

| Column | Description | Type / Unit |
| --- | --- | --- |
| `city` | City or populated-place name. | Text |
| `lat` | Latitude in decimal degrees. | Numeric, WGS84 |
| `lng` | Longitude in decimal degrees. | Numeric, WGS84 |
| `country` | Country name for the record. | Text |
| `iso2` | ISO 3166-1 alpha-2 country code. | Text |
| `admin_name` | First-level administrative area associated with the city. | Text |
| `capital` | Capital classification such as `primary` or `admin`; blank means no capital role is recorded. | Text |
| `population` | Estimated city population. | Integer count |
| `population_proper` | Estimated population for the city proper where available. | Integer count |

## Coordinate Notes

Coordinates are latitude/longitude pairs in WGS84 (`EPSG:4326`). They are suitable for mapping points, but distance and area analysis should use an appropriate projected CRS.

## Population Notes

Population values are estimates and may reflect different source years or definitions. Treat them as approximate indicators for exploratory analysis rather than authoritative census totals.
