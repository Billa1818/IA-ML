import numpy as np

A = np.arange(1, 17).reshape(4, 4)
B = np.random.rand(4, 4)

print("Matrice A :\n", A)
print("\nMatrice B :\n", B)

# 1. P = A × B × A^T
P = A @ B @ A.T
print("\nP = A × B × A^T :\n", P)

# 2. Q = (A + B) × (A - B)
Q = (A + B) @ (A - B)
print("\nQ = (A + B) × (A - B) :\n", Q)

# 3. P symétrique ?
est_symetrique = np.allclose(P, P.T)
print(f"\nP est symétrique : {est_symetrique}")

det_P = np.linalg.det(P)
print(f"Déterminant de P : {det_P:.4f}")

