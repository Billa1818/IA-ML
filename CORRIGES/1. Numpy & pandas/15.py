# Exercice 15 — Génération et analyse de données
import pandas as pd
import numpy as np

age = np.random.randint(1,90,200)

salaire = np.random.uniform(500,20000,200)

score = np.random.rand(200)*100

df = pd.DataFrame({
    "age":age,
    "salaire":salaire,
    "score":score.round(0)
})

print("Dataframe:\n",df)

df["quatile"] = pd.qcut(df["salaire"],q=4,labels=["Q1","Q2","Q3","Q4"])

print("Les quartiles du salaire:\n",df)

correl = df["age"].corr(df["salaire"])

print("Corralation entre age et salaire:\n",correl)

