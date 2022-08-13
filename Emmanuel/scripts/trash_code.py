#Trozos de código que quedaron sin usar, y pueden mejorarse o servir para ser retomados mas adelante

#Esta funcion toma una serie de columnas de un df y devuelve un df, con la frecuencia de aparicion de cada valor
#definimos primero los parametros: el dataframe a usar y un diccionario con el nombre de las columnas y los valores a buscar su frecuencia

def normalizador (df, columnas, nombre):
    list_nombres = []
    list_values = []

    for (label, content) in df[columnas].iteritems():
        list_nombres = label
        list_values = content.values()
        
    dicc = {nombre : list_nombres,
        'values' : list_values}

    return pd.DataFrame(dicc)


def normalizador(df, col_dicc):
    #creamos un dicc, le asignamos el nombre al type, e iteramos para el valor buscado, y repetimos para cada key
    dicc = {'types':[ el nombre de cada tipo ],
        'quantity':[ los valores para cada tipo ]}
    
    for value in col_dicc:
        dicc[key] = value
        contador = 0
        if value == valor buscado:
            contador += 1
        else:
            None

recordar:
df = df[df[col_name] == value_buscado]
puedo usar list comprehension para diccionarios
#zip puede unir los valores de dos columnas, y luego devolverlas en forma de lista con list(nombre_zip):

    #transformamos el diccionario creado en df para plotearlo
    output = pd.DataFrame.from_dict(dicc)
    return output

col_list = ['source_type_journal','source_type_conference','source_type_preprint']
df_sources = normalizador(df_metadata_sources, col_list)

#Extraemos la columna que nos interesa, craemos una lista con la cantidad de veces que aparece el tipo de source,
#luego lo volvemos un data frame para contar cuantas veces aparece, y lo volvemos un entero para formar luego un diccionario

journal = df_metadata_sources["source_type_journal"]
journal_list = [i for i in journal if i == 'Journal']
journal_list = int(pd.DataFrame(journal_list).value_counts())

conference = df_metadata_sources["source_type_conference"]
conference_list = [i for i in conference if i == 'Conference']
conference_list = int(pd.DataFrame(conference_list).value_counts())

preprint = df_metadata_sources["source_type_preprint"]
preprint_list = [i for i in preprint if i == 'Preprint']
preprint_list = int(pd.DataFrame(preprint_list).value_counts())

#creamos un diccionario con los tipos de source y su cantidad, luego lo volvemos df para plotearlo
dicc = {'source': ['journal','conference','preprint'],
    'quantity': [journal_list, conference_list, preprint_list]}
dt_sources = pd.DataFrame.from_dict(dicc)

#intento con funcion NORMALIZADORA
def normalizador (df, columnas, nombre):
    list_nombres = []
    list_values = []

    for (label, content) in df[columnas].iteritems():
        list_nombres = label
        list_values = content.values()
        
    dicc = {nombre : list_nombres,
        'values' : list_values}

    return pd.DataFrame(dicc)

nuevo_df = normalizador(df_metadata_sources, [:1,3], 'Source type')
print(nuevo_df)