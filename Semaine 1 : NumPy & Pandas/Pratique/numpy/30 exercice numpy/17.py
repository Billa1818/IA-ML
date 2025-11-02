import numpy as np

donnees = np.random.normal(100, 15, 10000)
hist, bins = np.histogram(donnees, bins=20)

print("Valeurs par bin :", hist)
print("Limites des bins :", bins)

# Pourcentage entre 85 et 115
valeurs_intervalle = np.sum((donnees >= 85) & (donnees <= 115))
pourcentage = (valeurs_intervalle / 10000) * 100
print(f"\nPourcentage entre 85 et 115 : {pourcentage:.2f}%")

print(f"Bin le plus rempli : {hist.argmax()} ({hist.max()} valeurs)")
print(f"Bin le moins rempli : {hist.argmin()} ({hist.min()} valeurs)")

# Vérification 68%
valeurs_1std = np.sum((donnees >= 85) & (donnees <= 115))
pct_1std = (valeurs_1std / 10000) * 100
print(f"\nVérification 68% : {pct_1std:.2f}% (attendu: ~68%)")
