import numpy as np

lancers = np.random.randint(1, 7, 1000)

valeurs_uniques, frequences = np.unique(lancers, return_counts=True)
print("Valeurs uniques :", valeurs_uniques)
print("Fréquences :", frequences)

face_plus_freq = valeurs_uniques[frequences.argmax()]
face_moins_freq = valeurs_uniques[frequences.argmin()]
print(f"\nFace la plus fréquente : {face_plus_freq} ({frequences.max()} fois)")
print(f"Face la moins fréquente : {face_moins_freq} ({frequences.min()} fois)")

ecart_type_freq = frequences.std()
print(f"Écart-type des fréquences : {ecart_type_freq:.2f}")
print(f"Distribution uniforme : {ecart_type_freq < 20}")

