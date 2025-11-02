import numpy as np

# 1️⃣ Création du vecteur colonne (5x1)
vecteur_colonne = np.array([[10], [20], [30], [40], [50]])

# 2️⃣ Création du vecteur ligne (1x4)
vecteur_ligne = np.array([1, 2, 3, 4])

print("Vecteur colonne (forme):", vecteur_colonne.shape)
print(vecteur_colonne)
print("\nVecteur ligne (forme):", vecteur_ligne.shape)
print(vecteur_ligne)

# 3️⃣ Broadcasting pour obtenir toutes les combinaisons de produits
matrice_produits = vecteur_colonne * vecteur_ligne

print("\nMatrice des produits (5x4):")
print(matrice_produits)

# 4️⃣ Ajout d’un vecteur ligne [100, 200, 300, 400]
vecteur_ajout = np.array([100, 200, 300, 400])
matrice_finale = matrice_produits + vecteur_ajout

print("\nMatrice finale après ajout du vecteur :")
print(matrice_finale)
