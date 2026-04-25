import pandas as pd
## import matplotlib.pyplot as plt##

# Étape 1 : Création du fichier CSV (simulée ici)
# Vous pouvez aussi créer manuellement le fichier
data = {}
df = pd.DataFrame(data)

# Sauvegarde en CSV
df.to_csv('ventes.csv', index=False)
print(" Fichier ventes.csv créé")

# Lecture du fichier
df = pd.read_csv('ventes.csv')

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
print("\n" + "="*50)
print("RÉSULTATS DE L'ANALYSE")
print("="*50)
print(df[['ID', 'Prix', 'Quantité', 'Remise', 'CA_Brut', 'CA_Net', 'TVA']])
print("\n" + "-"*50)
print(f"CA Total de l'entreprise : {ca_total:.2f} €")
print(f"Produit avec le plus gros bénéfice : ID {meilleur_produit} ({meilleur_ca:.2f} €)")
print("="*50)

# Étape 7 : Export du fichier final
df.to_csv('resultats_final.csv', index=False)
print("\n Fichier resultats_final.csv créé")

# BONUS : Graphique avec Matplotlib
#plt.figure(figsize=(10, 6))
#bars = plt.bar(df['ID'].astype(str), df['CA_Net'], color='skyblue', edgecolor='navy')
#plt.xlabel('ID du Produit')
#plt.ylabel('Chiffre d\'Affaires Net (€)')
#plt.title('CA Net par Produit')
#plt.grid(axis='y', alpha=0.3)

# Ajout des valeurs sur les barres
#for bar, value in zip(bars, df['CA_Net']):
   # plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            # f'{value:.1f}€', ha='center', va='bottom')

#plt.tight_layout()
#plt.savefig('graphique_ca.png')
#plt.show()
#print("✅ Graphique sauvegardé : graphique_ca.png")