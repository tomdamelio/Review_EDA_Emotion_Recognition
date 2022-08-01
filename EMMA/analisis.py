#Importar librerias a usar
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#CREACION DE FATA FRAMES
df_metadata = pd.read_csv('Tabla Normalizada - Metadata.csv', index_col = ['paper_id'])
df_data_type = pd.read_csv('Tabla Normalizada - Data type.csv')
df_participants = pd.read_csv('Tabla Normalizada - Participants.csv', index_col = ['paper_id'])
df_self_report = pd.read_csv('Tabla Normalizada - Self report.csv', index_col = ['paper_id'])
df_emotion_elicitation_techniques = pd.read_csv('Tabla Normalizada - Emotion elicitation techniques.csv', index_col = ['paper_id'])
df_eda = pd.read_csv('Tabla Normalizada - EDA.csv', index_col = ['paper_id'])
df_statistical_learning_models = pd.read_csv('Tabla Normalizada - Statistical Learning model.csv', index_col = ['paper_id'])
df_performances = pd.read_csv('Tabla Normalizada - Performances.csv', index_col = ['paper_id'])

#Creacion de gráficos:


#7. Gráfico de barra por añó para tipos de bases de datos

df_data_type=df_data_type.fillna('-')
df_data_type_sin_duplicates = df_data_type.drop_duplicates(subset='paper_id')

category_order = [2010, 2011, 2012, 2013, 2014, 2015, 2015, 2016, 2017, 2018, 2019, 2020]
sns.set_style('darkgrid')
sns.countplot(x='year', 
    data= df_data_type_sin_duplicates, 
    hue='db_type', 
    order=category_order)
plt.show()



#9. Frecuencia de journals, según si tienen origen Ingenieria o no
#df_metadata
#frecuencia de journals, y mostrar cuales son ingenieria y cuales no
df_metadata=df_metadata.fillna('-')
df_metadata_sources = df_metadata.drop_duplicates(subset='paper_id')

df_metadata_sources['source_type_journal']= df_metadata_sources['source_type_journal'].replace("x", "Journal") 
df_metadata_sources['source_type_conference'] = df_metadata_sources['source_type_conference'].replace("x", "Conference")
df_metadata_sources["source_type_preprint"]=df_metadata_sources["source_type_preprint"].replace("x", "Preprint")

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

#ploteado
dt_sources.plot(kind='bar', x='source', y='quantity')
plt.show()

