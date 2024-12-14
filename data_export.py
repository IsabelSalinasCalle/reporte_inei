import pandas as pd

# Ruta del archivo CSV transformado
archivo_csv_transformado = 'REPORTELINEA100_transformado.csv'

# Ruta del archivo Excel para exportar
archivo_excel = 'reporte_agrupado_por_ano_departamento.xlsx'

try:
    # Leer el archivo CSV transformado
    print(f"Leyendo el archivo transformado: {archivo_csv_transformado}")
    data_transformada = pd.read_csv(archivo_csv_transformado)
    
    # Verificar una muestra de los datos antes de exportar
    print("Muestra de los datos a exportar:")
    print(data_transformada.head())
    
    # Exportar a Excel
    data_transformada.to_excel(archivo_excel, index=False, sheet_name='Reporte Agrupado')
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {archivo_csv_transformado}. Verifica la ruta y el nombre del archivo.")
except Exception as e:
    print(f"Error al exportar los datos: {e}")




