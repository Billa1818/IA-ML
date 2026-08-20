# Exercice 16 — Transformations en masse
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

def stat(val):
    if val >=10 and val <=30:
        return True
    return False

df['senior'] = df["age"].apply(stat)

df["salaire"] = df["salaire"].clip(upper=600,lower=19000)

def  score(val):
    if val < 50:
        return "faible" 
    elif val ==50 : 
        return "passable"
    elif val >50 :
        return "forte"


df["cat_score"] = df["score"].apply(score)


print("Dataframe:\n",df)