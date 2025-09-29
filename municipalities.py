# municipalities.py

import json
from typing import Dict, List

import pandas as pd


def read_municipalities_excel(file_path: str) -> pd.DataFrame:
    """
    Read Excel file and return filtered DataFrame with required columns.
    Assumes actual headers are in the second row (header=1).
    """
    df = pd.read_excel(file_path, header=1)
    df = df.dropna(subset=["CPRO", "CMUN", "NOMBRE"])
    return df[["CPRO", "CMUN", "NOMBRE"]]


def transform_municipalities(df: pd.DataFrame) -> List[Dict[str, str]]:
    """
    Transform the DataFrame rows into a list of dictionaries
    with formatted municipality data.
    """
    municipalities = []
    for _, row in df.iterrows():
        id_provincia = str(row["CPRO"]).zfill(2)
        id_municipio = str(row["CMUN"]).zfill(3)
        full_id = int(
            id_provincia + id_municipio
        )  # 👈 fuerzo el numero para que quite el cero de la izquierda
        municipalities.append(
            {
                "ID_PROVINCIA": id_provincia,
                "ID_MUNICIPIO": str(full_id),  # 👈 lo devuelvo limpio 
                "NOMBRE_MUNICIPIO": row["NOMBRE"].strip(),
            }
        )
    return municipalities


def export_to_json(data: List[Dict[str, str]], output_file: str):
    """
    Export the list of municipalities to a JSON file.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    excel_file = "diccionario24.xlsx"
    output_json = "municipios.json"

    df_municipalities = read_municipalities_excel(excel_file)
    municipalities = transform_municipalities(df_municipalities)
    export_to_json(municipalities, output_json)
