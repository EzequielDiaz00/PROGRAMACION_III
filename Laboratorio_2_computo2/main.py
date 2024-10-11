import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Ezequiel\Arashi\Documentos\UGB\Ciclo II-2024\Lab2C2\champions.csv")

print(df.head())

# --- Gráfico de barras ---
# Mostrar el daño de ataque base de los campeones
plt.figure(figsize=(10,6))
top_attack_damage = df[['Champion Name', 'Base Attack Damage']].sort_values(by='Base Attack Damage', ascending=False).head(10)
sns.barplot(x='Champion Name', y='Base Attack Damage', data=top_attack_damage)
plt.title('Top 10 Campeones por Daño de Ataque Base')
plt.ylabel('Daño de Ataque Base')
plt.xticks(rotation=90)
plt.show()

# --- Gráfico de líneas ---
# Comparar la salud base de los campeones
plt.figure(figsize=(10,6))
top_health = df[['Champion Name', 'Base Health']].sort_values(by='Base Health', ascending=False).head(10)
sns.lineplot(x='Champion Name', y='Base Health', data=top_health, marker='o')
plt.title('Top 10 Campeones por Salud Base')
plt.ylabel('Salud Base')
plt.xticks(rotation=90)
plt.show()

# --- Gráfico circular ---
# Distribución de roles entre los campeones
role_distribution = df['Role'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(role_distribution, labels=role_distribution.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Roles de los Campeones')
plt.show()
