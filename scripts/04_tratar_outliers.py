import sqlite3
import pandas as pd

def winsorizar_iqr(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Aplica la regla de Tukey (IQR) con factor 1.5 y winsoriza los valores fuera de limite."""
    # PASO 2: Cuartiles
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    
    # PASO 3: Rango Intercuartílico
    iqr = q3 - q1
    
    # PASO 4: Límites (factor 1.5)
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    # PASO 5: Contar valores fuera
    outliers_inf = (df[columna] < limite_inferior).sum()
    outliers_sup = (df[columna] > limite_superior).sum()
    print(f"\n--- Variable: '{columna}' ---")
    print(f"Q1 (25%): {q1:.2f} | Q3 (75%): {q3:.2f} | IQR: {iqr:.2f}")
    print(f"Límite Inferior: {limite_inferior:.2f} | Límite Superior: {limite_superior:.2f}")
    print(f"Outliers detectados -> Por debajo: {outliers_inf} | Por encima: {outliers_sup}")
    
    # PASO 6: Winsorizar (clip)
    df[columna] = df[columna].clip(lower=limite_inferior, upper=limite_superior)
    print(f"✓ Variable '{columna}' winsorizada exitosamente.")
    return df

def ejecutar_tratar_outliers():
    conexion = sqlite3.connect("bd/desercion_estudiantes.db")
    df = pd.read_sql("SELECT * FROM estudiantes_limpios", conexion)
    
    print("=== PASO 3: DETECCIÓN Y WINSORIZACIÓN DE OUTLIERS (REGLA DE TUKEY) ===")
    
    # Identificar variables numéricas activas para winsorizar
    variables_evaluar = ['rendimiento_total', 'cred_sup']
    
    for var in variables_evaluar:
        if var in df.columns:
            df = winsorizar_iqr(df, var)
            
    # Guardar cambios en la base de datos
    df.to_sql("estudiantes_limpios", conexion, if_exists="replace", index=False)
    conexion.close()
    print("\n✓ Tabla 'estudiantes_limpios' actualizada en SQLite con variables winsorizadas.")

if __name__ == "__main__":
    ejecutar_tratar_outliers()
    