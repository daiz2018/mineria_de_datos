import sqlite3
import pandas as pd

def limpiar_cadenas_texto():
    conexion = sqlite3.connect("bd/desercion_estudiantes.db")
    df = pd.read_sql("SELECT * FROM estudiantes_limpios", conexion)

    print("=== PASO 4: NORMALIZACIÓN Y LIMPIEZA DE TEXTO ===")

    cols_texto = df.select_dtypes(include=['object']).columns
    
    for col in cols_texto:
        # Eliminar espacios extras y estandarizar a mayúsculas
        df[col] = df[col].astype(str).str.strip().str.upper()
        print(f"✓ Columna de texto '{col}' normalizada (strip + upper).")

    df.to_sql("estudiantes_limpios", conexion, if_exists="replace", index=False)
    conexion.close()
    print("\n✓ Datos completamente limpios y listos para la Sesión 4 (Transformación/Escalado).")

if __name__ == "__main__":
    limpiar_cadenas_texto()