"""
CORRECTIONS COMPLÈTES DES EXERCICES PANDAS
==========================================
Document de référence avec solutions détaillées et commentées
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# ============================================================================
# CHAPITRE 2: STRUCTURES DE DONNÉES
# ============================================================================

print("=" * 80)
print("CHAPITRE 2: STRUCTURES DE DONNÉES")
print("=" * 80)

# ----------------------------------------------------------------------------
# Exercice 2.1: Maîtrise des Series
# ----------------------------------------------------------------------------
print("\n--- Exercice 2.1: Maîtrise des Series ---\n")

# Series 1: Températures quotidiennes
temperatures = pd.Series([22.5, 24.3, 21.8, 23.1, 25.6, 20.4, 22.9])
print("1. Series des températures:")
print(f"Valeurs:\n{temperatures.values}")
print(f"Index: {temperatures.index.tolist()}")
print(f"Type de données: {temperatures.dtype}")
print(f"Forme: {temperatures.shape}")
print(f"Taille: {temperatures.size}")

# Ajout d'index personnalisé
jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
temperatures.index = jours
print(f"\nTempératures avec index personnalisé:\n{temperatures}")

# Series 2: Populations de pays
populations = pd.Series({
    'France': 67_000_000,
    'Allemagne': 83_000_000,
    'Italie': 60_000_000,
    'Espagne': 47_000_000,
    'Belgique': 11_500_000
})
print(f"\n2. Series des populations:")
print(f"Valeurs: {populations.values}")
print(f"Index: {populations.index.tolist()}")
print(f"Type: {populations.dtype}")
print(f"Forme: {populations.shape}")
print(f"Taille: {populations.size}")

# Series 3: Notes d'étudiants
notes_array = np.array([15.5, 12.0, 18.5, 14.0, 16.5, 11.0, 17.0, 13.5, 19.0, 15.0])
notes = pd.Series(notes_array)
print(f"\n3. Series des notes:")
print(f"Valeurs: {notes.values}")
print(f"Index: {notes.index.tolist()}")
print(f"Type: {notes.dtype}")
print(f"Forme: {notes.shape}")
print(f"Taille: {notes.size}")

# ----------------------------------------------------------------------------
# Exercice 2.2: Construction de DataFrames complexes
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 2.2: Construction de DataFrames complexes ---\n")

# Méthode 1: À partir d'un dictionnaire
livres_dict = {
    'Titre': ['1984', 'Le Petit Prince', 'Harry Potter', "L'Étranger", 
              'Germinal', 'Les Misérables', 'Candide', 'Madame Bovary',
              'Le Comte de Monte-Cristo', 'Notre-Dame de Paris', 
              'Voyage au centre de la Terre', 'Vingt mille lieues',
              'Les Trois Mousquetaires', "L'Assommoir", 'Bel-Ami'],
    'Auteur': ['George Orwell', 'Antoine de Saint-Exupéry', 'J.K. Rowling',
               'Albert Camus', 'Émile Zola', 'Victor Hugo', 'Voltaire',
               'Gustave Flaubert', 'Alexandre Dumas', 'Victor Hugo',
               'Jules Verne', 'Jules Verne', 'Alexandre Dumas', 
               'Émile Zola', 'Guy de Maupassant'],
    'Année_Publication': [1949, 1943, 1997, 1942, 1885, 1862, 1759, 1857,
                          1844, 1831, 1864, 1870, 1844, 1877, 1885],
    'Genre': ['Science-Fiction', 'Conte', 'Fantasy', 'Roman', 'Roman',
              'Roman', 'Conte philosophique', 'Roman', 'Roman', 'Roman',
              'Science-Fiction', 'Science-Fiction', 'Roman historique',
              'Roman', 'Roman'],
    'Nombre_Pages': [328, 96, 309, 186, 591, 1232, 144, 432, 1276, 512,
                     442, 424, 704, 502, 418],
    'Prix': [12.50, 7.90, 22.90, 9.50, 15.90, 28.00, 6.50, 14.90,
             32.00, 19.90, 12.90, 13.50, 24.90, 16.50, 11.90],
    'Disponible': [True, True, False, True, True, False, True, True,
                   True, False, True, True, False, True, True]
}
df_livres_1 = pd.DataFrame(livres_dict)
print("Méthode 1 - DataFrame depuis dictionnaire:")
print(df_livres_1.head())

# Méthode 2: À partir d'une liste de listes
donnees_livres = [
    ['1984', 'George Orwell', 1949, 'Science-Fiction', 328, 12.50, True],
    ['Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 96, 7.90, True],
    ['Harry Potter', 'J.K. Rowling', 1997, 'Fantasy', 309, 22.90, False],
    ["L'Étranger", 'Albert Camus', 1942, 'Roman', 186, 9.50, True],
    ['Germinal', 'Émile Zola', 1885, 'Roman', 591, 15.90, True],
    ['Les Misérables', 'Victor Hugo', 1862, 'Roman', 1232, 28.00, False],
    ['Candide', 'Voltaire', 1759, 'Conte philosophique', 144, 6.50, True],
    ['Madame Bovary', 'Gustave Flaubert', 1857, 'Roman', 432, 14.90, True],
    ['Le Comte de Monte-Cristo', 'Alexandre Dumas', 1844, 'Roman', 1276, 32.00, True],
    ['Notre-Dame de Paris', 'Victor Hugo', 1831, 'Roman', 512, 19.90, False],
    ['Voyage au centre de la Terre', 'Jules Verne', 1864, 'Science-Fiction', 442, 12.90, True],
    ['Vingt mille lieues', 'Jules Verne', 1870, 'Science-Fiction', 424, 13.50, True],
    ['Les Trois Mousquetaires', 'Alexandre Dumas', 1844, 'Roman historique', 704, 24.90, False],
    ["L'Assommoir", 'Émile Zola', 1877, 'Roman', 502, 16.50, True],
    ['Bel-Ami', 'Guy de Maupassant', 1885, 'Roman', 418, 11.90, True]
]
colonnes = ['Titre', 'Auteur', 'Année_Publication', 'Genre', 'Nombre_Pages', 'Prix', 'Disponible']
df_livres_2 = pd.DataFrame(donnees_livres, columns=colonnes)
print("\nMéthode 2 - DataFrame depuis liste de listes:")
print(df_livres_2.head())

# Méthode 3: À partir d'un dictionnaire de Series
series_titre = pd.Series(livres_dict['Titre'])
series_auteur = pd.Series(livres_dict['Auteur'])
series_annee = pd.Series(livres_dict['Année_Publication'])
series_genre = pd.Series(livres_dict['Genre'])
series_pages = pd.Series(livres_dict['Nombre_Pages'])
series_prix = pd.Series(livres_dict['Prix'])
series_dispo = pd.Series(livres_dict['Disponible'])

df_livres_3 = pd.DataFrame({
    'Titre': series_titre,
    'Auteur': series_auteur,
    'Année_Publication': series_annee,
    'Genre': series_genre,
    'Nombre_Pages': series_pages,
    'Prix': series_prix,
    'Disponible': series_dispo
})
print("\nMéthode 3 - DataFrame depuis dictionnaire de Series:")
print(df_livres_3.head())

print("\nComparaison des méthodes:")
print("- Méthode 1 (dict): Simple et lisible, idéale pour données structurées")
print("- Méthode 2 (liste): Efficace pour grandes données, économe en mémoire")
print("- Méthode 3 (dict de Series): Plus de contrôle, utile pour manipulation avancée")

# ----------------------------------------------------------------------------
# Exercice 2.3: Analyse des propriétés des DataFrames
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 2.3: Analyse des propriétés des DataFrames ---\n")

df_livres = df_livres_1  # Utilisons le premier DataFrame

print("1. Forme (shape):")
print(f"   {df_livres.shape} - {df_livres.shape[0]} lignes × {df_livres.shape[1]} colonnes")

print("\n2. Colonnes:")
print(f"   {df_livres.columns.tolist()}")

print("\n3. Index:")
print(f"   {df_livres.index.tolist()}")

print("\n4. Types de données (dtypes):")
print(df_livres.dtypes)

print("\n5. Résumé avec info():")
df_livres.info()

print("\n6. Statistiques descriptives avec describe():")
print(df_livres.describe())

print("\n--- RAPPORT D'ANALYSE ---")
print(f"""
Le DataFrame contient {df_livres.shape[0]} livres avec {df_livres.shape[1]} caractéristiques.

TYPES DE DONNÉES:
- Texte (object): Titre, Auteur, Genre (3 colonnes)
- Nombres entiers (int64): Année_Publication, Nombre_Pages (2 colonnes)
- Nombres décimaux (float64): Prix (1 colonne)
- Booléen (bool): Disponible (1 colonne)

STATISTIQUES SUR LES PRIX:
- Prix moyen: {df_livres['Prix'].mean():.2f}€
- Prix médian: {df_livres['Prix'].median():.2f}€
- Prix minimum: {df_livres['Prix'].min():.2f}€
- Prix maximum: {df_livres['Prix'].max():.2f}€
- Écart-type: {df_livres['Prix'].std():.2f}€

STATISTIQUES SUR LE NOMBRE DE PAGES:
- Moyenne: {df_livres['Nombre_Pages'].mean():.0f} pages
- Médiane: {df_livres['Nombre_Pages'].median():.0f} pages
- Livre le plus court: {df_livres['Nombre_Pages'].min()} pages
- Livre le plus long: {df_livres['Nombre_Pages'].max()} pages

DISPONIBILITÉ:
- Livres disponibles: {df_livres['Disponible'].sum()} ({df_livres['Disponible'].sum()/len(df_livres)*100:.1f}%)
- Livres indisponibles: {(~df_livres['Disponible']).sum()} ({(~df_livres['Disponible']).sum()/len(df_livres)*100:.1f}%)
""")

# ============================================================================
# CHAPITRE 3: CRÉATION ET CHARGEMENT DE DONNÉES
# ============================================================================

print("\n" + "=" * 80)
print("CHAPITRE 3: CRÉATION ET CHARGEMENT DE DONNÉES")
print("=" * 80)

# ----------------------------------------------------------------------------
# Exercice 3.1: Manipulation de fichiers CSV avec options avancées
# ----------------------------------------------------------------------------
print("\n--- Exercice 3.1: Manipulation de fichiers CSV ---\n")

# Création des données de ventes
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
produits = ['Ordinateur', 'Souris', 'Clavier', 'Écran', 'Casque']
clients = ['Client_A', 'Client_B', 'Client_C', 'Client_D', 'Client_E']

ventes_data = {
    'Date': dates.strftime('%Y-%m-%d'),
    'Produit': np.random.choice(produits, 30),
    'Quantité': np.random.randint(1, 10, 30),
    'Prix_Unitaire': np.random.uniform(10, 500, 30).round(2),
    'Client': np.random.choice(clients, 30)
}

df_ventes = pd.DataFrame(ventes_data)

# Ajout de valeurs manquantes
indices_na = np.random.choice(df_ventes.index, 5, replace=False)
df_ventes.loc[indices_na[:3], 'Quantité'] = 'N/A'
df_ventes.loc[indices_na[3:], 'Prix_Unitaire'] = 'N/A'

# Sauvegarde avec séparateur point-virgule
df_ventes.to_csv('ventes_brut.csv', sep=';', index=False, encoding='utf-8')
print("Fichier 'ventes_brut.csv' créé avec succès")

# Chargement avec options avancées
df_ventes_charge = pd.read_csv(
    'ventes_brut.csv',
    sep=';',
    encoding='utf-8',
    na_values=['N/A'],
    parse_dates=['Date'],
    nrows=20
)

print(f"\nDonnées chargées: {df_ventes_charge.shape[0]} lignes")
print(f"Valeurs manquantes par colonne:")
print(df_ventes_charge.isnull().sum())

# Nettoyage et sauvegarde
df_ventes_propre = df_ventes_charge.dropna()
df_ventes_propre.to_csv('ventes_propre.csv', index=False, encoding='utf-8')
print(f"\nDonnées nettoyées sauvegardées: {df_ventes_propre.shape[0]} lignes")

# ----------------------------------------------------------------------------
# Exercice 3.2: Gestion de fichiers Excel multi-feuilles
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 3.2: Gestion de fichiers Excel multi-feuilles ---\n")

# Création des DataFrames
dates_2023 = pd.date_range('2023-01-01', periods=100, freq='D')
dates_2024 = pd.date_range('2024-01-01', periods=100, freq='D')

ventes_2023 = pd.DataFrame({
    'Date': dates_2023,
    'Produit_ID': np.random.randint(1, 6, 100),
    'Quantité': np.random.randint(1, 20, 100),
    'Montant': np.random.uniform(50, 1000, 100).round(2)
})

ventes_2024 = pd.DataFrame({
    'Date': dates_2024,
    'Produit_ID': np.random.randint(1, 6, 100),
    'Quantité': np.random.randint(1, 20, 100),
    'Montant': np.random.uniform(50, 1000, 100).round(2)
})

produits_info = pd.DataFrame({
    'Produit_ID': [1, 2, 3, 4, 5],
    'Nom': ['Ordinateur', 'Souris', 'Clavier', 'Écran', 'Casque'],
    'Catégorie': ['Informatique', 'Périphérique', 'Périphérique', 'Informatique', 'Audio'],
    'Prix': [899.99, 29.99, 79.99, 349.99, 149.99]
})

# Sauvegarde dans Excel
with pd.ExcelWriter('ventes_multi_feuilles.xlsx', engine='openpyxl') as writer:
    ventes_2023.to_excel(writer, sheet_name='Ventes_2023', index=False)
    ventes_2024.to_excel(writer, sheet_name='Ventes_2024', index=False)
    produits_info.to_excel(writer, sheet_name='Produits', index=False)

print("Fichier Excel créé avec 3 feuilles")

# Chargement des feuilles
ventes_2023_loaded = pd.read_excel('ventes_multi_feuilles.xlsx', sheet_name='Ventes_2023')
ventes_2024_loaded = pd.read_excel('ventes_multi_feuilles.xlsx', sheet_name='Ventes_2024')
produits_loaded = pd.read_excel('ventes_multi_feuilles.xlsx', sheet_name='Produits')

print(f"Ventes 2023: {ventes_2023_loaded.shape}")
print(f"Ventes 2024: {ventes_2024_loaded.shape}")
print(f"Produits: {produits_loaded.shape}")

# Fusion des ventes
ventes_2023_loaded['Année'] = 2023
ventes_2024_loaded['Année'] = 2024
ventes_combinees = pd.concat([ventes_2023_loaded, ventes_2024_loaded], ignore_index=True)
print(f"\nVentes combinées: {ventes_combinees.shape}")

# Jointure avec informations produits
ventes_completes = ventes_combinees.merge(produits_loaded, on='Produit_ID', how='left')
print(f"Ventes avec infos produits: {ventes_completes.shape}")
print(f"\nPremières lignes:")
print(ventes_completes.head())

# Sauvegarde finale
ventes_completes.to_excel('ventes_finales.xlsx', index=False)
print("\nFichier final sauvegardé: ventes_finales.xlsx")

# ----------------------------------------------------------------------------
# Exercice 3.3: Intégration multi-formats
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 3.3: Intégration multi-formats ---\n")

# CSV: Informations clients
clients_data = {
    'ID': range(1, 11),
    'Nom': ['Dupont', 'Martin', 'Bernard', 'Dubois', 'Thomas',
            'Robert', 'Richard', 'Petit', 'Durand', 'Leroy'],
    'Email': [f'client{i}@email.com' for i in range(1, 11)],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice',
              'Nantes', 'Bordeaux', 'Lille', 'Rennes', 'Strasbourg']
}
df_clients = pd.DataFrame(clients_data)
df_clients.to_csv('clients.csv', index=False)
print("Fichier clients.csv créé")

# JSON: Commandes
commandes_data = [
    {'Order_ID': i, 'Client_ID': np.random.randint(1, 11),
     'Date': f'2024-0{np.random.randint(1, 10)}-{np.random.randint(10, 29):02d}',
     'Montant': round(np.random.uniform(50, 500), 2)}
    for i in range(1, 21)
]
with open('commandes.json', 'w') as f:
    json.dump(commandes_data, f, indent=2)
print("Fichier commandes.json créé")

# Chargement des données
df_clients_loaded = pd.read_csv('clients.csv')
df_commandes = pd.read_json('commandes.json')

# Simulation lecture depuis presse-papier (en pratique: pd.read_clipboard())
produits_clipboard = pd.DataFrame({
    'Produit_ID': [1, 2, 3, 4, 5],
    'Nom_Produit': ['Produit_A', 'Produit_B', 'Produit_C', 'Produit_D', 'Produit_E'],
    'Prix': [19.99, 29.99, 39.99, 49.99, 59.99]
})

print(f"\nClients: {df_clients_loaded.shape}")
print(f"Commandes: {df_commandes.shape}")
print(f"Produits: {produits_clipboard.shape}")

# Combinaison des données
df_unifie = df_commandes.merge(df_clients_loaded, left_on='Client_ID', right_on='ID', how='left')
print(f"\nDataFrame unifié: {df_unifie.shape}")
print(df_unifie.head())

# Sauvegarde en trois formats
df_unifie.to_csv('donnees_unifiees.csv', index=False)
df_unifie.to_excel('donnees_unifiees.xlsx', index=False)
df_unifie.to_json('donnees_unifiees_records.json', orient='records', indent=2)
df_unifie.to_json('donnees_unifiees_columns.json', orient='columns', indent=2)
df_unifie.to_json('donnees_unifiees_index.json', orient='index', indent=2)

print("\nDonnées sauvegardées en CSV, Excel et JSON (3 orientations)")

# ============================================================================
# CHAPITRE 4: SÉLECTION ET INDEXATION
# ============================================================================

print("\n" + "=" * 80)
print("CHAPITRE 4: SÉLECTION ET INDEXATION")
print("=" * 80)

# ----------------------------------------------------------------------------
# Exercice 4.1: Sélection de colonnes et notation
# ----------------------------------------------------------------------------
print("\n--- Exercice 4.1: Sélection de colonnes ---\n")

# Création du DataFrame d'employés
np.random.seed(42)
employes_data = {
    'ID_Employe': range(1, 21),
    'Prenom': ['Jean', 'Marie', 'Pierre', 'Sophie', 'Luc', 'Emma', 'Paul', 
               'Julie', 'Marc', 'Anne', 'Thomas', 'Laura', 'David', 'Céline',
               'Nicolas', 'Sarah', 'Antoine', 'Camille', 'Julien', 'Léa'],
    'Nom': ['Dupont', 'Martin', 'Bernard', 'Dubois', 'Thomas', 'Robert',
            'Richard', 'Petit', 'Durand', 'Leroy', 'Moreau', 'Simon',
            'Laurent', 'Lefebvre', 'Michel', 'Garcia', 'David', 'Bertrand',
            'Roux', 'Vincent'],
    'Departement': ['IT', 'RH', 'IT', 'Finance', 'IT', 'Marketing', 'Finance',
                    'RH', 'IT', 'Marketing', 'Finance', 'IT', 'RH', 'Marketing',
                    'IT', 'Finance', 'RH', 'IT', 'Marketing', 'Finance'],
    'Poste': ['Développeur', 'RH Manager', 'DevOps', 'Comptable', 'Architecte',
              'Chef de Projet', 'Analyste', 'Assistant RH', 'Tech Lead',
              'Marketing Manager', 'Contrôleur', 'Développeur', 'Recruteur',
              'Designer', 'Data Scientist', 'Auditeur', 'Formateur',
              'Développeur', 'Community Manager', 'Trésorier'],
    'Salaire_Annuel': [45000, 55000, 52000, 48000, 75000, 62000, 50000, 38000,
                       68000, 58000, 51000, 47000, 42000, 54000, 72000, 49000,
                       44000, 46000, 40000, 53000],
    'Date_Embauche': pd.date_range('2015-01-01', periods=20, freq='6M'),
    'Performance_Score': np.random.uniform(6.0, 10.0, 20).round(1)
}

df_employes = pd.DataFrame(employes_data)
print("DataFrame créé avec 20 employés")
print(df_employes.head())

# Sélection d'une seule colonne (retourne une Series)
print("\n1. Sélection d'une colonne (Series):")
salaires = df_employes['Salaire_Annuel']
print(f"Type: {type(salaires)}")
print(f"Premières valeurs:\n{salaires.head()}")

# Sélection de plusieurs colonnes (retourne un DataFrame)
print("\n2. Sélection de plusieurs colonnes (DataFrame):")
info_base = df_employes[['Prenom', 'Nom', 'Departement']]
print(f"Type: {type(info_base)}")
print(info_base.head())

# Notation par point (quand possible)
print("\n3. Notation par point:")
print(f"Départements: {df_employes.Departement.unique()}")
# Note: Ne fonctionne pas si le nom contient des espaces ou caractères spéciaux

# Sous-ensembles avec différentes combinaisons
print("\n4. Différents sous-ensembles:")
print("\na) Informations salariales:")
print(df_employes[['Prenom', 'Nom', 'Salaire_Annuel', 'Performance_Score']].head())

print("\nb) Informations RH:")
print(df_employes[['ID_Employe', 'Prenom', 'Nom', 'Date_Embauche']].head())

print("\nc) Vue managériale:")
print(df_employes[['Departement', 'Poste', 'Salaire_Annuel', 'Performance_Score']].head())

# ----------------------------------------------------------------------------
# Exercice 4.2: Maîtrise de iloc et loc
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 4.2: Maîtrise de iloc et loc ---\n")

print("=== UTILISATION DE iloc (position numérique) ===\n")

# Première ligne
print("1. Première ligne:")
print(df_employes.iloc[0])

# 5 premières lignes
print("\n2. Les 5 premières lignes:")
print(df_employes.iloc[:5])

# Lignes d'index pairs
print("\n3. Lignes d'index pairs:")
print(df_employes.iloc[::2])

# Lignes 3 à 7
print("\n4. Lignes 3 à 7 (index 3 à 7):")
print(df_employes.iloc[3:8])

# Lignes non contiguës
print("\n5. Lignes non contiguës (0, 5, 10, 15):")
print(df_employes.iloc[[0, 5, 10, 15]])

# Combinaison lignes et colonnes
print("\n6. Lignes 0-4, colonnes 1-3:")
print(df_employes.iloc[0:5, 1:4])

print("\n\n=== UTILISATION DE loc (labels) ===\n")

# Définir un index personnalisé pour mieux démontrer loc
df_employes_indexed = df_employes.set_index('ID_Employe')

# Sélection par label
print("1. Employé ID 5:")
print(df_employes_indexed.loc[5])

# Plage de labels
print("\n2. Employés ID 5 à 10:")
print(df_employes_indexed.loc[5:10])

# Labels spécifiques
print("\n3. Employés ID 1, 5, 10, 15:")
print(df_employes_indexed.loc[[1, 5, 10, 15]])

# Combinaison lignes et colonnes
print("\n4. Employés 1-5, colonnes spécifiques:")
print(df_employes_indexed.loc[1:5, ['Prenom', 'Nom', 'Salaire_Annuel']])

# Toutes les lignes, colonnes spécifiques
print("\n5. Toutes les lignes, certaines colonnes:")
print(df_employes_indexed.loc[:, ['Departement', 'Poste', 'Salaire_Annuel']].head())

# ----------------------------------------------------------------------------
# Exercice 4.3: Filtrage conditionnel complexe
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 4.3: Filtrage conditionnel complexe ---\n")

# 1. IT avec salaire > 50000
print("1. Employés IT avec salaire > 50000€:")
filtre_it = df_employes[(df_employes['Departement'] == 'IT') & 
                         (df_employes['Salaire_Annuel'] > 50000)]
print(filtre_it[['Prenom', 'Nom', 'Departement', 'Salaire_Annuel']])

# 2. Embauchés après 2020 avec performance > 8
print("\n2. Embauchés après 2020 avec score > 8:")
filtre_perf = df_employes[(df_employes['Date_Embauche'] > '2020-01-01') & 
                          (df_employes['Performance_Score'] > 8.0)]
print(filtre_perf[['Prenom', 'Nom', 'Date_Embauche', 'Performance_Score']])

# 3. Utilisation de query()
print("\n3. Utilisation de query():")
result_query = df_employes.query('Salaire_Annuel > 50000 and Performance_Score >= 8.0')
print(result_query[['Prenom', 'Nom', 'Salaire_Annuel', 'Performance_Score']])

# 4. Utilisation de isin()
print("\n4. Employés dans IT, Finance ou Marketing:")
depts = ['IT', 'Finance', 'Marketing']
filtre_depts = df_employes[df_employes['Departement'].isin(depts)]
print(filtre_depts[['Prenom', 'Nom', 'Departement']].head(10))

# 5. Utilisation de between()
print("\n5. Salaires entre 45000 et 55000€:")
filtre_between = df_employes[df_employes['Salaire_Annuel'].between(45000, 55000)]
print(filtre_between[['Prenom', 'Nom', 'Salaire_Annuel']])

# 6. Utilisation de str.contains()
print("\n6. Employés dont le nom contient 'er':")
filtre_nom = df_employes[df_employes['Nom'].str.contains('er', case=False)]
print(filtre_nom[['Prenom', 'Nom']])

# ----------------------------------------------------------------------------
# Exercice 4.4: Sélection de cellules et blocs spécifiques
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 4.4: Sélection de cellules et blocs ---\n")

# Cellule spécifique avec loc
print("1. Cellule avec loc (ligne 5, colonne 'Prenom'):")
cellule_loc = df_employes_indexed.loc[5, 'Prenom']
print(f"Valeur: {cellule_loc}")

# Cellule avec iloc
print("\n2. Cellule avec iloc (ligne 4, colonne 1):")
cellule_iloc = df_employes.iloc[4, 1]
print(f"Valeur: {cellule_iloc}")

# Accès rapide avec at
print("\n3. Accès rapide avec at:")
valeur_at = df_employes_indexed.at[5, 'Salaire_Annuel']
print(f"Salaire de l'employé 5: {valeur_at}€")

# Accès rapide avec iat
print("\n4. Accès rapide avec iat:")
valeur_iat = df_employes.iat[4, 5]
print(f"Valeur à position [4, 5]: {valeur_iat}")

# Bloc rectangulaire
print("\n5. Bloc rectangulaire (lignes 5-10, Prenom à Salaire_Annuel):")
bloc = df_employes.loc[5:10, 'Prenom':'Salaire_Annuel']
print(bloc)

# Comparaison de performance
print("\n6. Comparaison de performance at/iat vs loc/iloc:")
import time

# Test avec at
start = time.time()
for i in range(1000):
    _ = df_employes_indexed.at[5, 'Salaire_Annuel']
temps_at = time.time() - start

# Test avec loc
start = time.time()
for i in range(1000):
    _ = df_employes_indexed.loc[5, 'Salaire_Annuel']
temps_loc = time.time() - start

print(f"Temps at: {temps_at:.4f}s")
print(f"Temps loc: {temps_loc:.4f}s")
print(f"at est {temps_loc/temps_at:.1f}x plus rapide")

# ============================================================================
# CHAPITRE 5: MANIPULATION DES DONNÉES
# ============================================================================

print("\n\n" + "=" * 80)
print("CHAPITRE 5: MANIPULATION DES DONNÉES")
print("=" * 80)

# ----------------------------------------------------------------------------
# Exercice 5.1: Ajout et calcul de colonnes
# ----------------------------------------------------------------------------
print("\n--- Exercice 5.1: Ajout et calcul de colonnes ---\n")

# Création du DataFrame de transactions
np.random.seed(42)
dates_trans = pd.date_range('2023-01-01', periods=100, freq='D')
transactions_data = {
    'Date': dates_trans,
    'Type_Transaction': np.random.choice(['Dépôt', 'Retrait'], 100, p=[0.4, 0.6]),
    'Montant': np.random.uniform(50, 500, 100).round(2),
    'Solde_Avant': 5000.0
}

df_trans = pd.DataFrame(transactions_data)

# Calcul du solde après
print("1. Calcul du Solde_Après:")
df_trans['Solde_Après'] = df_trans['Solde_Avant']
for i in range(len(df_trans)):
    if i > 0:
        df_trans.loc[i, 'Solde_Avant'] = df_trans.loc[i-1, 'Solde_Après']
    
    if df_trans.loc[i, 'Type_Transaction'] == 'Dépôt':
        df_trans.loc[i, 'Solde_Après'] = df_trans.loc[i, 'Solde_Avant'] + df_trans.loc[i, 'Montant']
    else:
        df_trans.loc[i, 'Solde_Après'] = df_trans.loc[i, 'Solde_Avant'] - df_trans.loc[i, 'Montant']

# Calcul des frais (méthode 1: assignation directe)
print("\n2. Calcul des frais (assignation directe):")
df_trans['Frais_Transaction'] = 0.0
df_trans.loc[df_trans['Type_Transaction'] == 'Retrait', 'Frais_Transaction'] = \
    df_trans['Montant'] * 0.02

# Calcul du montant net (méthode 2: avec apply)
print("\n3. Calcul du Montant_Net (avec apply):")
df_trans['Montant_Net'] = df_trans.apply(
    lambda row: row['Montant'] - row['Frais_Transaction'] 
    if row['Type_Transaction'] == 'Retrait' else row['Montant'],
    axis=1
)

# Extraction des composants de date (méthode 3: assign)
print("\n4. Extraction des composants temporels (avec assign):")
df_trans = df_trans.assign(
    Mois=df_trans['Date'].dt.month,
    Année=df_trans['Date'].dt.year,
    Jour=df_trans['Date'].dt.day,
    Jour_Semaine=df_trans['Date'].dt.day_name()
)

print("\nAperçu du DataFrame avec nouvelles colonnes:")
print(df_trans[['Date', 'Type_Transaction', 'Montant', 'Frais_Transaction', 
                'Montant_Net', 'Solde_Après', 'Mois']].head(10))

print(f"\nStatistiques des frais totaux: {df_trans['Frais_Transaction'].sum():.2f}€")

# ----------------------------------------------------------------------------
# Exercice 5.2: Modification conditionnelle de valeurs
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 5.2: Modification conditionnelle ---\n")

# Création du DataFrame de produits
np.random.seed(42)
produits_data = {
    'Nom': [f'Produit_{i}' for i in range(1, 51)],
    'Categorie': np.random.choice(['Électronique', 'Alimentaire', 'Vêtements', 
                                   'Maison', 'Sport'], 50),
    'Prix': np.random.uniform(10, 200, 50).round(2),
    'Stock': np.random.randint(10, 200, 50),
    'Fournisseur': np.random.choice(['Ancien_Nom', 'Fournisseur_B', 
                                     'Fournisseur_C'], 50)
}

df_produits = pd.DataFrame(produits_data)
print("DataFrame de produits créé:")
print(df_produits.head())

# 1. Augmentation des prix Électronique
print("\n1. Augmentation de 10% pour l'Électronique:")
df_produits.loc[df_produits['Categorie'] == 'Électronique', 'Prix'] *= 1.10
print(df_produits[df_produits['Categorie'] == 'Électronique'][['Nom', 'Categorie', 'Prix']].head())

# 2. Remise pour stock élevé
print("\n2. Remise de 5% pour stock > 100:")
df_produits.loc[df_produits['Stock'] > 100, 'Prix'] *= 0.95
print(f"Nombre de produits concernés: {(df_produits['Stock'] > 100).sum()}")

# 3. Remplacement de fournisseur
print("\n3. Remplacement Ancien_Nom → Nouveau_Nom:")
df_produits['Fournisseur'] = df_produits['Fournisseur'].replace('Ancien_Nom', 'Nouveau_Nom')
print(df_produits['Fournisseur'].value_counts())

# 4. Mapping des catégories
print("\n4. Conversion catégories en codes:")
mapping_cat = {
    'Électronique': 'E',
    'Alimentaire': 'A',
    'Vêtements': 'V',
    'Maison': 'M',
    'Sport': 'S'
}
df_produits['Code_Categorie'] = df_produits['Categorie'].map(mapping_cat)
print(df_produits[['Nom', 'Categorie', 'Code_Categorie']].head())

# 5. Standardisation avec replace
print("\n5. Standardisation de valeurs:")
df_produits['Fournisseur'] = df_produits['Fournisseur'].replace({
    'Fournisseur_B': 'Fournisseur B',
    'Fournisseur_C': 'Fournisseur C'
})
print(df_produits['Fournisseur'].unique())

# ----------------------------------------------------------------------------
# Exercice 5.3: Suppression stratégique
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 5.3: Suppression stratégique ---\n")

# Création d'un DataFrame clients volumineux
np.random.seed(42)
clients_data = {
    'Client_ID': range(1, 101),
    'Nom': [f'Client_{i}' for i in range(1, 101)],
    'Email': [f'client{i}@email.com' for i in range(1, 101)],
    'Ville': np.random.choice(['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice'], 100),
    'Age': np.random.randint(18, 70, 100),
    'Derniere_Commande': pd.date_range('2022-01-01', periods=100, freq='3D'),
    'Montant_Total': np.random.uniform(10, 1000, 100).round(2),
    'Nb_Commandes': np.random.randint(1, 50, 100),
    'Statut': np.random.choice(['Actif', 'Inactif'], 100),
    'Score_Credit': np.random.randint(300, 850, 100),
    'Col_1': range(100),
    'Col_2': range(100, 200),
    'Col_3': range(200, 300),
    'Col_4': range(300, 400),
    'Col_5': range(400, 500)
}

df_clients = pd.DataFrame(clients_data)
print(f"DataFrame initial: {df_clients.shape}")
print(df_clients.head())

# 1. Suppression de colonnes individuelles
print("\n1. Suppression d'une colonne:")
df_temp = df_clients.copy()
df_temp = df_temp.drop('Col_5', axis=1)
print(f"Après suppression de Col_5: {df_temp.shape}")

# 2. Suppression de plusieurs colonnes
print("\n2. Suppression de plusieurs colonnes:")
df_temp = df_clients.copy()
df_temp = df_temp.drop(['Col_1', 'Col_2', 'Col_3'], axis=1)
print(f"Après suppression de Col_1-3: {df_temp.shape}")

# 3. Suppression par index
print("\n3. Suppression de lignes par index:")
df_temp = df_clients.copy()
df_temp = df_temp.drop([0, 1, 2, 3, 4])
print(f"Après suppression des 5 premières lignes: {df_temp.shape}")

# 4. Suppression selon conditions
print("\n4. Suppression des clients inactifs depuis plus d'un an:")
df_temp = df_clients.copy()
date_limite = pd.Timestamp('2024-01-01') - pd.Timedelta(days=365)
df_temp = df_temp[df_temp['Derniere_Commande'] > date_limite]
print(f"Après filtrage: {df_temp.shape}")

print("\n5. Suppression des commandes < 10€:")
df_temp = df_clients.copy()
df_temp = df_temp[df_temp['Montant_Total'] >= 10]
print(f"Après filtrage: {df_temp.shape}")

# 6. Utilisation de inplace
print("\n6. Suppression avec inplace:")
df_temp = df_clients.copy()
nb_avant = len(df_temp)
df_temp.drop(['Col_4', 'Col_5'], axis=1, inplace=True)
print(f"Colonnes avant: {nb_avant}, après: {df_temp.shape[1]}")

# ----------------------------------------------------------------------------
# Exercice 5.4: Renommage et tri avancés
# ----------------------------------------------------------------------------
print("\n\n--- Exercice 5.4: Renommage et tri ---\n")

# DataFrame avec noms incohérents
desordonne_data = {
    'Nom Client': ['Dupont', 'Martin', 'Bernard', 'Dubois'],
    'PRÉNOM': ['Jean', 'Marie', 'Pierre', 'Sophie'],
    'age employé': [35, 28, 42, 31],
    'Salaire Annuel €': [45000, 52000, 48000, 55000],
    'Date embauche': ['2020-01-15', '2021-03-20', '2019-07-10', '2022-02-28']
}

df_desordonne = pd.DataFrame(desordonne_data)
print("DataFrame désorganisé:")
print(df_desordonne)

# Renommage en snake_case
print("\n1. Renommage en snake_case:")
df_propre = df_desordonne.copy()
df_propre.columns = df_propre.columns.str.lower()
df_propre.columns = df_propre.columns.str.replace(' ', '_')
df_propre.columns = df_propre.columns.str.replace('é', 'e')
df_propre.columns = df_propre.columns.str.replace('€', '')
print(df_propre)

# Renommage individuel
print("\n2. Renommage manuel:")
df_propre = df_propre.rename(columns={
    'nom_client': 'nom',
    'prenom': 'prenom',
    'age_employe': 'age',
    'salaire_annuel_': 'salaire',
    'date_embauche': 'date_embauche'
})
print(df_propre)

# Tri par une colonne
print("\n3. Tri par salaire (croissant):")
df_trie = df_propre.sort_values('salaire')
print(df_trie)

print("\n4. Tri par salaire (décroissant):")
df_trie = df_propre.sort_values('salaire', ascending=False)
print(df_trie)

print("\n5. Tri par plusieurs colonnes:")
df_trie = df_propre.sort_values(['age', 'salaire'], ascending=[True, False])
print(df_trie)

print("\n6. Tri par index:")
df_trie = df_propre.sort_index()
print(df_trie)

print("\n" + "=" * 80)
print("Suite des corrections: Chapitres 6-12 à suivre...")
print("=" * 80)