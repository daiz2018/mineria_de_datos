import sqlite3
import pandas as pd

def diagnostico_inicial():
    conexion = sqlite3.connect("bd/desercion_estudiantes.db")
    df = pd.read_sql("SELECT * FROM estudiantes_consolidados", conexion)
    conexion.close()

    print("=== PASO 1: LAS TRES PREGUNTAS DEL DIAGNÓSTICO ===\n")

    # 1. ¿Cuánto falta?
    print("# 1. ¿Cuánto falta? (Variables con nulos)")
    nulos = df.isna().sum()
    print(nulos[nulos > 0])
    if nulos[nulos > 0].empty:
        print("No se encontraron valores nulos.")

    # 2. ¿Qué está repetido?
    print("\n# 2. ¿Qué está repetido?")
    print("Duplicados exactos:", df.duplicated().sum())

    # 3. ¿Qué se sale de rango?
    print("\n# 3. ¿Qué se sale de rango? (Resumen estadístico)")
    cols_numericas = ['rendimiento_total', 'pft_total_minutes', 'n_wifi_days']
    cols_existentes = [c for c in cols_numericas if c in df.columns]
    
    if cols_existentes:
        print(df[cols_existentes].describe().round(1))
    else:
        print(df.describe().round(1))

if __name__ == "__main__":
    diagnostico_inicial()