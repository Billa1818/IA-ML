# Exercice 18 — Benchmarking de méthodes de calcul
import pandas as pd
import numpy as np
import time

np.random.seed(42)
df = pd.DataFrame({
    'x': np.random.randint(0, 1000, 100_000),
    'y': np.random.randint(0, 1000, 100_000)
})

print("Démarrage du benchmark...\n")

debut = time.perf_counter()

df.apply(lambda ligne: np.sqrt(ligne['x']**2 + ligne['y']**2), axis=1)
temps_apply = time.perf_counter() - debut
print(f"Méthode 1 (apply)        : {temps_apply:.4f} secondes")

debut = time.perf_counter()
np.sqrt(df['x']**2 + df['y']**2)
temps_pandas = time.perf_counter() - debut
print(f"Méthode 2 (Pandas)       : {temps_pandas:.4f} secondes")

debut = time.perf_counter()

np.hypot(df['x'].to_numpy(), df['y'].to_numpy())
temps_numpy = time.perf_counter() - debut
print(f"Méthode 3 (NumPy pur)    : {temps_numpy:.4f} secondes")

print("-" * 40)

df['distance_euclidienne'] = np.hypot(df['x'].to_numpy(), df['y'].to_numpy())

print("\nRésumé statistique de la distance :")
print(df['distance_euclidienne'].describe())