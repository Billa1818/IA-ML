import numpy as np

dtype = [('nom', 'U10'), ('note_maths', 'f4'), ('note_info', 'f4')]
etudiants = np.zeros(20, dtype=dtype)

noms = [f"Etud{i}" for i in range(20)]
etudiants['nom'] = noms
etudiants['note_maths'] = np.random.uniform(0, 20, 20)
etudiants['note_info'] = np.random.uniform(0, 20, 20)

# 1. Tri par note_maths décroissante
tri_maths = np.sort(etudiants, order='note_maths')[::-1]
print("Top 5 en maths :")
for i in range(5):
    print(f"  {tri_maths[i]['nom']}: {tri_maths[i]['note_maths']:.2f}")

# 2. Tri par moyenne décroissante
moyennes = (etudiants['note_maths'] + etudiants['note_info']) / 2
indices_tri = np.argsort(moyennes)[::-1]
print("\nTop 5 par moyenne :")
for i in range(5):
    idx = indices_tri[i]
    print(f"  {etudiants[idx]['nom']}: {moyennes[idx]:.2f}")


