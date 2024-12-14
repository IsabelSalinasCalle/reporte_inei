import pandas as pd

# Ruta del archivo CSV de entrada
archivo_csv_salida = 'REPORTELINEA100.csv'
archivo_csv_transformado = 'REPORTELINEA100_transformado.csv'

try:
    # Leer el archivo CSV usando el delimitador ';'
    data = pd.read_csv(archivo_csv_salida)
    
    # Verificar que las columnas 'ANO' y 'DEPARTAMENTO' están presentes
    if 'ANO' in data.columns and 'DEPARTAMENTO' in data.columns:
        # Convertir las columnas de interés a tipo numérico, reemplazando valores no numéricos por 0
        columnas_a_sumar = [
            'No. DE CONSULTAS TELEFONICAS -TOTAL',
            'No. DE CONSULTAS TELEFONICAS - HOMBRES',
            'No. DE CONSULTAS TELEFONICAS - MUJERES'
        ]
        
        for columna in columnas_a_sumar:
            if columna in data.columns:
                # Convertir a numérico y reemplazar valores no válidos con 0
                data[columna] = pd.to_numeric(data[columna], errors='coerce').fillna(0)
            else:
                print(f"Advertencia: La columna '{columna}' no está en los datos.")
        
        # Agrupar los datos por 'ANO' y 'DEPARTAMENTO', y sumar las columnas de llamadas
        reporte = data.groupby(['ANO', 'DEPARTAMENTO']).agg({
            'No. DE CONSULTAS TELEFONICAS -TOTAL': 'sum',
            'No. DE CONSULTAS TELEFONICAS - HOMBRES': 'sum',
            'No. DE CONSULTAS TELEFONICAS - MUJERES': 'sum'
        }).reset_index()
        reporte.to_csv(archivo_csv_transformado, index=False)
                
        # Verificar el reporte antes de exportarlo
        print("Reporte generado:")
        print(reporte)
        
        # Ruta del archivo Excel de salida
        archivo_excel = 'reporte_agrupado_por_ano_departamento.xlsx'
        
        # Exportar el reporte a Excel
        reporte.to_excel(archivo_excel, index=False)
        
        print(f"Reporte generado y exportado exitosamente a {archivo_excel}")
    else:
        print("Las columnas 'ANO' o 'DEPARTAMENTO' no están en los datos.")
        
except Exception as e:
    print(f"Error al generar el reporte: {e}")