import numpy as np # Importation de la bibliothèque NumPy
tabl3d=np.random.randint(
    low=10, high=50, size=(4,5,6)
) # Création d'un tableau 3D aléatoire de dimensions 4x5x6 avec des entiers entre 10 et 50
print("Tableau 3D original :\n", tabl3d) # Affichage
print("\n") # Saut de ligne pour la lisibilité
print('Forme:', tabl3d.shape) # Affichage de la forme du tableau
print('Nombre de dimensions:', tabl3d.ndim) # Affichage du nombre de dimensions
print('Nombre total d\'éléments:', tabl3d.size) # Affichage du nombre total d'éléments
print('Type de données des éléments:', tabl3d.dtype) # Affichage du type de données des éléments
print('Taille en octets d\'un élément:', tabl3d.itemsize) # Affichage de la taille en octets d'un élément
print('Taille totale en octets du tableau:', tabl3d.nbytes) # Affichage de la taille totale en octets du tableau
