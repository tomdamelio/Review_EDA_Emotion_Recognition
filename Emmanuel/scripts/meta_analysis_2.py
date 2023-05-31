#%%
import pandas as pd
import numpy as np
import scipy.stats as stats

#%%
# Reseteo del directorio principal
os.getcwd()
os.chdir("C:\\Users\dadam\Review_EDA_Emotion_Recognition")

#%%
# Read the data
df_metadata = pd.read_csv('.\data\Tabla Normalizada - Metadata.csv')
df_data_type = pd.read_csv('.\data\Tabla Normalizada - Data type.csv')
df_participants = pd.read_csv('.\data\Tabla Normalizada - Participants.csv')
df_self_report = pd.read_csv('.\data\Tabla Normalizada - Self report.csv')
df_emotion_elicitation_techniques = pd.read_csv('.\data\Tabla Normalizada - Emotion elicitation techniques.csv')
df_eda = pd.read_csv('.\data\Tabla Normalizada - EDA.csv')
df_statistical_learning_models = pd.read_csv('.\data\Tabla Normalizada - Statistical Learning model.csv')
df_performances = pd.read_csv('.\data\Tabla Normalizada - Performances.csv')
df_alg_perf = pd.read_csv('.\data\Tabla Normalizada - Alg_Perf.csv')

#%%
# Filter the data
df_alg_perf = df_alg_perf[df_alg_perf['affective_model'] == 'dimensional']
df_alg_perf = df_alg_perf[df_alg_perf['is_classifier'].isin(['x', 'X'])]
df_alg_perf = df_alg_perf[df_alg_perf['class_model_output_categories'].isin(['HA, LA', 'HV, LV', 'LA, HA', 'LV, HV'])]
df_alg_perf['class_model_output_categories'] = df_alg_perf['class_model_output_categories'].replace(['LA, HA', 'LV, HV'], ['HA, LA', 'HV, LV'])

#%%
# Remove duplicate records in df_participants and df_performances
df_participants_unique = df_participants[['paper_id', 'N']].drop_duplicates(subset=['paper_id'])
df_performances_unique = df_performances[['paper_id', 'accuracy']].drop_duplicates(subset=['paper_id'])

# Merge the data
df_merged = df_alg_perf.merge(df_participants_unique, on='paper_id', how='left')
df_merged = df_merged.merge(df_performances_unique, on='paper_id', how='left')

#%%
# Save the merged dataframe as an Excel file
df_merged.to_excel('./data/df_merged.xlsx', index=False)

#%%
valence_models = df_merged[df_merged['class_model_output_categories'] == 'HV, LV']
arousal_models = df_merged[df_merged['class_model_output_categories'] == 'HA, LA']

# Add a temporary 'key' column to both valence and arousal models dataframes for the cross join
valence_models = valence_models.assign(key=1)
arousal_models = arousal_models.assign(key=1)

# Merge valence and arousal models using a cross join within each paper
merged_models = pd.merge(valence_models, arousal_models, on=['paper_id', 'key'])

# Drop the temporary 'key' column
merged_models = merged_models.drop(columns=['key'])

# Keep only the relevant columns
merged_models = merged_models[[
    'paper_id', 'model_id_x', 'apa_citation_x', 'year_x', 'affective_model_x', 'is_classifier_x',
    'class_model_output_number_x', 'class_model_output_categories_x', 'N_x', 'accuracy_x',
    'model_id_y', 'class_model_output_number_y', 'class_model_output_categories_y', 'N_y', 'accuracy_y'
]]

# Rename columns
merged_models.columns = [
    'paper_id', 'model_id_valence', 'apa_citation', 'year', 'affective_model', 'is_classifier',
    'class_model_output_number_valence', 'class_model_output_categories_valence', 'N_valence', 'accuracy_valence',
    'model_id_arousal', 'class_model_output_number_arousal', 'class_model_output_categories_arousal', 'N_arousal', 'accuracy_arousal'
]

# Group by paper_id and model_id_valence, and generate comparison_model_id
merged_models['comparison_model_id'] = merged_models.groupby(['paper_id', 'model_id_valence']).cumcount() + 1

#%%
# Convert non-numeric values to NaN
merged_models['accuracy_arousal'] = pd.to_numeric(merged_models['accuracy_arousal'], errors='coerce')
merged_models['accuracy_valence'] = pd.to_numeric(merged_models['accuracy_valence'], errors='coerce')

#%%
# Filter rows with numeric values in both columns
filtered_models = merged_models.dropna(subset=['accuracy_arousal', 'accuracy_valence'])

filtered_models.to_excel('./data/df_merged_2.xlsx', index=False)


#%%
# Print the data types of the columns in the filtered_models dataframe
print(filtered_models.dtypes)

# Convert necessary columns to numeric types
filtered_models['N_arousal'] = pd.to_numeric(filtered_models['N_arousal'], errors='coerce')
filtered_models['N_valence'] = pd.to_numeric(filtered_models['N_valence'], errors='coerce')
filtered_models['accuracy_arousal'] = pd.to_numeric(filtered_models['accuracy_arousal'], errors='coerce')
filtered_models['accuracy_valence'] = pd.to_numeric(filtered_models['accuracy_valence'], errors='coerce')

# Drop any rows with missing values
filtered_models = filtered_models.dropna(subset=['N_arousal', 'N_valence', 'accuracy_arousal', 'accuracy_valence'])


#%%
# Group the data by paper_id and calculate the standard deviation for arousal and valence
grouped_sd = filtered_models.groupby('paper_id').agg({'accuracy_arousal': 'std', 'accuracy_valence': 'std'}).reset_index()

# Rename the columns
grouped_sd.columns = ['paper_id', 'SD_arousal', 'SD_valence']

# Merge the grouped_sd DataFrame with the filtered_models DataFrame on the paper_id column
filtered_models = filtered_models.merge(grouped_sd, on='paper_id', how='left')

#%%
import numpy as np
import pandas as pd
from scipy import stats
import plotly.graph_objects as go

# Assuming 'filtered_models' is the DataFrame containing your data

# Calculate the effect size for each model
filtered_models['effect_size'] = filtered_models['accuracy_arousal'] - filtered_models['accuracy_valence']
filtered_models['variance'] = (1 / filtered_models['N_arousal']) + (1 / filtered_models['N_valence'])

# Group models by paper_id and calculate the mean effect size and variance for each paper
grouped_models = filtered_models.groupby('paper_id').agg({'effect_size': 'mean', 'variance': 'mean'}).reset_index()

# Calculate the weights
grouped_models['weight'] = 1 / grouped_models['variance']

# Calculate the weighted mean effect size
weighted_mean_effect_size = np.sum(grouped_models['weight'] * grouped_models['effect_size']) / np.sum(grouped_models['weight'])

# Calculate the variance of the weighted mean effect size
variance_weighted_mean_effect_size = 1 / np.sum(grouped_models['weight'])

# Calculate the standard error and confidence interval of the weighted mean effect size
standard_error = np.sqrt(variance_weighted_mean_effect_size)
critical_value = stats.norm.ppf(0.975)  # For a 95% confidence interval
lower_bound = weighted_mean_effect_size - critical_value * standard_error
upper_bound = weighted_mean_effect_size + critical_value * standard_error

# Print the results
print("Weighted mean effect size:", weighted_mean_effect_size)
print("95% Confidence interval:", (lower_bound, upper_bound))

# Add standard error, lower bound, and upper bound to the grouped_models DataFrame
grouped_models['standard_error'] = np.sqrt(grouped_models['variance'])
grouped_models['lower_bound'] = grouped_models['effect_size'] - critical_value * grouped_models['standard_error']
grouped_models['upper_bound'] = grouped_models['effect_size'] + critical_value * grouped_models['standard_error']


#%%
# Create a scatter plot for individual study effect sizes and confidence intervals
fig = go.Figure()

for index, row in grouped_models.iterrows():
    fig.add_trace(
        go.Scatter(
            x=[row["lower_bound"], row["upper_bound"]],
            y=[row["paper_id"], row["paper_id"]],
            mode="lines",
            showlegend=False,
            line=dict(color="blue"),
            name="Confidence Interval"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[row["effect_size"]],
            y=[row["paper_id"]],
            mode="markers",
            marker=dict(color="blue"),
            showlegend=False,
            name="Effect Size"
        )
    )

fig.add_shape(
    type="line",
    x0=weighted_mean_effect_size,
    x1=weighted_mean_effect_size,
    y0=-1,
    y1=len(grouped_models),
    yref="y",
    line=dict(color="red"),
    name="Overall Effect Size"
)

fig.update_layout(
    title="Forest Plot",
    xaxis_title="Effect Size",
    yaxis_title="Paper ID",
    yaxis=dict(autorange="reversed"),
    shapes=[dict(type='line', x0=0, x1=0, y0=-1, y1=len(grouped_models), yref="y", line=dict(color="black", dash='dash'), name="Line of No Effect")],
    legend=dict(
        x=1,
        y=1,
        traceorder="normal",
        font=dict(family="sans-serif", size=12),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=1
    )
)

fig.show()
# %%
