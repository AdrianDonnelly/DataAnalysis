import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mxmh_survey_results.csv")


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
genres = ['Frequency [Classical]', 'Frequency [EDM]', 'Frequency [Hip hop]', 'Frequency [Rock]', 'Frequency [Pop]']
mental_health_conditions = ['Anxiety', 'Depression', 'Insomnia', 'OCD']

# Heatmap of genre preference vs mental health conditions
data = df.groupby(mental_health_conditions)[genres].mean()
plt.figure(figsize=(12, 8))
sns.heatmap(data.T, cmap='coolwarm', annot=True)
plt.title('Music Preferences vs Mental Health Conditions')
plt.xlabel('Mental Health Conditions')
plt.ylabel('Genres')
plt.show()