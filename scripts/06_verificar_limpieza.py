import sqlite3
import pandas as pd

conexion = sqlite3.connect("bd/desercion_estudiantes.db")
df = pd.read_sql("SELECT * FROM estudiantes_limpios LIMIT 20", conexion)
print(df.head(20))
print("\nNulos restantes:", df.isna().sum().sum())
conexion.close()