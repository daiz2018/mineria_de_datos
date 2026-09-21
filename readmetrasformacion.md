# Proyecto de Minería de Datos – Deserción Estudiantil

Proyecto académico orientado al análisis de datos relacionados con la deserción estudiantil.

## Sesión 4 – Transformación de datos

En esta etapa se realiza el preprocesamiento de los datos almacenados en SQLite para dejarlos preparados para posteriores procesos de modelado.

Se aplican las siguientes transformaciones:

- Escalamiento de variables numéricas mediante MinMaxScaler, StandardScaler y RobustScaler.
- Codificación de variables categóricas mediante *One-Hot Encoding*.
- Discretización de rendimiento_total mediante cuantiles.
- Análisis de reducción de dimensionalidad mediante *PCA*.
- Construcción de la matriz final de características utilizando las variables numéricas estandarizadas y las variables categóricas codificadas.

### Ejecución

```bash
python3 scripts/07_transformaciones.py