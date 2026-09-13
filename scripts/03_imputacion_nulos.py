import sqlite3
import pandas as pd

def ejecutar_imputacion():
    conexion = sqlite3.connect("bd/desercion_estudiantes.db")
    df = pd.read_sql("SELECT * FROM estudiantes_consolidados", conexion)

    # 1. Definimos las variables clave para la imputación
    cols_numericas = ['rendimiento_total', 'cred_sup'] 
    cols_categoricas = ['tipo_ingreso', 'estudios_p_hash', 'estudios_m_hash']

    print("=== PASO 2: IMPUTACIÓN CON MEDIANA Y MODA ===\n")

    # Numéricas: La mediana resiste outliers
    for col in cols_numericas:
        if col in df.columns and df[col].isna().sum() > 0:
            mediana = df[col].median()
            print(f"Imputando {col} = {mediana:.1f}")
            df[col] = df[col].fillna(mediana)

    # Categóricas: La moda (valor más frecuente)
    for col in cols_categoricas:
        if col in df.columns and df[col].isna().sum() > 0:
            moda_val = df[col].mode()[0]
            print(f"Imputando {col} con su moda = {moda_val}")
            df[col] = df[col].fillna(moda_val)

    # Verificación final sobre el grupo de columnas seleccionadas
    cols_evaluadas = cols_numericas + cols_categoricas
    nulos_restantes = df[cols_evaluadas].isna().sum().sum()
    print(f"\n{nulos_restantes} nulos restantes en las columnas seleccionadas")

    # Guardar en la nueva tabla 'estudiantes_limpios'
    df.to_sql("estudiantes_limpios", conexion, if_exists="replace", index=False)
    conexion.close()
    print("✓ Tabla 'estudiantes_limpios' actualizada exitosamente en SQLite.")

if __name__ == "__main__":
    ejecutar_imputacion()