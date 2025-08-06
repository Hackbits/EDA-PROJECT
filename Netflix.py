import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('netflix_titles.csv')
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year.fillna(0).astype(int) 
df['rating'] = df['rating'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['is_movie'] = df['type'].apply(lambda x: 1 if x == 'Movie' else 0)
df['is_tv_show'] = df['type'].apply(lambda x: 1 if x == 'TV Show' else 0)
plt.figure(figsize=(12, 6))
sns.set_style('whitegrid')
growth_data = df.groupby('year_added')['type'].value_counts().unstack().fillna(0)
growth_data.plot(kind='bar', stacked=True, color=["#0061ff", "#60efff"])
plt.title('Netflix Content Over Time (Movies vs TV Shows)', fontsize=14)
plt.xlabel('Years', fontsize=12)
plt.ylabel('Number of Shows/Movies', fontsize=12)
plt.legend(title='Content Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()