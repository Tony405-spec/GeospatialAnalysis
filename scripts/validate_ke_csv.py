from __future__ import annotations

import csv
from pathlib import Path

REQUIRED_COLUMNS = {
    "city",
    "lat",
    "lng",
    "country",
    "iso2",
    "admin_name",
    "capital",
    "population",
    "population_proper",
}


def validate_ke_csv(path: str | Path) -> list[str]:
    """Validate required columns and coordinate ranges for the Kenya cities CSV."""
    csv_path = Path(path)
    errors: list[str] = []

    if not csv_path.exists():
        return [f"CSV file not found: {csv_path}"]

    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - fieldnames)
        if missing:
            errors.append(f"Missing required columns: {', '.join(missing)}")
            return errors

        for line_number, row in enumerate(reader, start=2):
            city = row.get("city") or f"line {line_number}"
            try:
                lat = float(row["lat"])
                lng = float(row["lng"])
            except ValueError:
                errors.append(f"{city}: lat and lng must be numeric")
                continue

            if not -90 <= lat <= 90:
                errors.append(f"{city}: latitude {lat} is outside -90..90")
            if not -180 <= lng <= 180:
                errors.append(f"{city}: longitude {lng} is outside -180..180")

    return errors


if __name__ == "__main__":
    failures = validate_ke_csv(Path(__file__).resolve().parents[1] / "ke.csv")
    if failures:
        raise SystemExit("\n".join(failures))
    print("ke.csv validation passed")
