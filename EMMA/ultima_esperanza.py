#Importar librerias a usar
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#CREACION DE FATA FRAMES
df_metadata = pd.read_csv('Tabla Normalizada - Metadata.csv')
df_data_type = pd.read_csv('Tabla Normalizada - Data type.csv')
df_participants = pd.read_csv('Tabla Normalizada - Participants.csv')
df_self_report = pd.read_csv('Tabla Normalizada - Self report.csv')
df_emotion_elicitation_techniques = pd.read_csv('Tabla Normalizada - Emotion elicitation techniques.csv')
df_eda = pd.read_csv('Tabla Normalizada - EDA.csv')
df_statistical_learning_models = pd.read_csv('Tabla Normalizada - Statistical Learning model.csv')
df_performances = pd.read_csv('Tabla Normalizada - Performances.csv')

df_metadata=df_metadata.fillna('-')
df_metadata_sin_duplicates = df_metadata.drop_duplicates(subset='paper_id')

df_sources = df_metadata_sin_duplicates.iloc[:,7:10]
print(df_sources)
def get_value(row):
     for c in df_sources.columns:
         if row[c]== 'x':
             return c

df_sources = df_sources.apply(get_value, axis=1)
df_sources = pd.DataFrame(df_sources)
df_sources.columns = ['Source type']

sns.countplot(x='Source type', data=df_sources)
plt.show()

#bases de datos
df_data_type=df_data_type.fillna('-')
df_data_type_sin_duplicates = df_data_type.drop_duplicates(subset='paper_id')

df_db = df_data_type_sin_duplicates.iloc[:,10:]
def get_value(row):
     for c in df_db.columns:
         if row[c]== 'x':
             return c

df_db = df_db.apply(get_value, axis=1)
df_db = pd.DataFrame(df_db)
df_db.columns = ['Data base']

sns.countplot(x='Data base', data=df_db)
plt.xticks(rotation=90)
plt.show()

#garfico barra por año para modelos categoriales y dimensionales
df_data_type=df_data_type.fillna('-')
df_data_type_sin_duplicates = df_data_type.drop_duplicates(subset='paper_id')

category_order = [2010, 2011, 2012, 2013, 2014, 2015, 2015, 2016, 2017, 2018, 2019, 2020]
sns.set_style('darkgrid')
sns.countplot(x='year', 
    data= df_data_type_sin_duplicates, 
    hue='db_type', 
    order=category_order)
plt.show()

#frecuencia tipos elicitation por modalidad

df_emotion_elicitation_techniques=df_emotion_elicitation_techniques.fillna('-')
df_emotion_elicitation_techniques_sin_duplicates = df_emotion_elicitation_techniques.drop_duplicates(subset='paper_id')

df_eli_modalidad = df_emotion_elicitation_techniques_sin_duplicates.iloc[:,3:7]
def get_value(row):
     for c in df_eli_modalidad.columns:
         if row[c]== 'x':
             return c

df_eli_modalidad = df_eli_modalidad.apply(get_value, axis=1)
df_eli_modalidad = pd.DataFrame(df_eli_modalidad)
df_eli_modalidad.columns = ['Elicitation modality']

sns.countplot(x='Elicitation modality', data=df_eli_modalidad)
plt.xticks(rotation=90)
plt.show()

#por revista
df_source_title = df_metadata_sin_duplicates[['paper_id','source_title']]
sns.countplot(x='source_title', data=df_source_title)
plt.xticks(rotation=90)
plt.show()

IEEE NO ES REVISTA