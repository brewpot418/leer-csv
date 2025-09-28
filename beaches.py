# beaches.py


import json
from typing import Dict, List

import pandas as pd


def read_beaches() -> List[Dict[str, any]]:
    file_name = "Playas_codigos.csv"

    df = pd.read_csv(file_name, encoding="latin1", sep=";")

    df["ID_PLAYA"] = df["ID_PLAYA"].astype(str).str.zfill(7)

    filtered_df = df[
        ["ID_PLAYA", "NOMBRE_PLAYA", "ID_MUNICIPIO", "LATITUD", "LONGITUD"]
    ]

    beaches_dict = filtered_df.to_dict(orient="records")

    return beaches_dict


def modify_beaches(beaches: List[Dict[str, any]]):
    for beach in beaches:
        latitude = clean_dms(beach["LATITUD"])
        longitude = clean_dms(beach["LONGITUD"])
        beach["LATITUD"] = dms_to_decimal(latitude)
        beach["LONGITUD"] = dms_to_decimal(longitude, is_longitude=True)


def clean_dms(dms_str: str) -> List[str]:
    parts = dms_str.split(" ")
    return [p.replace("º", "").replace("'", "").replace('"', "") for p in parts]


def dms_to_decimal(dms_list: List[str], is_longitude=False) -> float:
    """Convert DMS coordinates (degrees, minutes, seconds) to decimal format."""
    try:
        degrees, minutes, seconds = map(float, dms_list)
        decimal = degrees + minutes / 60 + seconds / 3600
        if is_longitude and decimal > 0:
            decimal = -decimal
        return decimal
    except ValueError:
        raise ValueError(f"Invalid DMS format: {dms_list}")


def export_to_json(beaches):
    with open("playas.json", "w", encoding="utf-8") as f:
        json.dump(beaches, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    beaches = read_beaches()
    modify_beaches(beaches)
    export_to_json(beaches)
