with open ("exemple.txt","r") as fichier:
    lignes = fichier.readlines()
    for i, ligne in enumerate(lignes, start=1):  # Ajouter un compteur, en commençant par 1
            print(f"Ligne {i}: {ligne.strip()}") 