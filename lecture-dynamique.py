import random
import matplotlib.pyplot as plt
import pandas as pd

# On prépare 1000 lignes de données
lignes = []

for i in range(1, 1000):
    lignes.append({
        'ID': 1000 + i,                   # IDs de 1001 à 4000
        'Prix': round(random.uniform(5.0, 500.0), 2),  # Prix entre 5 et 500 DT
        'Quantité': random.randint(1, 50),             # Quantité entre 1 et 50
        'Remise': random.choice([0, 5, 10, 15, 20, 30])  # Remises variées
    })
    # Création du fichier ventes.csv avec l'en-tête [cite: 12]
df = pd.DataFrame(lignes)
df.to_csv('ventes.csv', index=False)

print(f"Succès ! Le fichier 'ventes.csv' contient maintenant {len(df)} lignes.")

# Étape 2 : Calcul du CA Brut
df['CA_Brut'] = df['Prix'] * df['Quantité']

# Étape 3 : Application des remises
df['Montant_Remise'] = df['CA_Brut'] * (df['Remise'] / 100)
df['CA_Net'] = df['CA_Brut'] - df['Montant_Remise']

# Étape 4 : Calcul de la TVA
df['TVA'] = df['CA_Net'] * 0.20

# Étape 5 : CA Total
ca_total = df['CA_Net'].sum()

# Étape 6 : Produit avec le plus gros bénéfice
meilleur_produit = df.loc[df['CA_Net'].idxmax(), 'ID']
meilleur_ca = df['CA_Net'].max()

# Affichage des résultats
print("\n" + "=" * 50)
print("RÉSULTATS DE L'ANALYSE")
print("=" * 50)
print(df[['ID', 'Prix', 'Quantité', 'Remise', 'CA_Brut', 'CA_Net', 'TVA']])
print("\n" + "-" * 50)
print(f"CA Total de l'entreprise : {ca_total:.2f} €")
print(f"Produit avec le plus gros bénéfice : ID {meilleur_produit} ({meilleur_ca:.2f} €)")
print("=" * 50)

# Étape 7 : Export du fichier final
df.to_csv('resultats_final.csv', index=False)
print("\n Fichier resultats_final.csv créé")

# BONUS : Graphique avec Matplotlib
plt.figure(figsize=(15, 8))
# Trier par CA Net et prendre les 10 premiers
top_produits = df.sort_values(by='CA_Net', ascending=False).head(10)
print(df.columns)
plt.bar(top_produits['ID'], top_produits['CA_Net'])
plt.xlabel('ID du Produit')
plt.ylabel('Chiffre d\'Affaires Net (€)')
plt.title('CA Net par Produit')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('graphe.png')
plt.show()
print(" Graphique sauvegardé : graphe.png")
#  Lecture dynamique

try:
    # On lit le fichier qui existe déjà
    df = pd.read_csv('ventes.csv')
    print(f"Succès : Le fichier a été lu. Nombre de lignes : {len(df)}")
except FileNotFoundError:
    print("Erreur : Le fichier 'ventes.csv' est introuvable !")
