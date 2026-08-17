from pathlib import Path

from scripts.validate_ke_csv import validate_ke_csv


def test_repository_ke_csv_has_valid_coordinates():
    errors = validate_ke_csv(Path(__file__).resolve().parents[1] / "ke.csv")

    assert errors == []


def test_validator_reports_out_of_range_coordinates(tmp_path):
    csv_path = tmp_path / "bad.csv"
    csv_path.write_text(
        "city,lat,lng,country,iso2,admin_name,capital,population,population_proper\n"
        "Bad City,120,200,Kenya,KE,Test,,1,1\n",
        encoding="utf-8",
    )

    errors = validate_ke_csv(csv_path)

    assert "Bad City: latitude 120.0 is outside -90..90" in errors
    assert "Bad City: longitude 200.0 is outside -180..180" in errors
