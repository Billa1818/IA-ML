# Exercice 17 — Calculs matriciels et réduction de dimension
import pandas as pd
import numpy as np


df = pd.DataFrame({
    'Mathématiques': [14.5, 12.0, 9.5, 18.0, 16.5],
    'Physique': [12.0, 15.5, 11.0, 17.5, 14.0],
    'Informatique': [18.5, 14.0, 15.0, 19.5, 17.0]
}, index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])


X = df.to_numpy()

X_centre = X - np.mean(X, axis=0)

matrice_cov = np.cov(X_centre, rowvar=False)

valeurs_propres, vecteurs_propres = np.linalg.eig(matrice_cov)

indices_tries = np.argsort(valeurs_propres)[::-1]

vecteurs_propres_tries = vecteurs_propres[:, indices_tries]

axes_principaux = vecteurs_propres_tries[:, :2]

donnees_projetees = np.dot(X_centre, axes_principaux)

df_pca = pd.DataFrame(donnees_projetees, columns=['PC1', 'PC2'], index=df.index)

print(df_pca)