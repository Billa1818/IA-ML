import numpy as np # Importation de la bibliothèque NumPy
A=np.random.randint(1,10,(3,3)) # Création d'une matrice 3x3 avec des entiers aléatoires entre 1 et 10
B=np.random.randint(1,10,(3,3)) # Création d'une matrice 3x3 avec des entiers aléatoires entre 1 et 10
produit_scalaire=np.dot(A,B) # Calcul du produit scalaire des matrices A et B
print("Matrice A:\n",A) # Affichage de la matrice A
print("Matrice B:\n",B) # Affichage de la matrice B
print("Produit scalaire de A et B:\n",produit_scalaire) # Affichage du produit scalaire
inverse_A=np.linalg.inv(A) # Calcul de l'inverse de la matrice A
print("Inverse de la matrice A:\n",inverse_A) # Affichage de l'inverse de la matrice A
verification_identite=np.dot(A,inverse_A) # Vérification que le produit de A et son inverse donne la matrice identité
mat_indentity=np.eye(3) # Création de la matrice identité 3x3
if np.allclose(verification_identite, mat_indentity): # Vérification de l'égalité avec une tolérance
    print("La vérification est réussie: A * A_inv = I") # Message de succès
else:
    print("La vérification a échoué") # Message d'échec
valeur_propres, vecteurs_propres=np.linalg.eig(A) # Calcul des valeurs propres et des vecteurs propres de la matrice A
print("Valeurs propres de A:\n",valeur_propres) # Affichage des valeurs propres
print("Vecteurs propres de A:\n",vecteurs_propres) # Affichage des vecteurs propres