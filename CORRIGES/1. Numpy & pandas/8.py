# Exercice 8 — Création et inspection
import pandas as pd

data = {
    "nom": ["Alice", "Bob", "Claire", "David", "Emma", "Fabien", "Gabriel", "Hugo", "Inès", "Jules"],
    "age": [28, 34, 41, 25, 30, 45, 38, 29, 32, 27],
    "ville": ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Nantes", "Lille", "Strasbourg", "Rennes", "Montpellier"],
    "salaire": [35000, 42000, 51000, 31000, 38000, 56000, 48000, 36000, 40000, 34000]
}

df = pd.DataFrame(data)

print("3 firt ligne:\n",df.head(3))

print("Type colonne:\n",df.dtypes)

print("Statistique:\n",df.describe())

if df.isna().any().any() == True:
    print("Il y a une valeur manquantes")
else:
    print("Il n'y a pas de valeur manquantes")