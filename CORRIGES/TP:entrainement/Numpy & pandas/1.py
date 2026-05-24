# Exercice 1
import numpy as np

arr1=np.arange(1,10)

arr2=np.zeros(5,dtype=float)

arr3=np.linspace(0,1,6)

arr4=np.eye(4)

print('\n Tableau 1.')
print(arr1)
print('Forme:',arr1.ndim)
print('Type:',arr2.dtype)

print('\n Tableau 2.')
print(arr2)
print('Forme:',arr3.ndim)
print('Type:',arr3.dtype)

print('\n Tableau 3.')
print(arr3)
print('Forme:',arr3.ndim)
print('Type:',arr3.dtype)

print('\n Tableau 4.')
print(arr4)
print('Forme:',arr4.ndim)
print('Type:',arr4.dtype)