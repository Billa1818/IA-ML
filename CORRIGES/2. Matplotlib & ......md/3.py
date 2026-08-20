# Exercice 4 — Histogramme et distribution
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

age = np.random.randint(18, 66, 200)
salaire = np.random.uniform(500, 15000, 200)

df = pd.DataFrame({"age": age, "salaire": salaire.round(0)})

def cat(valeur):
    if valeur <= 1500:
        return "Junior"
    elif valeur <= 7000:
        return "Confirmé"
    else: 
        return "Senior"

df["categorie"] = df["salaire"].apply(cat)

# Préparation de la figure
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

couleurs = {'Junior': 'limegreen', 'Confirmé': 'dodgerblue', 'Senior': 'crimson'}

for nom_cat in ['Junior', 'Confirmé', 'Senior']:

    df_filtre = df[df["categorie"] == nom_cat]
    
    ax[0].scatter(df_filtre["age"], df_filtre["salaire"], color=couleurs[nom_cat], label=nom_cat)

ax[0].set_title("Répartition des salaires")
ax[0].set_xlabel("Âge")
ax[0].legend()

ax[1].scatter(df["age"], df["salaire"], color="lightgray")

coefficients = np.polyfit(df["age"], df["salaire"], 1)
a = coefficients[0]
b = coefficients[1]

x_ligne = np.array([df["age"].min(), df["age"].max()])
y_ligne = a * x_ligne + b

ax[1].plot(x_ligne, y_ligne, color="black", linewidth=2, linestyle="--", label="Tendance")

ax[1].set_title("Corrélation globale")
ax[1].set_xlabel("Âge")
ax[1].legend()

plt.tight_layout()
plt.show()