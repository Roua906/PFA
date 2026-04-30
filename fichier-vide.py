import pandas as pd

fichier = r"C:\Users\Lenovo\OneDrive\Desktop\PFA\PFA-1\ventes.csv"

try:
    df = pd.read_csv(fichier)
    print("Fichier lu avec succès !")
    print(df.head())
except pd.errors.EmptyDataError:
    print("Le fichier est vide ! Ajoute des données dedans.")
except FileNotFoundError:
    print("Le fichier n'existe pas à cet endroit.")
