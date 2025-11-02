import numpy as np

x = np.random.uniform(-10, 10, 100)
y = np.random.uniform(-10, 10, 100)

# Conversion en polaires
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

print(f"Nombre de points : {len(x)}")
print(f"Rayon moyen : {r.mean():.2f}")

# Filtrage cercle rayon 5
masque = r <= 5
points_cercle = np.sum(masque)
distance_moyenne = r[masque].mean()

print(f"\nPoints dans le cercle (r ≤ 5) : {points_cercle}")
print(f"Distance moyenne à l'origine : {distance_moyenne:.2f}")

