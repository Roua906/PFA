import pandas as pd

df = pd.read_csv('ventes.csv')

# =========================
# CHECK SI FICHIER VIDE
# =========================
if df.empty:
    print("❌ Le fichier ventes.csv est vide !")
    exit()   
   
