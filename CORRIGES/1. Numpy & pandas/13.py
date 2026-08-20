# Exercice 13 — Séries temporelles
import pandas as pd
import numpy as np

dates = pd.date_range(start="2025-01-01",periods=90,freq="D")

valeur =  np.random.randint(10,150,90)

df = pd.DataFrame({
    "dates":dates,
    "valeur":valeur
})

print("Dataframme : \n",df)

donnees_fevrier = df[df['dates'].dt.month == 2]

print("Données du mois de fevrier : \n",donnees_fevrier)

moyenne_hebdo = df.set_index("dates").resample("W")["valeur"].mean()

print("Moyenne hebdo : \n",moyenne_hebdo)

df['day'] = df['dates'].dt.day_name()

df['variation'] = df["valeur"].diff()

df['moy_mob'] = df["valeur"].rolling(window=7).mean()

print("Dataframme : \n",df)




