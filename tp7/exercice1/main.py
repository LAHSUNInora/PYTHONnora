from conversion import dollars_to_dirhams, meters_to_kilometers

# Script principal pour tester les fonctions de conversion

def main():
    """
    Fonction principale pour tester les conversions de devises et de distances.
    
    Cette fonction utilise les fonctions `dollars_to_dirhams` et 
    `meters_to_kilometers` importées depuis le module `conversion.py`.
    """
    # Conversion de dollars en dirhams
    dollars = 2455
    print(f"{dollars} dollars = {dollars_to_dirhams(dollars)} dirhams.")

    # Conversion de mètres en kilomètres
    meters = 2008
    print(f"{meters} mètres = {meters_to_kilometers(meters)} kilomètres.")

if __name__ == "__main__":
    # Exécuter la fonction principale
    main()
