import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("mxmh_survey_results.csv")

# Handle missing values
df.fillna(0, inplace=True)

# Ensure Age is numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Convert genre frequencies to numeric values
genres = ['Classical', 'EDM', 'Hip hop', 'Rock', 'Pop']
mental_health_conditions = ['Anxiety', 'Depression', 'Insomnia', 'OCD']

df.rename(columns={
    'Frequency [Classical]': 'Classical',
    'Frequency [EDM]': 'EDM',
    'Frequency [Hip hop]': 'Hip hop',
    'Frequency [Rock]': 'Rock',
    'Frequency [Pop]': 'Pop'
}, inplace=True)

frequency_mapping = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Frequently": 3,
    "Very frequently": 4
}

for genre in ['Classical', 'EDM', 'Hip hop', 'Rock', 'Pop']:
    df[genre] = df[genre].map(frequency_mapping).fillna(0)
# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 16))  # 2x2 grid of plots

# Plot 1: Age Distribution
sns.histplot(df['Age'], kde=True, bins=20, color='blue', ax=axs[0, 0])
axs[0, 0].set_title('Age Distribution of Survey Participants')
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('Frequency')

# Plot 2: Primary Streaming Service Usage
df['Primary streaming service'].value_counts().plot(kind='pie',
    startangle=90,
    ax=axs[0, 1],
    colormap='viridis')
axs[1, 0].set_title('Streaming Service')
axs[1, 0].set_ylabel('')

# Plot 3: Favorite Genre Distribution
df['Fav genre'].value_counts().plot(kind='bar', color='purple', ax=axs[1, 0])
axs[1, 0].set_title('Favorite Music Genres')
axs[1, 0].set_xlabel('Genre')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].tick_params(axis='x', rotation=45)

# Plot 4: Mental Health and Genre Preference Heatmap
heatmap_data = df[mental_health_conditions + genres].corr().loc[mental_health_conditions, genres]
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".2f", ax=axs[1, 1])
axs[1, 1].set_title('Music Preferences vs Mental Health Conditions')
axs[1, 1].set_xlabel('Music Genres')
axs[1, 1].set_ylabel('Mental Health Conditions')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()
