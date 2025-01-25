import unittest
from src.mat_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    """
    Classe de tests unitaires pour les fonctions du module math_operations.

    Cette classe contient des tests pour les fonctions suivantes :
    - add : Additionner deux nombres.
    - subtract : Soustraire un nombre d'un autre.
    - multiply : Multiplier deux nombres.
    - divide : Diviser un nombre par un autre.
    """

    def test_add(self):
        """
        Teste la fonction add.

        Vérifie que la somme de deux nombres est correcte.
        """
        self.assertEqual(add(2, 3), 5)  # 2 + 3 doit être égal à 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 doit être égal à 0
        self.assertEqual(add(0, 0), 0)  # 0 + 0 doit être égal à 0

    def test_divide(self):
        """
        Teste la fonction divide.

        Vérifie que la division retourne les résultats corrects
        et que la division par zéro lève une exception ValueError.
        """
        self.assertEqual(divide(10, 2), 5)  # 10 / 2 doit être égal à 5
        self.assertEqual(divide(9, 3), 3)  # 9 / 3 doit être égal à 3

        # Teste si une division par zéro lève une exception
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    # Lancer tous les tests définis dans la classe
    unittest.main()
