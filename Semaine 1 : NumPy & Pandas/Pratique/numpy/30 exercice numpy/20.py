import numpy as np 

A_random = np.random.rand(4, 4)
A_sym = (A_random + A_random.T) / 2
print("Matrice symétrique :\n", A_sym)

valeurs_propres, vecteurs_propres = np.linalg.eig(A_sym)
print("\nValeurs propres :", valeurs_propres)
print("Vecteurs propres :\n", vecteurs_propres)

# Vérification A × v = λ × v pour la première valeur propre
v0 = vecteurs_propres[:, 0]
lambda0 = valeurs_propres[0]
Av = A_sym @ v0
lambda_v = lambda0 * v0
print(f"\nVérification A×v = λ×v : {np.allclose(Av, lambda_v)}")

valeur_dominante = valeurs_propres[np.abs(valeurs_propres).argmax()]
print(f"Valeur propre dominante : {valeur_dominante:.4f}")


