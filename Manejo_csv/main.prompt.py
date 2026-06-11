import leer_csv
from pathlib import Path

encabezados, datos, ultimo_id = leer_csv.leer_csv(Path(__file__).parent / "csv" / "datos.csv")
for fila in datos:
    print(fila) 
