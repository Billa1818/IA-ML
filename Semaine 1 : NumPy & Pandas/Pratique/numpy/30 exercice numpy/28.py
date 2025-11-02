import numpy as np

dtype = [('titre', 'U30'), ('auteur', 'U20'), ('annee', 'i4'), ('pages', 'i4'), ('prix', 'f4')]
livres = np.zeros(50, dtype=dtype)

titres = [f"Livre_{i}" for i in range(50)]
auteurs = [f"Auteur_{i%15}" for i in range(50)]
livres['titre'] = titres
livres['auteur'] = auteurs
livres['annee'] = np.random.randint(1980, 2024, 50)
livres['pages'] = np.random.randint(100, 800, 50)
livres['prix'] = np.random.uniform(5, 50, 50)

# 1. Livres après 2000
apres_2000 = livres[livres['annee'] > 2000]
print(f"Livres publiés après 2000 : {len(apres_2000)}")

# 2. Plus de 300 pages et moins de 20€
critere = (livres['pages'] > 300) & (livres['prix'] < 20)
livres_critere = livres[critere]
print(f"Livres > 300 pages et < 20€ : {len(livres_critere)}")

# 3. Auteur le plus prolifique
auteurs_uniques, comptes = np.unique(livres['auteur'], return_counts=True)
auteur_max = auteurs_uniques[comptes.argmax()]
print(f"Auteur le plus prolifique : {auteur_max} ({comptes.max()} livres)")

