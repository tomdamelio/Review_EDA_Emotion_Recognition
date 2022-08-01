
journal = df_metadata_sources.replace(['x'],'journal')
journal = journal['source_type_journal'].value_counts()
journal = pd.DataFrame(journal[0:1])

conference = df_metadata_sources.replace(['x'],'conference')
conference = conference['source_type_conference'].value_counts()
conference = pd.DataFrame(conference[0:1])

preprint = df_metadata_sources.replace(['x'],'preprint')
preprint = preprint['source_type_preprint'].value_counts()
preprint = pd.DataFrame(preprint[0:1])

df1['DEAP ']= df1['DEAP ']. replace("x", "DEAP") 
df1['Multimodal Dyadic Behavior (MMDB)'] = df1['Multimodal Dyadic Behavior (MMDB)']. replace("x", "MMDB")
df1["Ascertain"]=df1["Ascertain"].replace("x", "Ascertain")


source = pd.concat([journal, conference, preprint])

#PRIMERA OPCION CON SOURCE_TYPE, PERO LA NUEVA COLUMNA TIENE DATOS COMO "-CONFERENCE-"
print(df_metadata_sources)

df_metadata_sources['source_type_journal']= df_metadata_sources['source_type_journal'].replace("x", "Journal") 
df_metadata_sources['source_type_conference'] = df_metadata_sources['source_type_conference'].replace("x", "Conference")
df_metadata_sources["source_type_preprint"]=df_metadata_sources["source_type_preprint"].replace("x", "Preprint")

df_metadata_sources["sources"] = (df_metadata_sources['source_type_journal'] + df_metadata_sources["source_type_conference"] + df_metadata_sources["source_type_preprint"]).astype('str')
df_sources = df_metadata_sources[['sources']]

print(df_sources)
#TERMINA PRIMERA OPCION


#

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)


# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)

#valores= [55, 48, 1]
#nombre = ["journal","conference","preprint"]
#colores= "blue", "red", "orange"
#plt.pie(valores, labels= nombre, colors= colores, autopct= "%0.1f%%",)
#plt.title("Papers por tipo de source")
#plt.show()

#countries = df_metadata_sin_duplicates.pivot_table(columns=['first_author_country_affiliation'], aggfunc='size')
#source_title = df_metadata_sin_duplicates.query('source_type_journal=="x"')
#source_title= source_title.pivot_table(columns=['source_title'], aggfunc='size')

#countries.plot(kind='bar', title='Mis cojones al viento', x='country', y='paper quantity')
#plt.show()

#source_title.plot(kind='bar', title='Mis cojones al viento', x='country', y='paper quantity')
#plt.show()

#pepe = df_metadata_sin_duplicates['source_title'].unique()

#fig, ax = plt.subplots()
###

#papers_journal_count = papers_journal['source_type_journal'].value_counts()
#papers_conference = papers_conference.replace(['x'],'conference')
#papers_conference_count = papers_conference['source_type_conference'].value_counts()
#papers_preprint = papers_preprint.replace(['x'],'preprint')
#papers_preprint_count = papers_preprint['source_type_preprint'].value_counts()


#PLOTEADO
#fig, ax = plt.subplots()
#ax.bar(papers_source.index, papers_source[''])
#plt.show()

#journal = df_metadata_sin_duplicates.query('source_type_journal=="x"')
#journal = journal.replace(['x'],'journal')
#print(journal[['apa_citation','source_type_journal']])
#print(journal['source_type_journal'].value_counts())
#print(df_metadata_sin_duplicates[['apa_citation','year', 'first_author_country_affiliation']])

#paper_per_year = df_metadata['year'].value_counts()
#paper_per_year.plot(kind='bar', title='Mis cojones al viento', x='year', y='paper quantity')
#plt.show()

#paper_per_country = df_metadata['first_author_country_affiliation'].value_counts()
#paper_per_country.plot(kind='bar', title='Mis cojones al viento', x='country', y='paper quantity')
#plt.show()

#papers_journal = df_metadata_sin_duplicates[df_metadata_sin_duplicates['source_type_journal'] == 'x']
#papers_conference = df_metadata_sin_duplicates[df_metadata_sin_duplicates['source_type_conference'] == 'x']
#papers_preprint = df_metadata_sin_duplicates[df_metadata_sin_duplicates['source_type_preprint'] == 'x']

#papers_journal = papers_journal.replace(['x'],'journal')
#papers_journal_count = papers_journal['source_type_journal'].value_counts()
#papers_conference = papers_conference.replace(['x'],'conference')
#papers_conference_count = papers_conference['source_type_conference'].value_counts()
#papers_preprint = papers_preprint.replace(['x'],'preprint')
#papers_preprint_count = papers_preprint['source_type_preprint'].value_counts()

#papers_per_source_type = {'journal':papers_journal_count, 'conference':papers_conference_count, 'preprint':papers_preprint_count}
#df_papers_per_source_type = pd.DataFrame(papers_per_source_type)
#print(papers_per_source_type)

#print(papers_journal[['apa_citation', 'source_type_journal']])
#print(df_papers_per_source_type)
#fig, ax = plt.subplots()
#ax.bar(df_papers_per_source_type.index, df_papers_per_source_type.[''], title='Mis cojones al viento')
#plt.show()

#print(papers_conference_count)
#print(papers_preprint_count)

#papers_per_sourcetype = {'journal': papers_journal_count,'conference' : papers_conference_count,'preprint' : papers_preprint_count}
#df_papers_per_sourcetype = pd.DataFrame(papers_per_sourcetype)
#print(df_papers_per_sourcetype)

#df_papers_per_sourcetype.plot(kind='bar', title='Mis cojones al viento', x='source type', y='paper quantity')
#plt.show()

#papers_journal.plot(kind='bar', title='Mis cojones al viento', x='journal or not', y='paper quantity')
#plt.show()

#journal = df_metadata_sin_duplicates.query('source_tipe_journal=="x"')
#print(journal)

#1. SOURCES - reemplazamos las x en las columnas por su respectivo tipo de source
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

df2_data_type = df_data_type_sin_duplicates[['paper_id', 'db_private', 'db_public', 'is_database']]

df2_data_type['db_private']= df2_data_type['db_private'].replace("x", "Private")
df2_data_type['db_private']= df2_data_type['db_private'].replace("X", "Private")  
df2_data_type['db_public'] = df2_data_type['db_public'].replace("x", "Public")
df2_data_type['db_public'] = df2_data_type['db_public'].replace("X", "Public")
df2_data_type["is_database"]=df2_data_type["is_database"].replace("x", "Public")
df2_data_type["is_database"]=df2_data_type["is_database"].replace("X", "Public")

#CREACION DF PARA PLOTEAR
private = df2_data_type["db_private"]
private_list = [i for i in private if i == 'Private']
private_list = int(pd.DataFrame(private_list).value_counts())

public1 = df2_data_type["db_public"]
public_list1 = [i for i in public1 if i == 'Public']
public_list1 = int(pd.DataFrame(public_list1).value_counts())

public2 = df2_data_type["is_database"]
public_list2 = [i for i in public2 if i == 'Public']
public_list2 = int(pd.DataFrame(public_list2).value_counts())

public_list = public_list1+public_list2

dicc = {'source': ['private','public'],
    'quantity': [private_list, public_list]}
dt_data_type_private_public = pd.DataFrame.from_dict(dicc)
