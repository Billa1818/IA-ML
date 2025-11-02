import numpy as np # Importation de la bibliothèque NumPy
random_array = np.random.randint(0,100,100) # Création d'un tableau 1D avec 100 entiers aléatoires entre 0 et 100
print("Tableau original :\n", random_array) # Affichage du tableau original
multiple3=random_array[(random_array % 3 ==0) & (random_array >50)] # Filtrage des éléments qui sont des multiples de 3
print("Éléments multiples de 3 et > 50 :\n", multiple3) # Affichage des éléments multiples de 3
compteur = multiple3.size # Comptage du nombre d'éléments dans le tableau filtré
print("Nombre d'éléments multiples de 3 et > 50 :", compteur) # Affichage du nombre d'éléments multiples de 3