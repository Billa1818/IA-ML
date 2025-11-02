import numpy as np # Importation de la bibliothèque NumPy
temperature=np.random.uniform(0,40,(365)) # Création d'un tableau 1D avec des flottants aléatoires entre 0 et 40
saison=np.array_split(temperature,4)
noms_saisons=["Printemps","Été","Automne","Hiver"] # Noms des saisons
for i, saison_temps in enumerate(saison):
    moyenne=np.mean(saison_temps) # Calcul de la moyenne des températures pour la saison
    print(f"{noms_saisons[i]} - Moyenne: {moyenne:.2f}°C") # Affichage des résultats
    max_temp=np.max(saison_temps) # Calcul de la température maximale pour la saison
    jour_max=np.argmax(saison_temps) + i*len(saison_temps)
    min_temp=np.min(saison_temps) # Calcul de la température minimale pour la saison
    jour_min=np.argmin(saison_temps) + i*len(saison_temps)

    print(f"  Température maximale: {max_temp:.2f}°C, Jour: {jour_max}") # Affichage de la température maximale
    print(f"  Température minimale: {min_temp:.2f}°C, Jour: {jour_min}")
    #Moyenne mobile sur 7 jours
    moyenne_mobile=np.convolve(saison_temps, np.ones(7)/7, mode='valid')
    print(f"  Moyenne mobile sur 7 jours (premiers 5 jours): {moyenne_mobile[:5]}") # Affichage des 5 premiers jours de la moyenne mobile
# Histogramme des températures pour la saison
    hist, bin_edges = np.histogram(saison_temps, bins=10, range=(0,40))
    print(f"  Histogramme des températures (10 bins):")
    for j in range(len(hist)):
        print(f"    {bin_edges[j]:.1f} - {bin_edges[j+1]:.1f}°C: {hist[j]} jours")
    print()