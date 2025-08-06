import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('netflix_titles.csv')
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['rating'] = df['rating'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['is_movie'] = df['type'].apply(lambda x: 1 if x == 'Movie' else 0)
df['is_tv_show'] = df['type'].apply(lambda x: 1 if x == 'TV Show' else 0)
