def concatenate(str1, str2):
    """
    Concatène deux chaînes de caractères.

    Args:
        str1 (str): La première chaîne de caractères.
        str2 (str): La deuxième chaîne de caractères.

    Returns:
        str: Une chaîne résultant de la concaténation des deux chaînes.
    
    Exemple:
        >>> concatenate("Bonjour, ", "monde!")
        'Bonjour, monde!'
    """
    # Combine les deux chaînes en une seule
    return str1 + str2


def to_uppercase(string):
    """
    Convertit une chaîne de caractères en majuscules.

    Args:
        string (str): La chaîne de caractères à convertir.

    Returns:
        str: La chaîne convertie en majuscules.
    
    Exemple:
        >>> to_uppercase("bonjour")
        'BONJOUR'
    """
    # Transforme tous les caractères de la chaîne en majuscules
    return string.upper()
