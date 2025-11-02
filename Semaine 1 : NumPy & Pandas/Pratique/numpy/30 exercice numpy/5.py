import numpy as np # Importation de la bibliothèque NumPy
tab10x10=np.random.randint(
    low=0,high=100,size=(10,10)) # Création d'un tableau 10x10 avec des entiers aléatoires entre 0 et 100
print("Tableau 10x10 original :\n", tab10x10) # Affichage du tableau original
diadonal=np.diag(tab10x10) # Extraction de la diagonale principale et création d'un nouveau tableau avec uniquement cette diagonale
print(" Diagonale principale :\n", diadonal) # Affichage du tableau avec uniquement la diagonale principale
inversion=tab10x10[:,::-1]
diadonal_2nd=np.diag(inversion) # Extraction de la deuxième diagonale et création d'un nouveau tableau avec uniquement cette diagonale
print("Deuxième diagonale :\n", diadonal_2nd) # Affichage du tableau avec uniquement la deuxième diagonale
tab4x4=tab10x10[2:6,2:6] # Extraction d'un sous-tableau 4x4 à partir du tableau original
print("Sous-tableau 4x4 (lignes 2 à 5 et colonnes 2 à 5) :\n", tab4x4) # Affichage du sous-tableau 4x4