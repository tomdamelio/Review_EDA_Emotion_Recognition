importar librerias
estandarizar, crear un entorno
creacion df
estandarizar caracteristcias de los plots
funciones

creacion plots
guardar plot



# TAREAS
- [ ] hay que rehacer analisis estadistico
- [ ] plots que quedan
    - [ ] 1. Hacer un plots para ver como cambia la performance promedio (accuracy) en general con el paso del tiempo.  Esto lo resolveria con un box plot por año de accuracy. Donde en el eje X este de 2010 a 2020, y en el eje Y este el accuracy. Con este plot podriamos analizar si efectivamente mejora la performance de los modelos predictivos con el paso del tiempo
    - [ ] 1.bis. subsjetear esta progresion de accuracies pero por dimension afectiva: hacer un plot (conjunto de boxplots de 2010 a 2020) de valencia y otro plot (conjunto de boxplots de 2010 a 2020) de arousal. Este plot nos ayudaría a ver si cambia la progresion de accuracies dependiendo cada dimension afectiva
    - [ ] 2. Hacer un plot de la progresión de modelos de regresión vs clasificación de 2010 a 2020. Este plot deberia ser igual al plot que ve la progresion de modelos dimensioanles vs categoriales. La idea con este plot seria analizar sin la progresion de papers basados en modelos dimensioanels se acompaña con modelso estadísticos de regresion (que es lo que se esperaria dado el tipo de variable, pero asumimos que no sucede)
- [ ] Juntar los analisis de datos en un unico script y estandarizar el codigo
- [ ] Luego de correr analis de datos con tabla final → tener un reporte de resultados para discutir`


# Anotaciones de Tomas
El analisis estadístico de valencia vs arousal estaba considerando también valores de performance (accuracy) igual a 0. DEl mismo modo, solo se estaban considerando modelos que fueran “HV, LV”, pero si los papers estaban anotados como “LV, HV” no los estaba considerando.

> *Estuve inspeccionadno algunas de estas cosas en el archivo `analisis_exploratorio_2` que pushee en tu carpeta, donde modifque algunas cosas del analisis de perofmrance de arousal vs valencia para ver porque no andaba bien.*
> 

De todasformas, al volver a correr el analisis si esos valores igual a 0 sigue sin dar.

Igual queda para probar otras cosas con respecto a este analisis, antes de descartar esta idea.

En contreto, queda ver si no se puede correr modelos intra-sujeto (donde cada sujeto sea el paper) para comparar arousal vs valencia

¿Como implementariamos esto?

En conreto, habria que seguir los siguientes pasos:

1. Subsetear par quedarse solo con modelso de “HV,LV” (y “LV, “HV”), y “HA,LA” (y “LA, “HA”).
2. FIltrar para quedarnos unicamente con papers que tengan tanto valencia Y arousal (al querer hacer modelos “intrasujeto” es imporatne que se cumpla con esta condición.
3. Agrupar  por paper y sacar la media de la performance (para que quede paper un unico valor de performance promedio de valencia, y un unico valor de performance promedio de arousal. Esto es fundamental para los pasos que siguen)
4. Recien ahora (y  no antes, esto es mucho muy importante) analizar cual es la medida de performance mas prevalente y subsetear para quedarnos solo con esa medida.
5. Hacer T test INTRASUJETO