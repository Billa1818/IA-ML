# Exercice 3 — Opérations et broadcasting
import numpy as np

arr = np.arange(1,6) # Tableau de 5 valeurs de 1 à 5

print(arr)

arr =  arr + 10 # Addition scalaire : chaque élément du tableau est incrémenté de 10

print(arr)

arr = arr ** 2 # Élément par élément : chaque élément du tableau est élevé au carré

print(arr)
 
arr = (arr - arr.min()) / (arr.max() - arr.min()) # Normalisation : chaque élément du tableau est normalisé entre 0 et 1

print(arr)

mat3x4 = np.random.randint(10,51,12).reshape(3,4) # Création d'une matrice 3x4 de valeurs aléatoires entre 10 et 50

print(mat3x4)

moyenneLigne = np.mean(mat3x4,axis=1) # Calcul de la moyenne de chaque ligne de la matrice

print(np.mean(mat3x4,axis=1)) # Affichage de la moyenne de chaque ligne

print(np.mean(mat3x4,axis=0)) # Calcul de la moyenne de chaque colonne de la matrice

print(np.std(mat3x4)) # Calcul de l'écart type de tous les éléments de la matrice
