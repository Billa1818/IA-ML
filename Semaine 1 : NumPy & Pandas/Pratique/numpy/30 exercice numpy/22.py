import numpy as np

matrice = np.random.randint(1, 101, size=(10, 10))
print("Matrice originale :\n", matrice)

result = np.where(matrice < 30, -1, np.where(matrice > 70, 1, 0))
print("\nMatrice transformée :\n", result)

nb_petits = np.sum(result == -1)
nb_moyens = np.sum(result == 0)
nb_grands = np.sum(result == 1)
print(f"\nCatégorie -1 (< 30) : {nb_petits} éléments")
print(f"Catégorie 0 (30-70) : {nb_moyens} éléments")
print(f"Catégorie 1 (> 70) : {nb_grands} éléments")
