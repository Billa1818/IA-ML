# Exercice 1 — Création de tableaux
import numpy as np

arr1 = np.arange(1,10) # Tableau de 9 valeurs de 1 à 9

print("\n\n",arr1," Forme:",arr1.shape," Type:",arr1.dtype)

arr2 = np.zeros(5,dtype=float) # Tableau de 5 valeurs initialisées à 0.0

print("\n\n",arr2," Forme:",arr2.shape," Type:",arr2.dtype)

arr3 = np.linspace(0,1,6) # 6 valeurs entre 0 et 1, espacées de manière égale

print("\n\n",arr3," Forme:",arr3.shape," Type:",arr3.dtype)

arr4 = np.ones((4, 4)) # Tableau 4x4 de valeurs initialisées à 1.0

print("\n\n",arr4," Forme:",arr4.shape," Type:",arr4.dtype)
