# Exercice 11 — GroupBy et agrégations
import pandas as pd

data = {
    'région': ['Nord', 'Sud', 'Nord', 'Est', 'Sud', 'Nord', 'Est', 'Sud'],
    'vendeur': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David', 'Charlie', 'Eve'],
    'mois': ['Janvier', 'Janvier', 'Février', 'Janvier', 'Février', 'Mars', 'Mars', 'Mars'],
    'montant': [1500, 2000, 1200, 3000, 1800, 1100, 2500, 1900]
}

df = pd.DataFrame(data)

print("Dataframe :\n",df)

total_par_region = df.groupby(["région"]).sum()

print("Total par region :\n",total_par_region)

moy_par_vendeur = df.groupby("vendeur")["montant"].agg(["mean","sum","count"])

print(moy_par_vendeur)

tableau_croise = df.pivot_table(values='montant', index='mois', columns='région', aggfunc='sum', fill_value=0)

print("\n",tableau_croise)

df['pourcentage_region'] = (df['montant'] / df.groupby('région')['montant'].transform('sum')) * 100

print(df)


