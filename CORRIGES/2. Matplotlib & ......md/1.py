# Exercice 1 — Graphique linéaire
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

jour =  np.arange(1,91)

citron = np.random.randint(20,150,90)

banane = np.random.randint(40,100,90)

orange = np.random.randint(25,70,90)

data = {
    "citron":citron,
    "banane":banane,
    "orange":orange
}

df = pd.DataFrame(data)

fig , ax = plt.subplots()

ax.plot(jour,df["citron"],label="Citron")

ax.plot(jour,df["banane"],label="banane")

ax.plot(jour,df["orange"],label="orange")

ax.legend()

ax.set_title("Evolution des produits citron, banane et orange")

ax.set_xlabel("Quantité vendu")

ax.set_ylabel("jour(s)")

ax.grid(True,alpha=0.4,linestyle=":")

plt.show()