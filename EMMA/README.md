# Concepto
Let’s start with the most front-facing file in your repository, the README file. It should contain information that will help your forgetful future self, newcomers, and collaborators figure out why this project exists, how things are organized, conventions used in the project, and where they can go to find more information.

Note here that the why portion is the most important. It gives the necessary context for the reader of your README file. Think of it as documentation that you leave behind, so you don’t have to sit down and explain over and over the high-level overview of the project.

# Analisis de los datos, versión de Emmanuel
La inspiracion para el orden de la carpeta viene de estas fuentes:

- https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510

# Orden carpetas 
## data/
se encuentran las tablas, de mas a menos procesada
## graficos/
se almacena aca los graficos obtenidos
## notebooks/
notebooks con el analisis de los datos
## scripts/
scripts xd

# TO DO LIST
- [ ] grafico de barra por año para modelos categoriales y dimensionales
- [ ] subsetear para quedarnos con modelos dimensionales(columna affective model), subsetear con regressor, donde nos quedamos solo con las dimensiones que sean arousal/valence, quedarse con la medida de perforrmace que mas aparezca (count), hacer el test estadístico correspondiente (t, wettney, etc)
- [ ] subsetear para quedarnos con modelos dimensionales(columna affective model), quedarse solo con clasificación binarias (LA,HA/LV,HV), quedarse con la medida de performance que mas aparezca (hacer count). hacer el test estadístico correspondiente (t, wettney, etc), que depende del supuesto (si hay normalidad se aplica paramétrico, sino no-parametrico). 
- [ ] frencuencia de los modelos algortimicos 
- [ ] frencuencia de los tipos de elicitation (por modalidad o tecnica especifica)
- [ ] grafico de barra por año para tipos de base de datos
- [ ] frencuencia por base de datos
- [ ] frecuencia journal, por si es ingeniería o no

- [ ] Graficos exploratorios (cuales?)

# Cambios tabla:
- [ ] borrar ann
- [ ] agregar regression y classifier antes de todos los modelos, y pasar todo a minúscula
- [ ] pasar todos las medidas de tiempo a segundos
- [ ] agregar model id

# Notas
- IEEE no es revista, cambiar eso en tabla
- Hay datos incompletos en la tabla, rellenarlos
- Tener en cuenta que en la columna APA_citation hay papers que,a pesar de ser el mismo, se han escrito con pequeñas diferencias que hace que puedan ser interpretados
- como papers distintos. Tener cuidado a la hora de dropear duplicados.
- tener en cuenta COMO se interpreto que las bases de datos eran publicas o privadas
- Lorenzo encontró que hay mas bases de datos por paper, por lo que hay que tenerlo en cuenta a la hora de dropear los duplicados