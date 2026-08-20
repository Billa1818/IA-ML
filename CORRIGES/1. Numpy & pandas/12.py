# Exercice 12 — Jointures
import pandas as pd

# Création du DataFrame clients
clients = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'nom': ['Alice', 'Bob', 'Charlie', 'David']
})

# Création du DataFrame commandes
commandes = pd.DataFrame({
    'id_commande': [101, 102, 103, 104],
    'id': [1, 2, 1, 5], 
    'montant': [150.0, 200.0, 350.0, 120.0]
})

nouveaux_clients = pd.DataFrame({
    'id': [5, 6],
    'nom': ['Eve', 'Frank']
})

print("Client : \n",clients)

print("Commande : \n",commandes)

df = pd.merge(clients,commandes,on="id",how="inner")

print("Client ayant au moin une commande :\n",df)

df = pd.merge(clients,commandes,on="id",how="left")

print("Liste de tout les client  :\n",df)

df = pd.merge(clients,commandes,on="id",how="outer")

print("Liste de tout les client et commande  :\n",df)

ndf = pd.concat([clients,nouveaux_clients],ignore_index=True)

print("Fusion des dataframme  :\n",df)