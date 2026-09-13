import sqlite3
import pandas as pd
import requests

def obtener_datos_desempleo_api():
    """Descarga los indicadores de desempleo juvenil de ESPAÑA desde la API del Banco Mundial."""
    print("Consultando la API del Banco Mundial (Desempleo Juvenil en España)...")
    
    url = "http://api.worldbank.org/v2/country/ESP/indicator/SL.UEM.1524.ZS?format=json&date=2015:2024"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()[1]
        
        registros = [
            {
                'cohorte': int(item['date']),
                'tasa_desempleo_juvenil': round(item['value'], 2)
            }
            for item in datos if item['value'] is not None
        ]
        print("✓ Datos de la API de España descargados con éxito.")
        return pd.DataFrame(registros)
    except Exception as e:
        print(f"× Error al consultar la API: {e}")
        return pd.DataFrame()

def ejecutar_ingesta():
    # 1. Obtener datos de la API de España
    df_api = obtener_datos_desempleo_api()
    
    # 2. Cargar datasets locales CSV (2018, 2021, 2022)
    print("Cargando datasets locales en CSV...")
    df_2018 = pd.read_csv("bd/dataset_2018_hash.csv", sep=";", decimal=",").assign(cohorte=2018)
    df_2021 = pd.read_csv("bd/dataset_2021_hash.csv", sep=";", decimal=",").assign(cohorte=2021)
    df_2022 = pd.read_csv("bd/dataset_2022_hash.csv", sep=";", decimal=",").assign(cohorte=2022)
    
    # Unificar las 3 cohortes
    df_estudiantes = pd.concat([df_2018, df_2021, df_2022], ignore_index=True)
    
    # 3. Guardar en SQLite
    ruta_db = "bd/desercion_estudiantes.db"
    conexion = sqlite3.connect(ruta_db)
    
    df_estudiantes.to_sql("estudiantes_consolidados", conexion, if_exists="replace", index=False)
    df_api.to_sql("api_desempleo_juvenil", conexion, if_exists="replace", index=False)
    
    print(f"✓ Base de datos SQLite actualizada en: {ruta_db}")
    conexion.close()

if __name__ == "__main__":
    ejecutar_ingesta()