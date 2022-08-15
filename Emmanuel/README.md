# Analisis de los datos (Emmanuel)
La inspiracion para el orden de la carpeta viene de estas fuentes:

- https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510

# Orden carpetas 
## data/
se encuentran las tablas, de mas a menos procesada
## figures/
se encuentran los plots
## notebooks/
notebooks con el analisis de los datos
## scripts/
scripts con codigo que no sea necesario incluir en los notebooks
## tableau/
archivos de tableau

# Gráficos principales
- [x] Gráfico de barra por año (2010-2020) por paper según modelos de emociones empleado (categoriales o dimensionales)
- [x] Análisis estadístico para determinar si modelos de detección de arousal performan mejor que los basados en valence (Algoritmos de regresión)
- [x] Análisis estadístico para determinar si modelos de detección de arousal performan mejor que los basados en valence (Algoritmos de clasificación)
- [x] Gráficos frencuencia de los modelos algoritimicos, según modelos de regresión y clasificación
- [ ] frencuencia de los tipos de elicitation (por modalidad o tecnica especifica)
- [x] grafico de barra por año para tipos de base de datos
- [x] frencuencia por base de datos
- [x] frecuencia journal, por si es ingeniería o no
- [x] Grafico papers por pais, plot mapa 
- [ ] Grafico papers por pais, plot mapa, tamaño del pais segun cantidad de papers
- [ ] grafo de clasificacion (como en Spezialetti 2018)
- [ ] diferencia entre performances entre modelos: Roy

- [ ] Análisis estadístico, teniendo en cuenta lo obtenido en los gráficos 2 y 3

# Graficos extras
- [x] Frecuencia de papers por tipo de source (conference, journal, pre-print)
- [ ] Gráfico combinatorio (bases de datos privadas y publicas(tipos de bases de datos publicas usadas))
- [x] Gráfico de barras papers por país y continente

# Cambios tabla:
- [x] borrar ann
- [x] agregar regression y classifier antes de todos los modelos
- [x] pasar a minuscula nombre de todos los algoritmos (innecesario, hasta estilizar los graficos)
- [x] pasar todas las medidas de tiempo a segundos (innecesario, hasta realizar un grafico al respecto)
- [x] agregar model id

# Notas (si se han marcado es que ya se han tenido en cuenta a la hora del analisis)
- [x] IEEE no es revista, cambiar eso en tabla
- [ ] Hay datos incompletos en la tabla, rellenarlos
- [x] Tener en cuenta que en la columna APA_citation hay papers que,a pesar de ser el mismo, se han escrito con pequeñas diferencias que hace que puedan ser interpretados como papers distintos. Tener cuidado a la hora de dropear duplicados.
- [ ] tener en cuenta COMO se interpreto que las bases de datos eran publicas o privadas
- [ ] Lorenzo encontró que hay mas bases de datos por paper, por lo que hay que tenerlo en cuenta a la hora del analisis (paper id 37(DEAPx1, AMIGOSx1, MAHNOBx1, DECAFx1, Driving Workloadx1), 62(DEAPx2,MAHNOBx1))
- [x] Se han introducido cambios en la Tabla Normalizada en el drive, que repercuten directamente en los archivos csv localizados en data/cleaned, pero no en data/processed. Por lo que hay que tener cuidado
- [ ] La tabla data base tiene dos papers con datos faltantes (paper_id 7 y 14), hay que rellenar
- [x] Ver grafico 4, cambiar random regression por random forest
- [ ] Ver grafico 2 y 3, dejar de lado modelos de regresion, y tomar en classifier los papers que tengan ambos: HL LV HA LA
- [ ] Tener en cuenta a la hora de publicar: https://towardsdatascience.com/an-introduction-to-making-scientific-publication-plots-with-python-ea19dfa7f51e
- [x] El grafico de papers por pais no incluye Taiwan
- [ ] Cuando se modifiquen los datos de la hoja Data base, tener en cuenta para cambiar los graficos que de ella se hayan desprendido
- [ ] Revisar que la aplicacion de get_value no se haya hecho en columnas donde en una fila puede haber mas de un dato (no funciona)
- [ ] Al grafo falta customizarle el tamaño de sus lineas, segun la fuerza de la relacion entre las categorias
