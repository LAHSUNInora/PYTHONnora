def statistiques_fichier(nom_fichier):
    try:
       
        with open(nom_fichier, "r") as fichier:
            lignes = fichier.readlines()
        
        # Calcul des statistiques
        total_lignes = len(lignes)
        total_mots = sum(len(ligne.split()) for ligne in lignes)
        total_caracteres = sum(len(ligne) for ligne in lignes)
        print(f"Statistiques pour le fichier '{nom_fichier}':")
        print(f"- Nombre total de lignes : {total_lignes}")
        print(f"- Nombre total de mots : {total_mots}")
        print(f"- Nombre total de caracteres : {total_caracteres}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    
nom_fichier = "exemple.txt"


statistiques_fichier(nom_fichier)
