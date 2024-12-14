import pandas as pd

# Ruta del archivo CSV de entrada
archivo_csv = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\PIPELINE_ASEGURADOS\\LINEA100.csv'

try:
    # Leer el archivo CSV usando el delimitador ';'
    data = pd.read_csv(archivo_csv, encoding='utf-8-sig', sep=';')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv_salida = 'REPORTELINEA100.csv'
    data.to_csv(archivo_csv_salida, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv_salida}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
print(pd.read_csv(archivo_csv_salida))


