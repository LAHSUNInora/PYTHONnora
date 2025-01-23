""" Écrivez un programme qui demande à l'utilisateur de saisir un fichier, puis un entier. Utilisez les 
concepts de gestion des exceptions pour garantir que le fichier est lu avec succès et que l'entier est 
valide. Gérer toutes les exceptions appropriées et afficher des messages utiles"""


def read_file(filename):
    """
    Tente de lire le contenu d'un fichier. Si le fichier n'existe pas,
    enregistre l'erreur et lève une exception.
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("le fichier  n'a pas été trouvé .")

def get_positive_integer():
    """
    Demande à l'utilisateur de saisir un entier positif.
    Continue jusqu'à ce qu'une saisie valide soit fournie.
    """
    while True:
        try:
            user_input = input("Veuillez saisir un entier positif : ")
            value = int(user_input)
            if value <= 0:
                raise ValueError("Le nombre doit être strictement positif.")
            return value
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

def main():
    """
    Programme principal qui combine la lecture de fichier et la saisie d'un entier.
    """
    print("=== Programme de gestion des fichiers et des entiers ===")

    # Étape 1 : Lecture du fichier
    while True:
        try:
            filename = input("Veuillez entrer le nom du fichier à lire : ")
            file_content = read_file(filename)
            print("\nContenu du fichier :")
            print(file_content)
            break
        except FileNotFoundError as e:
            print(e)
            print("Veuillez réessayer avec un fichier valide.")

    # Étape 2 : Saisie d'un entier positif
    positive_integer = get_positive_integer()
    print(f"\nVous avez saisi l'entier positif : {positive_integer}")

    print("\n=== Fin du programme ===")

# Exécution du programme
if __name__ == "__main__":
    main()