import pandas as pd

# =========================
# 1. LECTURE DYNAMIQUE
# =========================
# يقرا أي fichier CSV فيه données (حتى 1000+ lignes)
df = pd.read_csv('ventes.csv')

print(" Aperçu des données :")
print(df.head())

# =========================
# 2. CALCUL DU CA BRUT
# =========================
df['CA_Brut'] = df['Prix'] * df['Quantité']

# =========================
# 3. REMISE
# =========================
df['Montant_Remise'] = df['CA_Brut'] * (df['Remise'] / 100)

# =========================
# 4. CA NET
# =========================
df['CA_Net'] = df['CA_Brut'] - df['Montant_Remise']

# =========================
# 5. TVA
# =========================
df['TVA'] = df['CA_Net'] * 0.20

# =========================
# 6. RÉSULTATS GLOBAUX
# =========================
ca_total = df['CA_Net'].sum()

meilleur_produit = df.loc[df['CA_Net'].idxmax(), 'ID']
meilleur_ca = df['CA_Net'].max()

# =========================
# 7. AFFICHAGE
# =========================
print("\n" + "="*50)
print(" RÉSULTATS DE L'ANALYSE DES VENTES")
print("="*50)

print(df[['ID', 'Prix', 'Quantité', 'Remise', 'CA_Brut', 'CA_Net', 'TVA']].head(10))

print("\n" + "-"*50)
print(f" CA Total de l'entreprise : {ca_total:.2f} €")
print(f" Meilleur produit : ID {meilleur_produit} ({meilleur_ca:.2f} €)")
print("="*50)

# =========================
# 8. EXPORT RÉSULTAT
# =========================
df.to_csv('resultats_final.csv', index=False)
print("\n Fichier resultats_final.csv créé avec succès")