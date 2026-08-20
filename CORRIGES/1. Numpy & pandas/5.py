# Exercice 5 — Algèbre linéaire
import numpy as np

arr = np.random.randint(4,16,(3,3)) # Génère un tableau 3x3 avec des valeurs aléatoires entre 4 et 15

print(arr)

inverse = np.linalg.inv(arr) # Calcule l'inverse de la matrice 3x3

det =  np.linalg.det(arr) # Calcule le déterminant de la matrice 3x3

A = [[2,1],[5,3]]  

B = [8,13]

C = [[2,1,4],[5,5,3],[5,5,3]] 

X = np.linalg.solve(A,B) # Résout le système d'équations linéaires Ax = B

valP,vecP = np.linalg.eig(C) # Calcule les valeurs propres et les vecteurs propres de la matrice C

 