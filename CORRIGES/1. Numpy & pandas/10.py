# Exercice 10 — Données manquantes
import pandas as pd

data = {
    "nom": ["Clavier", "Souris", None, "Écran", "Casque", "Webcam"],
    "prix": [15000, None, 25000, 120000, None, 35000],
    "categorie": ["Informatique", None, "Accessoire", "Informatique", None, "Accessoire"],
    "stock": ["10", "25", "15", "5", None, "20"]
}


df = pd.DataFrame(data)

print("Dataframe :\n",df)

print("Valeur vide : \n",df.isna(),f"il y a {df.isna().count()} valeur vide")

mean = df["prix"].mean()

df["prix"] = df[["prix"]].fillna(mean)

print("Dataframe avec valeur manquante prix remplacer par la moyenne :\n",df)

df["categorie"] = df[["categorie"]].fillna("inconnu")

print("Dataframe avec les categorie manquante remplace par inconnu  :\n",df)

df = df.dropna(subset=["nom"])

print("Dataframe avec nom null supprimer :\n",df)

df["stock"] = df["stock"].fillna(0).astype(int)

