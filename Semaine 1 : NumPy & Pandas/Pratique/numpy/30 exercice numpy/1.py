import numpy as np # importation de numpy
arr_5x5=np.zeros((5, 5), dtype=int)
print('Tableau 5x5 de zéros entiers:')
print(arr_5x5)
arr_5x5[0,:] = 1 # première ligne à 1
arr_5x5[:,0]=1 # première colonne à 1
arr_5x5[-1,:] = 1 # dernière ligne à 1
arr_5x5[:,-1]=1 # dernière colonne à 1
print('Tableau avec une bordure :')
print(arr_5x5)