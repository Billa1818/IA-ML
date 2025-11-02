import numpy as np # Importation de la bibliothèque NumPy
matA=np.arange(0,24,2).reshape(3,4) # Création de la matrice A (3x4) avec des entiers de 0 à 23
print("Matrice A :\n", matA) # Affichage de la matrice A
matB=np.arange(0,36,3).reshape(3,4) # Création de la matrice B (3x4) avec des entiers de 0 à 35
print("Matrice B :\n", matB) # Affichage de la matrice B
matC=np.arange(0,60,5).reshape(3,4) # Création de la matrice C (3x4) avec des entiers de 0 à 59
print("Matrice C :\n", matC) # Affichage de la matrice C
mat_enpileV=np.vstack((matA,matB,matC)) # Empilement vertical des matrices A, B et C pour créer une nouvelle matrice (9x4)
print("Matrice empilée (A, B, C) :\n", mat_enpileV) # Affichage de la matrice empilée
mat_enpileH=np.hstack((matA,matB,matC)) # Empilement horizontal des matrices A, B et C pour créer une nouvelle matrice (3x12)
print("Matrice empilée horizontalement (A, B, C) :\n", mat_enpileH) # Affichage de la matrice empilée horizontalement   
empile_profondeur=np.dstack((matA,matB,matC)) # Empilement en profondeur des matrices A, B et C pour créer une nouvelle matrice (3x4x3)
print("Matrice empilée en profondeur (A, B, C) :\n", empile_profondeur) # Affichage de la matrice empilée en profondeur