import numpy as np # Importation de la bibliothèque NumPy
arr=np.random.randn(1000) # Création d'un tableau NumPy avec 1000 valeurs aléatoires suivant une distribution normale
print("Tableau initial :", arr)
moyenne=np.mean(arr) # Calcul de la moyenne des valeurs
print("Moyenne :", moyenne)
mediane=np.median(arr) # Calcul de la médiane des valeurs
print("Médiane :", mediane)
ecart_type=np.std(arr) # Calcul de l'écart-type des valeurs
print("Écart-type :", ecart_type)
percentile_95=np.percentile(arr, 95) # Calcul du 95ème percentile
print("95ème percentile :", percentile_95)
unique=np.unique(arr[(arr >= moyenne - ecart_type) & (arr <= moyenne + ecart_type)],return_counts=True) # Extraction des valeurs uniques
print("Valeurs uniques et leurs occurrences :", unique)