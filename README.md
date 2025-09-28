# Proyecto: Procesamiento de Municipios y Playas (AEMET)

## Descripción
Este proyecto procesa datos públicos proporcionados por AEMET (Agencia Estatal de Meteorología) para generar archivos JSON que representan comunidades autónomas, provincias, municipios y playas.

## Fuentes de Datos
- **diccionario24.xlsx**: Información de municipios
- **Playas_codigos.csv**: Información de playas

## Estructura del Proyecto
- `main.py`: Script principal que ejecuta todo el flujo
- `municipalities.py`: Lógica de lectura y conversión de municipios
- `beaches.py`: Lógica de lectura y conversión de playas
- `diccionario24.xlsx`: Datos fuente de municipios (AEMET)
- `Playas_codigos.csv`: Datos fuente de playas (AEMET)
- `comunidades_autonomas.json`: JSON estático creado manualmente
- `provincias.json`: JSON estático creado manualmente
- `municipios.json`: Output generado con el script
- `playas.json`: Output generado con el script
- `requirements.txt`: Dependencias del entorno Python
- `__pycache__`: Archivos temporales de Python

## Uso
### Pasos
1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias con pip
4. Ejecutar `main.py` para generar los archivos JSON

## Dependencias
- pandas
- openpyxl
- et_xmlfile

## Notas
Los datos provienen de fuentes públicas de AEMET, y el proyecto facilita su uso en APIs, visualizaciones o desarrollos propios.

## Autor
Brewpot418
