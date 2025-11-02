import numpy as np

A = np.array([[2, 1, -1], [1, 3, 2], [3, 1, -3]])
b = np.array([8, 13, 2])

x = np.linalg.solve(A, b)
print("Solution x :", x)

# Vérification
verification = A @ x
print("Vérification A × x :", verification)
print("b :", b)
print(f"Solution correcte : {np.allclose(verification, b)}")
