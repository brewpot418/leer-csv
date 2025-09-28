# main.py

from beaches import export_to_json as export_beaches_json
from beaches import modify_beaches, read_beaches
from municipalities import (
    export_to_json as export_municipalities_json,
)
from municipalities import (
    read_municipalities_excel,
    transform_municipalities,
)


def main():
    # Procesar municipios
    excel_file = "diccionario24.xlsx"
    output_municipalities_file = "municipios.json"
    df_municipalities = read_municipalities_excel(excel_file)
    municipalities = transform_municipalities(df_municipalities)
    export_municipalities_json(municipalities, output_municipalities_file)
    print(f"Municipios exportados a {output_municipalities_file}")

    # Procesar playas
    beaches = read_beaches()
    modify_beaches(beaches)
    output_beaches_file = "playas.json"
    export_beaches_json(beaches)
    print(f"Playas exportadas a {output_beaches_file}")


if __name__ == "__main__":
    main()
