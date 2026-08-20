# Exercice 5 — Sous-graphiques et mise en page
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

jours = np.arange(1, 91)
ventes_A = np.random.randint(20, 100, size=90)
ventes_B = np.random.randint(50, 150, size=90)
ventes_C = np.random.randint(10, 80, size=90)

departements = ["Alibori", "Atacora", "Atlantique", "Borgou", "Collines", "Couffo", 
                "Donga", "Littoral", "Mono", "Ouémé", "Plateau", "Zou"]
ventes_dep = np.random.randint(500, 500000, 12)
df_regions = pd.DataFrame({"Departement": departements, "Ventes": ventes_dep})
df_regions = df_regions.sort_values(by='Ventes') 

categories = np.random.choice(['Junior', 'Confirmé', 'Senior'], size=200, p=[0.4, 0.4, 0.2])
ages, salaires_corr = [], []
for cat in categories:
    if cat == 'Junior':
        ages.append(np.random.randint(20, 30))
        salaires_corr.append(np.random.randint(150000, 300000))
    elif cat == 'Confirmé':
        ages.append(np.random.randint(30, 45))
        salaires_corr.append(np.random.randint(300000, 700000))
    else:
        ages.append(np.random.randint(45, 65))
        salaires_corr.append(np.random.randint(700000, 1500000))
df_corr = pd.DataFrame({'Age': ages, 'Salaire': salaires_corr, 'Categorie': categories})

salaires_dist = np.random.normal(loc=250000, scale=50000, size=1000)
df_dist = pd.DataFrame({'Salaire': salaires_dist})

fig, ax = plt.subplots(2, 2, figsize=(16, 10))

fig.suptitle("Tableau de Bord : Analyse Globale des Performances et RH", fontsize=18, fontweight='bold')

ax[0, 0].plot(jours, ventes_A, color='royalblue', label="Produit A")
ax[0, 0].plot(jours, ventes_B, color='darkorange', label="Produit B")
ax[0, 0].plot(jours, ventes_C, color='forestgreen', label="Produit C")
ax[0, 0].set_title("1. Évolution des ventes (90 jours)")
ax[0, 0].legend()
ax[0, 0].grid(alpha=0.3)

couleurs_dep = ['dodgerblue' if dep == df_regions.iloc[-1]['Departement'] else 'lightgray' for dep in df_regions['Departement']]
ax[0, 1].barh(df_regions['Departement'], df_regions['Ventes'], color=couleurs_dep, edgecolor='black')
ax[0, 1].set_title(f"2. Ventes par département (Leader : {df_regions.iloc[-1]['Departement']})")
ax[0, 1].set_xlabel("Chiffre d'affaires (FCFA)")

couleurs_cat = {'Junior': 'limegreen', 'Confirmé': 'dodgerblue', 'Senior': 'crimson'}
for cat in ['Junior', 'Confirmé', 'Senior']:
    df_filtre = df_corr[df_corr['Categorie'] == cat]
    ax[1, 0].scatter(df_filtre['Age'], df_filtre['Salaire'], color=couleurs_cat[cat], label=cat, alpha=0.7, edgecolors='black')

coefs = np.polyfit(df_corr['Age'], df_corr['Salaire'], 1)
x_ligne = np.array([df_corr['Age'].min(), df_corr['Age'].max()])
ax[1, 0].plot(x_ligne, coefs[0] * x_ligne + coefs[1], color='black', linestyle='--', linewidth=2, label="Tendance")

ax[1, 0].set_title("3. Corrélation Expérience / Salaire")
ax[1, 0].legend()
ax[1, 0].grid(alpha=0.3)

ax[1, 1].hist(df_dist['Salaire'], bins=30, density=True, color='lightgray', edgecolor='white')
df_dist['Salaire'].plot.kde(ax=ax[1, 1], color='black', linewidth=2, label='Densité')

moyenne = df_dist['Salaire'].mean()
mediane = df_dist['Salaire'].median()
ax[1, 1].axvline(moyenne, color='crimson', linestyle='--', linewidth=2, label='Moyenne')
ax[1, 1].axvline(mediane, color='dodgerblue', linestyle=':', linewidth=2, label='Médiane')

ax[1, 1].set_title("4. Distribution Globale des Salaires (Loi normale)")
ax[1, 1].legend()

plt.tight_layout()

fig.subplots_adjust(top=0.92) 

plt.show()