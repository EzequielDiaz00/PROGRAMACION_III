# Programa para graficas de Campeones de League of Legends, Artistas y Peliculas
# Datasets usados:
#   https://www.kaggle.com/datasets/dem0nking/league-of-legends-champions-dataset
#   https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
#   https://www.kaggle.com/datasets/pieca111/music-artists-popularity

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datasets
df = pd.read_csv(r"champions.csv")
df1 = pd.read_csv(r"artists.csv")
df2 = pd.read_csv(r"imdb_top_1000.csv")

# print(df.head())

# --- Gráfico de barras ---
# Mostrar los 10 artistas más populares
plt.figure(figsize=(10, 6))
top_artists = df1[['artist_lastfm', 'listeners_lastfm']].sort_values(by='listeners_lastfm', ascending=False).head(10)
sns.barplot(x='artist_lastfm', y='listeners_lastfm', data=top_artists)
plt.title('Top 10 Artistas Más Populares')
plt.ylabel('Número de Oyentes')
plt.xlabel('Artista')
plt.xticks(rotation=90)
plt.show()

# --- Gráfico de líneas ---
# Popularidad de las películas a lo largo de los años
plt.figure(figsize=(12, 6))
top_movies = df2[['Series_Title', 'IMDB_Rating', 'Released_Year']].sort_values(by='IMDB_Rating', ascending=False).head(10)
sns.lineplot(x='Series_Title', y='IMDB_Rating', data=top_movies, marker='o')
plt.title('Top 10 Películas por Popularidad (IMDB Rating)')
plt.ylabel('Calificación IMDB')
plt.xlabel('Pelicula')
plt.xticks(rotation=45)
plt.show()

# --- Gráfico circular ---
# Distribución de roles entre los campeones de League of Legends
role_distribution = df['Role'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(role_distribution, labels=role_distribution.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Roles de los Campeones de League of Legends')
plt.show()
