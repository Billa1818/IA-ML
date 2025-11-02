import numpy as np # Importation de la bibliothèque NumPy
arr=np.arange(0,20) # Création d'un tableau 1D avec des entiers de 0 à 19
print("Tableau original :\n", arr) # Affichage du tableau original
new_arr=np.sort(arr[arr % 2 ==0]) # Tri des éléments impairs du tableau
print("Éléments pairs triés :\n", new_arr) # Affichage des éléments pairs triés
new_arr2=np.sort(arr[arr % 2 ==1])[::-1] # Tri des éléments impairs du tableau en ordre décroissant
print("Éléments impairs triés (ordre décroissant) :\n", new_arr2) # Affichage des éléments impairs triés
final_array=np.concatenate((new_arr, new_arr2)) # Combinaison des deux tableaux triés
print("Tableau final (pairs triés + impairs triés décroissants) :\n", final_array) # Affichage du tableau final