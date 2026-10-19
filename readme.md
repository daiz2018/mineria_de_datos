# Predicción del Riesgo de Deserción Universitaria

## Minería de Datos

**Corporación Universitaria Minuto de Dios – UNIMINUTO**  
**Programa:** Ingeniería de Sistemas  
**Asignatura:** Minería de Datos  
**Docente:** Esteban Ernesto Morales Castro  

### Integrantes
- Jonathan Díaz Salgado
- Diego Alberto Ñanguma Briñez

---

## Descripción del proyecto

Este proyecto busca analizar información académica, demográfica, socioeconómica y de actividad digital de estudiantes universitarios con el propósito de identificar factores relacionados con la deserción estudiantil.

A partir del análisis de los datos se pretende posteriormente desarrollar un modelo de minería de datos que permita predecir el riesgo de abandono universitario.

---

## Planteamiento del problema

La deserción universitaria representa un problema para las instituciones de educación superior, ya que afecta tanto la trayectoria de los estudiantes como los recursos y resultados de las universidades.

Las instituciones disponen de grandes cantidades de información sobre sus estudiantes, pero analizar manualmente estos datos puede resultar complejo. Por esta razón, el proyecto propone utilizar técnicas de minería de datos para encontrar patrones relacionados con el abandono y permitir una identificación temprana de estudiantes con riesgo de deserción.

---

## Pregunta de investigación

**¿Es posible utilizar técnicas de minería de datos para identificar patrones y predecir el riesgo de deserción de estudiantes universitarios a partir de sus características académicas, demográficas, socioeconómicas y de comportamiento digital?**

---

## Objetivo general

Analizar y desarrollar un modelo de minería de datos que permita identificar factores asociados a la deserción universitaria y predecir el riesgo de abandono de los estudiantes.

---

## Dataset

Para el desarrollo del proyecto se utilizará **StudentDropoutDataset**, publicado en Zenodo por Igualde-Sáez et al. (2025).

El conjunto de datos contiene información anonimizada relacionada con estudiantes, cursos, programas académicos, rendimiento, matrícula y actividad digital.

### Características principales

| Indicador | Cantidad |
|---|---:|
| Estudiantes | 39,364 |
| Cursos | 4,989 |
| Programas académicos | 163 |
| Registros totales | 464,739 |
| Variables principales | 77 |

### Información disponible

El dataset contiene información relacionada con:

- Información de ingreso
- Información académica
- Rendimiento académico
- Matrículas y créditos
- Información sociodemográfica
- Indicadores económicos
- Actividad en el LMS
- Acceso a Wi-Fi
- Información relacionada con el abandono

---

## Metodología

El proyecto se desarrollará siguiendo las fases de **CRISP-DM**, permitiendo organizar el proceso de minería de datos desde la comprensión del problema hasta el desarrollo y evaluación de los modelos.

Las etapas contempladas son:

1. Comprensión del negocio
2. Comprensión de los datos
3. Preparación de los datos
4. Modelado
5. Evaluación
6. Despliegue

---

## Tecnologías

- Python
- Pandas
- Visual Studio Code
- Git
- GitHub

---

## Estado actual

El proyecto se encuentra en su etapa inicial, correspondiente a la definición del problema y comprensión de los datos.

Se cuenta con el dataset inicial que será utilizado para realizar el análisis exploratorio, preparación de los datos y posteriores técnicas de minería de datos.

---

## Referencia

Igualde-Sáez, M., et al. (2025). *StudentDropoutDataset* [Conjunto de datos]. Zenodo.

DOI: https://doi.org/10.5281/zenodo.17239943



## Informe EDA — revisión documental

La entrega reúne revisión de calidad, cuatro gráficas univariadas, dispersión, mapa de calor, cruces por estado y hallazgos con evidencia y acciones sugeridas.

- [Informe de laboratorio](Entrega_Mineria_EDA/Informe_EDA_Entrega.md)
- [Notebook ejecutado](Entrega_Mineria_EDA/EDA_Desercion_Entrega.ipynb)
- [Instrucciones y limitaciones](Entrega_Mineria_EDA/LEEME_Entrega.md)
- [Figuras y tablas de respaldo](Entrega_Mineria_EDA/resultados_entrega)

Para ejecutarlo se necesita una copia local de `desercion_estudiantes.db`, con las tablas `estudiantes_consolidados` y `estudiantes_limpios`. La base no se publica en este repositorio. La fuente original está en [Zenodo](https://doi.org/10.5281/zenodo.17239943); la base preparada debe obtenerse del equipo. Consultar las instrucciones de la entrega para rutas y dependencias.

Los códigos A/B y el horizonte de abandono siguen pendientes de definición autorizada. Los cruces se presentan como códigos y no como tasas de deserción interpretadas.
