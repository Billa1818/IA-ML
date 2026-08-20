# Exercice 19 — Pipeline complet sur données capteurs

import pandas as pd
import numpy as np

np.random.seed(42)

dates_possibles = pd.date_range(start="2026-08-01", periods=504, freq="h")
dates_choisies = np.random.choice(dates_possibles, size=500, replace=False)

df = pd.DataFrame({
    'date_heure': dates_choisies,
    'capteur': np.random.choice(['Capteur_A', 'Capteur_B', 'Capteur_C'], size=500),
    'temperature': np.random.normal(loc=22, scale=4, size=500), # Température moyenne de 22°C
    'humidite': np.random.normal(loc=55, scale=8, size=500),    # Humidité moyenne de 55%
    'pression': np.random.normal(loc=1013, scale=5, size=500)   # Pression atmosphérique
})

idx_outliers = df.sample(frac=0.05, random_state=42).index
df.loc[idx_outliers, 'temperature'] += np.random.choice([-50, 50], size=len(idx_outliers))

idx_nan = df.sample(frac=0.10, random_state=99).index
df.loc[idx_nan, 'humidite'] = np.nan

Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1
limite_basse = Q1 - 1.5 * IQR
limite_haute = Q3 + 1.5 * IQR

df['temperature'] = df['temperature'].clip(lower=limite_basse, upper=limite_haute)

df['humidite'] = df['humidite'].fillna(
    df.groupby('capteur')['humidite'].transform('median')
)

df['jour'] = df['date_heure'].dt.date

df_agrege = df.groupby(['capteur', 'jour'])[['temperature', 'humidite', 'pression']].mean().reset_index()

moyenne_temp = df_agrege['temperature'].mean()
std_temp = df_agrege['temperature'].std()

df_agrege['z_score_temp'] = (df_agrege['temperature'] - moyenne_temp) / std_temp

df_agrege.to_csv('releves_journaliers_capteurs.csv', index=False)

print("Le traitement est terminé. Le fichier 'releves_journaliers_capteurs.csv' a été généré.")
print("\nAperçu des données finales :")
print(df_agrege.head())
