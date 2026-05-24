# Exercice 2
import numpy as np

mat=np.arange(10,100,10).reshape(3,3)

print("Matrice :")


print("Matrice original : \n",mat)

lin2= mat[1]

print("2ème ligne de la matrice : \n",lin2)

col3 = mat[:,2]

print("3ème collone : \n",col3)

mat_botom_r=mat[1:,1:]

print("Matrice 2x2 en bas a droit : \n",mat_botom_r)

elm_sup_45= mat[mat>45]

print("Element superieur a 45: \n",elm_sup_45)

mat[mat%2==0]=0

print("Matrice avec tout les element paire remplacer par 0 \n",mat)

