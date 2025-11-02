import numpy as np # Importation de la bibliothèque NumPy
arr=np.arange(100) # Création d'un tableau NumPy avec des valeurs de 0 à 99
print("Tableau initial :", arr)
arr=arr.reshape(10,10) # Reshape le tableau en une matrice 10x10
print("Matrice 10x10 :\n", arr)
ligne5=arr[4,:] # Extraction de la 5ème ligne (index 4)
print("5ème ligne :", ligne5)
colonne3=arr[:,2] # Extraction de la 3ème colonne (index 2)
print("3ème colonne :", colonne3)
somme_ligne=np.sum(arr, axis=1) # Calcul de la somme de chaque ligne
print("Somme de chaque ligne :", somme_ligne)
moyenne_colonne=np.sum(arr, axis=0) # Calcul de la somme de chaque colonne
print("Somme de chaque colonne :", moyenne_colonne)