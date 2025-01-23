import os 
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"
try: 
    os.rename(ancien_nom,nouveau_nom)
    print(f"Fichier renomme en {nouveau_nom}.")
except FileNotFoundError:
    print("le fichier renommer n'a pas ete trouver.") 
except IOError:
    print("Erreur lors du renommage du fichier.") 