

def dollars_to_dirhams(dollars):
    """
    Convertit une somme en dollars en dirhams marocains.

    Args:
        dollars (float): Le montant en dollars à convertir.

    Returns:
        float: Le montant converti en dirhams marocains.
    
    Exemple:
        >>> dollars_to_dirhams(1)
        10.5
    """
    # Taux de conversion actuel (1 dollar = 10.5 dirhams)
    taux = 10.5
    return dollars * taux


def meters_to_kilometers(meters):
    """
    Convertit une distance en mètres en kilomètres.

    Args:
        meters (float): La distance en mètres.

    Returns:
        float: La distance convertie en kilomètres.
    
    Exemple:
        >>> meters_to_kilometers(1000)
        1.0
    """
    # Conversion : 1 kilomètre = 1000 mètres
    return meters / 1000
