import numpy as np

A = np.random.randint(0, 100, size=(5, 5))
B = np.random.rand(20)
C = np.random.rand(3, 4) + 1j * np.random.rand(3, 4)

np.savez('donnees.npz', matrice_A=A, vecteur_B=B, complexe_C=C)
print("Fichier sauvegardé : donnees.npz")

# Rechargement
data = np.load('donnees.npz')
A_charge = data['matrice_A']
B_charge = data['vecteur_B']
C_charge = data['complexe_C']

print(f"A identique : {np.array_equal(A, A_charge)}")
print(f"B identique : {np.array_equal(B, B_charge)}")
print(f"C identique : {np.array_equal(C, C_charge)}")

