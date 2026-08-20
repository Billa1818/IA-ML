# Exercice 4 — Reshaping et manipulation de forme
import numpy as np

arr = np.arange(1,13) # Valeur consecutive de 1 à 12

print(arr)

reshape3x4 = arr.reshape(3,4) # Reshape le tableau en une matrice 3x4

print(reshape3x4)

reshape2x6 = arr.reshape(2,6) # Reshape le tableau en une matrice 2x6

print(reshape2x6)

transpose = reshape3x4.T # Transpose de la matrice 3x4, ce qui donne une matrice 4x3

print(transpose)

tab1 = np.array([4,5,2,1]) 

tab2 = np.array([1,3,2,1])

concat = np.concatenate((tab1,tab2),axis=0) # Concatenation des deux tableaux en un seul tableau 1D

print(concat)

empliH = np.hstack((tab1,tab2)) # Empilement horizontal des deux tableaux, ce qui donne un tableau 1D

empliV = np.vstack((tab1,tab2)) # Empilement vertical des deux tableaux, ce qui donne une matrice 2x4

tab3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

reshape3d = tab3.reshape(-1) # Aplatit le tableau 3D en un tableau 1D

print(reshape3d)