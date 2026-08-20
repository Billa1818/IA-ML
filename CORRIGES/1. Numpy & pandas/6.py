#Exercice 6 — Statistiques et aléatoire
import numpy as np

np.random.seed(5) # Fixe la graine pour la génération de nombres aléatoires afin d'obtenir les mêmes résultats à chaque exécution

arr = np.random.normal(50,10,1000) # Génère un tableau de 1000 valeurs aléatoires suivant une distribution normale avec une moyenne de 50 et un écart type de 10

min = np.min(arr) # Calcule la valeur minimale du tableau arr

max = np.max(arr) # Calcule la valeur maximale du tableau arr

mean =  np.mean(arr) # Calcule la moyenne du tableau arr

std =np.median(arr) # Calcule la médiane du tableau arr

q1 = np.quantile(arr,0.25) # Calcule le premier quartile (25ème percentile) du tableau arr

q3 = np.quantile(arr,0.75) # Calcule le troisième quartile (75ème percentile) du tableau arr

arr1 = np.random.randint(4,45,50) # Génère un tableau de 50 valeurs aléatoires entières entre 4 et 44

arr2 = np.random.randint(4,20,50) # Génère un tableau de 50 valeurs aléatoires entières entre 4 et 19

corel =  np.correlate(arr1,arr2) #  Calcule la corrélation entre les deux tableaux arr1 et arr2

print(corel)
