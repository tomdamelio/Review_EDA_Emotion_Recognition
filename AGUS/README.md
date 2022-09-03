#### Anotaciones Agustin


### Algunos comentarios en general

-   importante: base de datos. Se pasaron los datos ?? Yo, capaz erroneamente, asumi que sí y me percate recien hoy. No me queda claro. Me parece que no

- si cuando hacemos graficos de frecuencias no diferenciamos entre frecuencia segun modelo o frecuencia segun paper pierde sentido.
ej: si UN solo paper tine 60 modelos y usa una misma caracteristica si solo hacemos frecuencia por modelos se pierde que si bien esa feature
 es utilizada por muchos modelos si tenemos en cuenta por autor o por paper solo UNA persona lo utiliza

 - hacer convenciones para:
        - los nombres de variables (en especial df): acá en realidad yo estuve en falta y no lo hice. Podría modificarlo
        para que los nombres x ej de las Dataframes se adapten al formato usado por Emma (primero porque me parece correcto y segundo porque 
        es el que mas codigo hizo entonces habria que modificar menos)
        - cómo se va a subsetear por columnas: 
                                       ``` nombre_df['nombre_columna] ó nombre_df.nombre_columna```



 - ¿Subsetear segun nombre de columna en vez de por posición? Puede hacer el codigo mas legible e intuitivo


 - siempre que se plotea correr tmb un value_counts o simil para tener a mano el formato tabla tmb de esas frecuencias (incluso podría ser en %):

    ```nombre_df['nombre_columna'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'```

- La columna 'auditory_other' está vacía

- en el plot de cantidad de papers por journal: se podrían agrupar esos journals con algun criterio para hacer mas bonita la distribución y para que tenga mas sentido a nuestros fines?.

Ej: agruparlos por ingenieria, neurociencias y psicología, y otros. Seguramente haya mas de ingenieria, y ese dato nos puede servir para justificar el fin de nuestro trabajo. (se podría hacer sin agruparlos pero si se agrupa creo que queda mejor)



#### Algunos conflictos que Emma señaló y me competen:

-paper id 22 tiene mal pasada las performances de accuracy
respuesta: va vacío pues no es claro el paper. APLICA UN '-'

- La tabla data base tiene dos papers con datos faltantes (paper_id 7 y 14), hay que rellenar
 rta: paper 14: en los que se elicita mediante videos de ese paper en realidad tendría que ir 'Video2GIF dataset' como data set utilizado (falta cambiar)


  Lorenzo encontró que hay mas bases de datos por paper, por lo que hay que tenerlo en cuenta a la hora del analisis
   (paper id 37(DEAPx1, AMIGOSx1, MAHNOBx1, DECAFx1, Driving Workloadx1), 62(DEAPx2,MAHNOBx1))

   rta : Si, es un modelo que entrena con datos de diferentes bases de datos.
