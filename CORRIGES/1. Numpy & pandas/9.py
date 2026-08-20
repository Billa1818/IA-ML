# Exercice 9 — Sélection et filtrage
import pandas as pd

data = {
    "nom": ["Alice", "Bob", "Claire", "David", "Emma", "Fabien", "Gabriel", "Hugo", "Inès", "Jules"],
    "age": [28, 34, 41, 25, 30, 45, 38, 29, 32, 27],
    "ville": ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Nantes", "Lille", "Strasbourg", "Rennes", "Montpellier"],
    "salaire": [35000, 42000, 51000, 31000, 38000, 56000, 48000, 36000, 40000, 34000]
}

df = pd.DataFrame(data)

ndf= df[["nom","salaire"]]

print("Dataframe avec nom et salaire \n",ndf)

print("Plus de 29 ans : \n ",df[df["age"]>29])

print("Habitant a paris et lyon:\n",df[df["ville"].isin(["Paris","Lyon"])])

print("Salaire entre 40000 et 50000:\n",df[(df["salaire"]>=40000) & (df["salaire"]<=50000)])

print("1er ligne par position :\n",df.iloc[2])

print("4eme ligne par position :\n",df.iloc[4])