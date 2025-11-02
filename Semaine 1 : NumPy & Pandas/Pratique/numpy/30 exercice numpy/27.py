import numpy as np

matrice = np.random.randint(0, 101, size=(10, 10))
print("Matrice :\n", matrice)

# Indices des lignes et colonnes
lignes = np.arange(10).reshape(-1, 1)
colonnes = np.arange(10)

# Condition 1 : pairs ET lignes impaires
cond1 = (matrice % 2 == 0) & (lignes % 2 == 1)

# Condition 2 : divisibles par 5 ET colonnes paires
cond2 = (matrice % 5 == 0) & (colonnes % 2 == 0)

# Masque final
masque = cond1 | cond2

nb_elements = np.sum(masque)
somme = np.sum(matrice[masque])
print(f"\nNombre d'éléments satisfaisant les conditions : {nb_elements}")
print(f"Somme de ces éléments : {somme}")
