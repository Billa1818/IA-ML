# Exercice 7 — Performance et vectorisation
import numpy as np

from time import time

arr = np.random.normal(50,10,1000000)

deb= time()

som = 0 

for i in arr :

    som = som + i

fin = time()

print(" \n Python : ",fin-deb)

deb= time()

som = np.sum(arr)

fin = time()

print(" \n NumPy : ",fin-deb)