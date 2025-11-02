import numpy as np # Importation de la bibliothèque NumPy
tab=np.arange(1,121) # Création d'un tableau 1D avec des entiers de 1 à 120
print("Tableau original :\n", tab) # Affichage du tableau original
tab=tab.reshape(10,12) # Reshape du tableau en 2D (10 lignes, 12 colonnes)
print("Tableau reshaped (10x12) :\n", tab) # Affichage du tableau reshaped
tab=tab.reshape((3,5,8)) # Reshape du tableau en 3D (3 blocs, 5 lignes, 8 colonnes)
print("Tableau reshaped (3x5x8) :\n", tab) # Affichage du tableau reshaped
tab=tab.reshape(2,-1) # Reshape du tableau en 2D avec 2 lignes et un nombre de colonnes calculé automatiquement
print("Tableau reshaped (2x - auto ) :\n", tab) # Affichage du tableau reshaped