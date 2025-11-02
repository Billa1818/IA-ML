import numpy as np

X = np.random.uniform(10, 35, 365)
bruit = np.random.normal(0, 10, 365)
Y = 2 * X + bruit
Z = np.random.uniform(0, 100, 365)

corr_XY = np.corrcoef(X, Y)[0, 1]
corr_XZ = np.corrcoef(X, Z)[0, 1]
print(f"Corrélation X-Y : {corr_XY:.4f}")
print(f"Corrélation X-Z : {corr_XZ:.4f}")

matrice_corr = np.corrcoef([X, Y, Z])
print("\nMatrice de corrélation complète :\n", matrice_corr)
