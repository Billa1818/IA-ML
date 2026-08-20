# Exercice 4 — Histogramme et distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaires = np.random.normal(loc=250000, scale=50000, size=1000)
df = pd.DataFrame({'Salaire': salaires})

moyenne = df['Salaire'].mean()
mediane = df['Salaire'].median()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].hist(df['Salaire'], bins=40, density=True, color='lightgray', edgecolor='white')

df['Salaire'].plot.kde(ax=ax[0], color='black', linewidth=2, label='Densité')

ax[0].axvline(moyenne, color='crimson', linestyle='--', linewidth=2.5, label=f'Moyenne ({moyenne:,.0f})')

ax[0].axvline(mediane, color='dodgerblue', linestyle=':', linewidth=3, label=f'Médiane ({mediane:,.0f})')

ax[0].set_title("Distribution des salaires")
ax[0].set_xlabel("Salaire")
ax[0].set_ylabel("Densité")
ax[0].legend()

ax[1].boxplot(
    df['Salaire'], 
    vert=False, 
    patch_artist=True,
    boxprops=dict(facecolor='skyblue', color='black'),
    medianprops=dict(color='dodgerblue', linewidth=2)
)

ax[1].set_title("Dispersion et valeurs atypiques")
ax[1].set_xlabel("Salaire")

ax[1].set_yticks([]) 

ax[1].set_xlim(ax[0].get_xlim())

plt.tight_layout()
plt.show()