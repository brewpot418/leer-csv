import csv
from typing import Dict, List, Set


def obtener_csv() -> List[Dict[str, str]]:
    with open("Playas_codigos.csv", mode="r", newline="", encoding="latin1") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')

        playas = list()
        next(reader)  # Ignorar la primera fila (cabecera)

        for row in reader:
            if len(row) != 8:  # Verifica que la fila tenga 8 columnas
                print(f"Este row no ha sido filtrado: {row}")
                continue

            # Procesar latitud
            lista_latitud_reparadora = row[6].split(" ")
            lista_latitud = (
                lista_latitud_reparadora[0].replace("º", ""),
                lista_latitud_reparadora[1].replace("'", ""),
                lista_latitud_reparadora[2].replace('"', ""),
            )

            # Procesar longitud
            lista_longitud_reparadora = row[7].split(" ")
            lista_longitud = (
                lista_longitud_reparadora[0].replace("º", ""),
                lista_longitud_reparadora[1].replace("'", ""),
                lista_longitud_reparadora[2].replace('"', ""),
            )

            # Crear el diccionario para la playa
            diccionario = {
                "ID_PLAYA": row[0],
                "NOMBRE_PLAYA": row[1],
                "ID_PROVINCIA": row[2],
                "NOMBRE_PROVINCIA": row[3],
                "ID_MUNICIPIO": row[4],
                "NOMBRE_MUNICIPIO": row[5],
                "LATITUD": dms_to_decimal(lista_latitud),
                "LONGITUD": dms_to_decimal(lista_longitud, is_longitude=True),
            }
            playas.append(diccionario)

    return playas


def dms_to_decimal(dms_list: List[str], is_longitude=False) -> float:
    """Convierte coordenadas DMS (grados, minutos, segundos) a formato decimal."""
    try:
        # Se separan grados, minutos y segundos de la lista
        degrees, minutes, seconds = [float(i) for i in dms_list]

        # Se realiza la conversión a decimal
        decimal = degrees + minutes / 60 + seconds / 3600

        # Si es longitud (longitudes oeste son negativas), corregimos
        if is_longitude and decimal > 0:
            decimal = -decimal

        return decimal
    except ValueError:
        raise ValueError(f"Formato DMS inválido: {dms_list}")


def obtener_provincias(playas: List[Dict[str, str]]) -> Set[str]:
    """Obtiene un conjunto de provincias únicas de las playas."""
    provincias = set()
    for playa in playas:
        provincias.add(playa["NOMBRE_PROVINCIA"])
    return provincias


def main():
    playas = obtener_csv()
    print(f"Primeras 5 playas: {playas[:5]}")  # Muestra las primeras 5 playas
    provincias = obtener_provincias(playas)
    print(f"Provincias únicas: {provincias}")  # Muestra las provincias únicas


if __name__ == "__main__":
    main()
