# Exercice 2 — Barres et camembert
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

departements = [
    "Alibori", "Atacora", "Atlantique", "Borgou", 
    "Collines", "Couffo", "Donga", "Littoral", 
    "Mono", "Ouémé", "Plateau", "Zou"
]

ventes = np.random.randint(500,500000,12)

df = pd.DataFrame({"departement":departements,"ventes":ventes})

fig , ax = plt.subplots(1,2,figsize=(8, 6))

ax[0].barh(df["departement"],df["ventes"])

vente_max = ventes.argmax()

decale = np.zeros(len(df["departement"]))

decale[vente_max] = 0.25

ax[1].pie(df["ventes"],labels=df["departement"],explode=decale,autopct='%1.0f%%')

plt.show()

