import logging

# Configuration du module logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message):
    """
    Enregistre un message d'erreur dans le fichier error.log.
    """
    logging.error(message)

def read_file(filename):
    """
    Tente de lire le contenu d'un fichier. Si le fichier n'existe pas,
    enregistre l'erreur dans un fichier log et affiche un message.
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        error_message = f"Erreur : le fichier '{filename}' n'a pas été trouvé."
        print(error_message)
        log_error(error_message)
    finally:
        print("Bloc finally exécuté, que l'erreur se produise ou non.")

# Exemple d'utilisation
read_file("fichier_inexistant.txt")