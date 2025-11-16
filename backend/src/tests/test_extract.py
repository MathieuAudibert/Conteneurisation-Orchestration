from pathlib import Path
import sys

import pytest
import pandas as pd

from backend.src.etl.extract import extract

def test_extract(tmp_path):
    # crée un fichier csv temporaire
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(
        "brand,model,transmission,make_year,reg_year,fuel_type,engine_capacity(CC),km_driven,ownership,price,overall_cost,has_insurance,spare_key,reg_number,title\n"
        "Mahindra,Thar LX D 4WD MT CONVERTIBLE,Manual,2020,01-01-2021,Diesel,2184,11003,1st owner,1231000,23431,TRUE,No,HR26,2020 Mahindra Thar LX D 4WD MT CONVERTIBLE\n"
        "Hyundai,Verna 1.6 VTVT SX,Manual,2018,01-07-2018,Petrol,1591,66936,1st owner,786000,15359,TRUE,No,DL7C,2018 Hyundai Verna 1.6 VTVT SX"
    )

    cars = extract(str(test_file))

    # vérifie que les données sont correctement extraites
    assert isinstance(cars, pd.DataFrame)
    assert len(cars) == 2  # vérifie qu'il y a 2 lignes
    assert list(cars.columns) == [
        "brand",
        "model",
        "transmission",
        "make_year",
        "reg_year",
        "fuel_type",
        "engine_capacity(CC)",
        "km_driven",
        "ownership",
        "price",
        "overall_cost",
        "has_insurance",
        "spare_key",
        "reg_number",
        "title",
    ]