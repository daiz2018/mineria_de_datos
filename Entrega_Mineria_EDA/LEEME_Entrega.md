# Entrega de Minería de Datos

## Archivos

- `EDA_Desercion_Entrega.ipynb`: notebook con las seis secciones del informe, siete figuras interpretadas y cuatro hallazgos con evidencia y acción.
- `Informe_EDA_Entrega.md`: informe de laboratorio para lectura, con figuras y conclusiones.
- `requirements.txt`: librerías necesarias para repetir el análisis.
- `resultados_entrega/`: figuras y tablas exportadas, bitácora, diccionario y vista analítica documentada.

## Abrir en VS Code

1. Conserva tu notebook anterior como respaldo.
2. Pon `EDA_Desercion_Entrega.ipynb` junto a `desercion_estudiantes.db`, dentro de tu carpeta de trabajo.
3. Selecciona Python 3.13.15, pulsa Ejecutar todo y guarda con Cmd+S.
4. La revisión de duplicados recorre toda la tabla original de 464.739 filas y puede tardar varios minutos. No se limita a 20 filas.

Requiere pandas, numpy y matplotlib; son las herramientas que ya se usaron para las gráficas. Si faltan, ejecutar en una celda temporal `%pip install pandas matplotlib`, reiniciar y ejecutar todo.

## Contenido según la rúbrica

1. Portada y contexto: pregunta y objetivo.
2. Calidad: faltantes, duplicados exactos, extremos y decisiones.
3. Univariado: descriptivos y cuatro figuras interpretadas.
4. Bivariado/multivariado: función de correlación, dispersión, heatmap y cruces por estado.
5. Cuatro hallazgos con evidencia y acción; conclusiones y límites.
6. Anexos: código completo ejecutado, diccionario, bitácora y exportaciones.

## Pendientes que deben explicarse

Los códigos A/B todavía no tienen significado confirmado. Se calculan cruces del campo registrado sin llamar a ninguno “desertor”. Jonathan o el diccionario de origen deben confirmar el mapa, el horizonte y las definiciones de variables para completar la interpretación en términos de abandono.

El análisis preserva los faltantes originales; no presenta los rendimientos rellenados de 2018 como mediciones. Propone la unidad estudiante-programa-año y resume numéricas por mediana. Esa decisión y sus límites están escritos en el cuaderno.

## Repositorio

La base y los CSV originales permanecen locales; no incluir la base de aproximadamente 597 MB en un commit. El notebook, el informe y `resultados_entrega` contienen los entregables revisados. La base original no se modifica.
