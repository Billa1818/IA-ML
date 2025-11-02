import numpy as np

#  Création d'une image 100x100 avec gradient horizontal
# Chaque colonne aura une intensité croissante de 0 à 255
image = np.tile(np.linspace(0, 255, 100, dtype=np.uint8), (100, 1))

print("Image originale (gradient horizontal) créée.")

#  Ajout de bruit aléatoire
# On ajoute du bruit uniforme entre -30 et +30, puis on recadre entre 0 et 255
bruit = np.random.randint(-30, 31, (100, 100))
image_bruitee = np.clip(image.astype(int) + bruit, 0, 255).astype(np.uint8)

print("Bruit ajouté à l'image.")

#  Application d'un seuillage binaire
# Si la valeur > 128 → 255, sinon → 0
image_seuil = np.where(image_bruitee > 128, 255, 0).astype(np.uint8)

print("Seuillage appliqué (binaire 0 / 255).")

#  Calcul de l'histogramme
# Nombre d'occurrences pour chaque intensité de 0 à 255
histogramme = np.bincount(image_seuil.flatten(), minlength=256)

print("Histogramme calculé.")
print("Valeurs non nulles de l'histogramme :")
for i, v in enumerate(histogramme):
    if v > 0:
        print(f"Niveau {i} : {v} pixels")

#  Inversion de l'image (négatif)
image_negative = 255 - image_seuil

print("Image inversée (négatif) générée.")
