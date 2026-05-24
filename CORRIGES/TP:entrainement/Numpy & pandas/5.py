# Exercice 5
import numpy as np

A = [[2,1],[5,3]]
B = [8,13]

mat1 = np.array(A)

mat2= np.array(B)


print("Matrice A: \n",mat1)

print("Matrice B: \n",mat2)

prod= np.dot(mat1,mat2)

print("A * B: \n",prod)

inv_mat1=np.linalg.inv(mat1)

print("Inverse a A1 \n",inv_mat1)

det_mat1=np.linalg.det(mat1)

print("Determinant a A \n",det_mat1)

sol = np.linalg.solve(mat1, mat2)

print("Solution Ax=b \n",sol)

vap,vep=np.linalg.eig(mat1)

print("Valeur propre de  A \n",vap)

print("Vecteur propre de  A \n",vep)

matS= mat1.T

print("Transpose de A \n",matS)

