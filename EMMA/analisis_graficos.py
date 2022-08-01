#1. Grafico de barra por año para modelos categoriales y dimensionales



#4. Porcentaje general de frecuencia modelos categoriales y dimensionales

df_data_type

obtener porcentaje de cuantos papers hay para modelos categoriales y dimensionales

#5. Frecuencia de los modelos algoritmicos

df_statistical_learning_models

obtener frecuencia de modelos algoritmicos

no es necesario dropear duplicados

#6. Frecuencia de los tipos de elicitation (por modalidad o tecnica especifica)

df_emotion_elicitation_techniques

obtener frecuencia de los tipos de elicitaion
dropear

obtener frecuencia de uso de tecnicas especificas






#1.

#REPLACE X POR VALOR 
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


dt_data_type_private_public.plot(kind='bar', x='source', y='quantity')
plt.show()

#8. Frecuencia por base de datos
#REPLACE X POR VALOR 
df_data_type_sin_duplicates['DEAP']= df_data_type_sin_duplicates['DEAP'].replace("x", "DEAP")
df_data_type_sin_duplicates['AMIGOS']= df_data_type_sin_duplicates['AMIGOS'].replace("x", "AMIGOS")
df_data_type_sin_duplicates['MAHNOB']= df_data_type_sin_duplicates['MAHNOB'].replace("x", "MAHNOB")
df_data_type_sin_duplicates['CASE']= df_data_type_sin_duplicates['CASE'].replace("x", "CASE")
df_data_type_sin_duplicates['Ascertain']= df_data_type_sin_duplicates['Ascertain'].replace("x", "Ascertain")
df_data_type_sin_duplicates['Cog.load']= df_data_type_sin_duplicates['Cog.load'].replace("x", "Cog.load")
df_data_type_sin_duplicates['Multimodal Dyadic Behavior (MMDB)']= df_data_type_sin_duplicates['Multimodal Dyadic Behavior (MMDB)'].replace("x", "Multimodal Dyadic Behavior (MMDB)")
df_data_type_sin_duplicates['RECOLA']= df_data_type_sin_duplicates['RECOLA'].replace("x", "RECOLA")
df_data_type_sin_duplicates['DECAF']= df_data_type_sin_duplicates['DECAF'].replace("x", "DECAF")
df_data_type_sin_duplicates['Driving Workload']= df_data_type_sin_duplicates['Driving Workload'].replace("x", "Driving Workload")
df_data_type_sin_duplicates['(AV+EC) 2015']= df_data_type_sin_duplicates['(AV+EC) 2015'].replace("x", "(AV+EC) 2015")
df_data_type_sin_duplicates['Liris']= df_data_type_sin_duplicates['Liris'].replace("x", "Liris")
df_data_type_sin_duplicates['SenseEmotion']= df_data_type_sin_duplicates['SenseEmotion'].replace("x", "SenseEmotion")
df_data_type_sin_duplicates['PMEmo']= df_data_type_sin_duplicates['PMEmo'].replace("x", "PMEmo")
df_data_type_sin_duplicates['AFEW']= df_data_type_sin_duplicates['AFEW'].replace("x", "AFEW")
df_data_type_sin_duplicates['Hazumi1911']= df_data_type_sin_duplicates['Hazumi1911'].replace("x", "Hazumi1911")
df_data_type_sin_duplicates['Bio Vid Emo DB']= df_data_type_sin_duplicates['Bio Vid Emo DB'].replace("x", "Bio Vid Emo DB")
df_data_type_sin_duplicates['RCDAT']= df_data_type_sin_duplicates['RCDAT'].replace("x", "RCDAT")
df_data_type_sin_duplicates['DREAMER']= df_data_type_sin_duplicates['DREAMER'].replace("x", "DREAMER")
df_data_type_sin_duplicates['Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status']= df_data_type_sin_duplicates['Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status'].replace("x", "Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status")
df_data_type_sin_duplicates['Stress Recognition in Automobile Drivers Data Set']= df_data_type_sin_duplicates['Stress Recognition in Automobile Drivers Data Set'].replace("x", "Stress Recognition in Automobile Drivers Data Set")
df_data_type_sin_duplicates['PsPM-HRA1']= df_data_type_sin_duplicates['PsPM-HRA1'].replace("x", "PsPM-HRA1")

#CREACION DF PARA PLOTEAR
deap = df_data_type_sin_duplicates["DEAP"]
deap_list = [i for i in deap if i == 'DEAP']
deap_list = int(pd.DataFrame(deap_list).value_counts())

amigos = df_data_type_sin_duplicates["AMIGOS"]
amigos_list = [i for i in amigos if i == 'AMIGOS']
amigos_list = int(pd.DataFrame(amigos_list).value_counts())

manhob = df_data_type_sin_duplicates["MAHNOB"]
manhob_list = [i for i in manhob if i == 'MAHNOB']
manhob_list = int(pd.DataFrame(manhob_list).value_counts())

case = df_data_type_sin_duplicates["CASE"]
case_list = [i for i in case if i == 'CASE']
case_list = int(pd.DataFrame(case_list).value_counts())

Ascertain = df_data_type_sin_duplicates["Ascertain"]
Ascertain_list = [i for i in Ascertain if i == 'Ascertain']
Ascertain_list = int(pd.DataFrame(Ascertain_list).value_counts())

Cogload = df_data_type_sin_duplicates["Cog.load"]
Cogload_list =[i for i in Cogload if i == 'Cog.load']
Cogload_list =int(pd.DataFrame(Cogload_list).value_counts())

mmdb = df_data_type_sin_duplicates["Multimodal Dyadic Behavior (MMDB)"]
mmdb_list = [i for i in mmdb if i == 'Multimodal Dyadic Behavior (MMDB)']
mmdb_list = int(pd.DataFrame(mmdb_list).value_counts())

recola = df_data_type_sin_duplicates["RECOLA"]
recola_list = [i for i in recola if i == 'RECOLA']
recola_list = int(pd.DataFrame(recola_list).value_counts())

decaf = df_data_type_sin_duplicates["DECAF"]
decaf_list= [i for i in decaf if i == 'DECAF']
decaf_list= int(pd.DataFrame(decaf_list).value_counts())

Driving_Workload = df_data_type_sin_duplicates["Driving Workload"]
Driving_Workload_list = [i for i in Driving_Workload if i == 'Driving Workload']
Driving_Workload_list = int(pd.DataFrame(Driving_Workload_list).value_counts())

av_ec = df_data_type_sin_duplicates["(AV+EC) 2015"]
av_ec_list = [i for i in av_ec if i == '(AV+EC) 2015']
av_ec_list = int(pd.DataFrame(av_ec_list).value_counts())

Liris = df_data_type_sin_duplicates["Liris"]
Liris_list = [i for i in Liris if i == 'Liris']
Liris_list = int(pd.DataFrame(Liris_list).value_counts())

SenseEmotion = df_data_type_sin_duplicates["SenseEmotion"]
SenseEmotion_list = [i for i in SenseEmotion if i == 'SenseEmotion']
SenseEmotion_list = int(pd.DataFrame(SenseEmotion_list).value_counts())

PMEmo = df_data_type_sin_duplicates["PMEmo"]
PMEmo_list = [i for i in PMEmo if i == 'PMEmo']
PMEmo_list = int(pd.DataFrame(PMEmo_list).value_counts())

afew = df_data_type_sin_duplicates["AFEW"]
afew_list = [i for i in afew if i == 'AFEW']
afew_list = int(pd.DataFrame(afew_list).value_counts())

Hazumi1911 = df_data_type_sin_duplicates["Hazumi1911"]
Hazumi1911_list = [i for i in Hazumi1911 if i == 'Hazumi1911']
Hazumi1911_list = int(pd.DataFrame(Hazumi1911_list).value_counts())

Bio_vid = df_data_type_sin_duplicates["Bio Vid Emo DB"]
Bio_vid_list = [i for i in Bio_vid if i == 'Bio Vid Emo DB']
Bio_vid_list = int(pd.DataFrame(Bio_vid_list).value_counts())

rcdat = df_data_type_sin_duplicates["RCDAT"]
rcdat_list = [i for i in rcdat if i == 'RCDAT']
rcdat_list = int(pd.DataFrame(rcdat_list).value_counts())

dreamer = df_data_type_sin_duplicates["DREAMER"]
dreamer_list = [i for i in dreamer if i == 'DREAMER']
dreamer_list = int(pd.DataFrame(dreamer_list).value_counts())

Non_EEG = df_data_type_sin_duplicates["Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status"]
Non_EEG_list = [i for i in Non_EEG if i == 'Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status']
Non_EEG_list = int(pd.DataFrame(Non_EEG_list).value_counts())

Stress_recognition = df_data_type_sin_duplicates["Stress Recognition in Automobile Drivers Data Set"]
Stress_recognition_list = [i for i in Stress_recognition if i == 'Stress Recognition in Automobile Drivers Data Set']
Stress_recognition_list = int(pd.DataFrame(Stress_recognition_list).value_counts())

PsPM = df_data_type_sin_duplicates["PsPM-HRA1"]
PsPM_list = [i for i in PsPM if i == 'PsPM-HRA1']
PsPM_list = int(pd.DataFrame(PsPM_list).value_counts())

dicc = {'source': ['DEAP', 'AMIGOS', 'MAHNOB', 'CASE', 'Ascertain', 'Cog.load', 'Multimodal Dyadic Behavior (MMDB)', 'RECOLA', 'DECAF', 'Driving Workload', '(AV+EC) 2015', 'Liris', 'SenseEmotion', 'PMEmo', 'AFEW', 'Hazumi1911', 'Bio Vid Emo DB', 'RCDAT', 'DREAMER', 'Non-EEG Biosignals Data Set for Assessment and Visualization of Neurological Status', 'Stress Recognition in Automobile Drivers Data Set', 'PsPM-HRA1'],
    'quantity': [deap, amigos, manhob, case, Ascertain, Cogload, mmdb, recola, decaf, Driving_Workload, av_ec, Liris, SenseEmotion, PMEmo, afew, Hazumi1911, Bio_vid, rcdat, dreamer, Non_EEG, Stress_recognition, PsPM]}
dt_frec_db = pd.DataFrame.from_dict(dicc)

dt_frec_db.plot(kind='bar', x='source', y='quantity')
plt.show()