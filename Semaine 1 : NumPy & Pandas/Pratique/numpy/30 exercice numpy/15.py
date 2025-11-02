import numpy as np

notes = np.random.randint(0, 21, size=(15, 6))
print("Matrice des notes :\n", notes)

# 1. Moyenne de chaque étudiant
moyennes_etudiants = notes.mean(axis=1)
print("\nMoyennes des étudiants :", moyennes_etudiants)

# 2. Moyenne de chaque matière
moyennes_matieres = notes.mean(axis=0)
print("Moyennes des matières :", moyennes_matieres)

# 3. Écart-type de chaque matière
ecarts_types = notes.std(axis=0)
print("Écarts-types des matières :", ecarts_types)

# 4. Meilleur étudiant et matière la plus difficile
meilleur_etudiant = moyennes_etudiants.argmax()
matiere_difficile = moyennes_matieres.argmin()
print(f"\nMeilleur étudiant : {meilleur_etudiant} (moyenne: {moyennes_etudiants[meilleur_etudiant]:.2f})")
print(f"Matière la plus difficile : {matiere_difficile} (moyenne: {moyennes_matieres[matiere_difficile]:.2f})")
