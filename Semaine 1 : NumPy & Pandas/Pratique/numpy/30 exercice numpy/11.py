import numpy as np # Importation de la bibliothèque NumPy
A=np.random.randint(low=1, high=20, size=(5, 5)) # Création d'un tableau 5x5 avec des entiers aléatoires de 1 à 20
print("Matrice A :\n", A) # Affichage de la matrice A
B=np.random.randint(low=1, high=20, size=(5, 5)) # Création d'un tableau 5x5 avec des entiers aléatoires de 1 à 20
print("Matrice B :\n", B) # Affichage de la matrice B
C=(A+B)*2 # Addition des matrices A et B, puis multiplication par 2
print("Matrice C ( (A + B) * 2 ) :\n", C) # Affichage de la matrice C
D=(((np.dot(A, A))+(np.dot(B, B)))**0.5 ) # Produit matriciel de A et B
print("Matrice D ( ((A . A) + (B . B)) ** 0.5 ) :\n", D) # Affichage de la matrice D
E=(A - B) / (A + B + 0.0001) # Soustraction de B à A, puis division par la somme de A et B (avec un petit décalage pour éviter la division par zéro)
print("Matrice E ( (A - B) / (A + B) ) :\n", E) # Affichage de la matrice E
