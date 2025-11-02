import numpy as np # Importation de la bibliothèque NumPy
taille =8
mat8x8=np.zeros((taille, taille), dtype=int) # Création d'une matrice 8x8 remplie de zéros
mat8x8[1::2, ::2] = 1 # Remplissage des cases noires
mat8x8[::2, 1::2] = 1 # Remplissage des cases blanches
print(mat8x8) # Affichage de la matrice
