import csv
from pathlib import Path

base = Path(__file__).parent
ruta_csv = base / "csv" / "datos.csv"

def leer_csv(ruta_archivo):
    datos = []
    ultimo_id = 0
    encabezados = []
    if ruta_archivo.exists():
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados = lector.fieldnames
            for fila in lector:
                datos.append(dict(fila))
            ultimo_id = len(datos) -1
            
    return encabezados,datos, ultimo_id

def modificar_fila_csv(ruta_archivo, columna_busqueda, valor_busqueda, cambios):
    filas = []

    with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        encabezados = lector.fieldnames

        for fila in lector:
            if fila[columna_busqueda] == str(valor_busqueda):
                fila.update(cambios)
            filas.append(fila)

    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(filas)
