# Exercice 2 — Indexation et slicing
import numpy as np

arr = np.arange(10,91,10).reshape(3,3) # Tableau 3x3 de valeurs de 10 à 90, espacées de 10

print(arr)

ligne2 = arr[1] # Extraction de la 2ème ligne du tableau (index 1)

print(ligne2)

ligne3 = arr[:,1] # Extraction de la 3ème colonne du tableau (index 2)

print(ligne3) 

mat2x2 = arr[1:, 1:] # Extraction d'un sous-tableau 2x2 à partir de la 2ème ligne et de la 2ème colonne

print(mat2x2) 

elmSup45 = arr[arr > 45] # Extraction des éléments du tableau supérieurs à 45

print(elmSup45)

arr[arr % 2 == 0 ] = 0 # Remplacement des éléments pairs du tableau par 0

print(arr)