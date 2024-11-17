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
genres = ['Frequency [Classical]', 'Frequency [EDM]', 'Frequency [Hip hop]', 'Frequency [Rock]', 'Frequency [Pop]']
mental_health_conditions = ['Anxiety', 'Depression', 'Insomnia', 'OCD']

frequency_mapping = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Frequently": 3,
    "Very frequently": 4
}

for genre in genres:
    df[genre] = df[genre].map(frequency_mapping).fillna(0)

# Plot 1: Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=20, color='blue')
plt.title('Age Distribution of Survey Participants')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Primary Streaming Service Usage
plt.figure(figsize=(10, 6))
df['Primary streaming service'].value_counts().plot(kind='bar', color='green')
plt.title('Primary Streaming Service Usage')
plt.xlabel('Streaming Service')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Plot 3: Favorite Genre Distribution
plt.figure(figsize=(12, 8))
df['Fav genre'].value_counts().plot(kind='bar', color='purple')
plt.title('Favorite Music Genres')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Plot 4: Mental Health and Genre Preference
# Reshape the data for the heatmap
heatmap_data = df[mental_health_conditions + genres].corr().loc[mental_health_conditions, genres]

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Music Preferences vs Mental Health Conditions')
plt.xlabel('Music Genres')
plt.ylabel('Mental Health Conditions')
plt.show()
