import sqlite3
import pandas as pd

def analizar_datos():
    ruta_db = "bd/desercion_estudiantes.db"
    conexion = sqlite3.connect(ruta_db)
    
    # Consulta SQL con LEFT JOIN
    consulta_sql = """
    SELECT 
        e.dni_hash,
        e.cohorte,
        e.abandono_hash AS estado_estudiante,
        u.tasa_desempleo_juvenil
    FROM estudiantes_consolidados e
    LEFT JOIN api_desempleo_juvenil u 
        ON e.cohorte = u.cohorte
    """
    
    df_unido_sql = pd.read_sql(consulta_sql, conexion)
    
    # Resumen de desempleo por cohorte y estado de deserción
    resumen_sql = """
    SELECT 
        e.cohorte,
        e.abandono_hash AS estado,
        COUNT(DISTINCT e.dni_hash) AS total_estudiantes,
        u.tasa_desempleo_juvenil
    FROM estudiantes_consolidados e
    LEFT JOIN api_desempleo_juvenil u ON e.cohorte = u.cohorte
    GROUP BY e.cohorte, e.abandono_hash
    ORDER BY e.cohorte ASC
    """
    
    df_resumen = pd.read_sql(resumen_sql, conexion)
    conexion.close()
    
    print("--- RESUMEN DE ESTUDIANTES Y DESEMPLEO POR COHORTE ---")
    print(df_resumen.to_string(index=False))

if __name__ == "__main__":
    analizar_datos()