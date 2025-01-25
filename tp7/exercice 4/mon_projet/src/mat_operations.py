def add(a, b):
    """
    Additionne deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La somme des deux nombres.
    
    Exemple:
        >>> add(2, 3)
        5
    """
    # Retourne la somme des deux arguments
    return a + b


def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La différence entre les deux nombres.
    
    Exemple:
        >>> subtract(5, 3)
        2
    """
    # Retourne la différence entre les deux arguments
    return a - b


def multiply(a, b):
    """
    Multiplie deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: Le produit des deux nombres.
    
    Exemple:
        >>> multiply(4, 3)
        12
    """
    # Retourne le produit des deux arguments
    return a * b


def divide(a, b):
    """
    Divise le premier nombre par le deuxième.

    Args:
        a (float): Le numérateur.
        b (float): Le dénominateur (doit être différent de 0).

    Returns:
        float: Le résultat de la division.

    Raises:
        ValueError: Si le dénominateur est égal à 0.
    
    Exemple:
        >>> divide(10, 2)
        5.0
    """
    # Vérifie que le dénominateur n'est pas nul
    if b == 0:
        raise ValueError("Division par zéro!")  # Lève une exception en cas de division par zéro

    # Retourne le quotient des deux arguments
    return a / b
