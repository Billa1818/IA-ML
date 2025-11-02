import numpy as np # Importation de la bibliothèque NumPy
mat8x12=np.random.randint(-50,50,size=(8,12)) # Création d'un tableau 8x12 avec des entiers aléatoires de -50 à 50
print("Tableau original :\n", mat8x12) # Affichage du tableau
X_min = mat8x12.min(axis=0)
# Calculer les valeurs maximales de chaque colonne (X_max)
X_max = mat8x12.max(axis=0)
# Calculer l'étendue (X_max - X_min)
X_range = X_max - X_min
# Gérer le cas de la division par zéro (si une colonne est constante)
# Si X_range est 0, on le remplace par 1. Le résultat de cette colonne sera 0.
X_range = np.where(X_range == 0, 1, X_range)
# Appliquer la formule de normalisation (Broadcasting automatique)
matrice_normalisee = (mat8x12 - X_min) / X_range
print("Matrice normalisée :\n", matrice_normalisee) # Affichage de la matrice normalisée
# Statistiques de la matrice normalisée
mean_normalized = matrice_normalisee.mean()
std_normalized = matrice_normalisee.std()
print("Moyenne de la matrice normalisée :", mean_normalized) # Affichage de la moyenne
print("Écart type de la matrice normalisée :", std_normalized)