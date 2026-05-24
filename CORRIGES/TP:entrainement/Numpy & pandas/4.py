# exercice 4
import numpy as np

tab=np.arange(1,13)

print("Tableau initial : \n",tab)

tab3x4=tab.reshape(3,4)

print("Tableau après rechape 3x4 : \n",tab3x4)

tab2x3=tab.reshape(2,6)

print("Tableau après rechape 3x4 : \n",tab2x3)

transpo_v1=tab3x4.T

print('Transposé de v1:\n',transpo_v1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a= ",a)
print("b= ",b)
ab=np.concatenate((a,b))

print("concatenation de a & b",ab)


emp_h=np.hstack((a,b))

emp_v=np.vstack((a,b))

print("enpil.. H \n",emp_h)

print("enpil.. V \n",emp_v)

tab3x3=np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])

print("Mat 3x3 : \n",tab3x3)

tab1D=tab3x3.reshape(1,-1)

print("Tableau applatis:\n",tab1D)