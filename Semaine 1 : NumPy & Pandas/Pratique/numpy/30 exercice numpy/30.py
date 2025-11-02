import numpy as np

performances = np.random.uniform(0, 100, size=(30, 10))
print(f"Dataset : {performances.shape} (30 athlètes, 10 épreuves)")

# 1. Normalisation z-score
moyennes = performances.mean(axis=0)
ecarts_types = performances.std(axis=0)
z_scores = (performances - moyennes) / ecarts_types
print("\nNormalisation z-score effectuée")

# 2. Classement par score total
scores_totaux = performances.sum(axis=1)
classement = np.argsort(scores_totaux)[::-1]
print(f"\nTop 3 athlètes :")
for i in range(3):
    athlete = classement[i]
    print(f"  Athlète {athlete} : {scores_totaux[athlete]:.2f} points")

# 3. Épreuves discriminantes
ecarts_epreuves = performances.std(axis=0)
epreuve_plus_discriminante = ecarts_epreuves.argmax()
print(f"\nÉpreuve la plus discriminante : {epreuve_plus_discriminante} (σ={ecarts_epreuves[epreuve_plus_discriminante]:.2f})")

# 4. Matrice de corrélation
corr_matrix = np.corrcoef(performances.T)
print("\nMatrice de corrélation entre épreuves calculée")
print(f"Shape : {corr_matrix.shape}")

# 5. Sauvegarde
classement_data = np.column_stack([classement + 1, scores_totaux[classement]])
np.savetxt('classement.csv', classement_data, delimiter=',', 
           header='athlete,score_total', comments='', fmt='%d,%.2f')

np.savez('statistiques.npz', 
         z_scores=z_scores,
         correlations=corr_matrix,
         ecarts_types=ecarts_epreuves)

print("\nFichiers sauvegardés : classement.csv, statistiques.npz")
print("\n" + "=" * 50)
