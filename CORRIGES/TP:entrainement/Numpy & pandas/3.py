# Exercice 3
import numpy as np

tab=np.arange(1,6)

print("Tableau : \n",tab)

tab_1=tab*2

print("Tableau avec scalaire sans boucle: \n",tab_1)

tab_2= tab*tab

print("Tableau au carré sans boucle: \n",tab_2)

tab_3 = (tab - tab.min()) / (tab.max() - tab.min())

print("Normalisation: \n",tab_3)

mat_random= np.random.randint(1,10,(3,4))

print("Matrice aleatoire: \n",mat_random)

moy_lin= mat_random.mean(axis=0)

print("La moyenne par ligne est de : ",moy_lin)

moy_col= mat_random.mean(axis=1)

print("La moyenne par colonne est de : ",moy_col)

std= mat_random.std()

print(std)