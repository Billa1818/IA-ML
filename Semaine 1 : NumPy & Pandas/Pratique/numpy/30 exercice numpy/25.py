import numpy as np

ventes = np.zeros((100, 4))
ventes[:, 0] = np.random.randint(1, 31, 100)  # dates (jours 1-30)
ventes[:, 1] = np.random.randint(1, 6, 100)   # produit_id (1-5)
ventes[:, 2] = np.random.randint(1, 11, 100)  # quantité
ventes[:, 3] = np.random.uniform(10, 100, 100)  # prix

np.savetxt('ventes.csv', ventes, delimiter=',', 
           header='date,produit_id,quantite,prix', comments='')

# Rechargement et analyse
data = np.loadtxt('ventes.csv', delimiter=',', skiprows=1)

# 1. Ventes totales par produit
for produit in range(1, 6):
    mask = data[:, 1] == produit
    total = np.sum(data[mask, 2] * data[mask, 3])
    print(f"Produit {produit} : {total:.2f}€")

# 2. Jour avec CA le plus élevé
ca_par_jour = {}
for jour in np.unique(data[:, 0]):
    mask = data[:, 0] == jour
    ca_par_jour[jour] = np.sum(data[mask, 2] * data[mask, 3])
meilleur_jour = max(ca_par_jour, key=ca_par_jour.get)
print(f"\nMeilleur jour : {int(meilleur_jour)} (CA: {ca_par_jour[meilleur_jour]:.2f}€)")

# 3. Produit le plus vendu
quantites_par_produit = {}
for produit in range(1, 6):
    mask = data[:, 1] == produit
    quantites_par_produit[produit] = np.sum(data[mask, 2])
produit_plus_vendu = max(quantites_par_produit, key=quantites_par_produit.get)
print(f"Produit le plus vendu : {produit_plus_vendu} ({quantites_par_produit[produit_plus_vendu]:.0f} unités)")

