from conversion import dollars_to_dirhams, meters_to_kilometers
import unittest

class TestConversion(unittest.TestCase):
    """
    Classe de test pour le module conversion.py.

    Cette classe contient des tests unitaires pour vérifier les fonctions
    dollars_to_dirhams et meters_to_kilometers.
    """

    try:
        def test_dollars_to_dirhams(self):
            """
            Teste la conversion de dollars en dirhams.

            Vérifie si la fonction dollars_to_dirhams retourne les résultats
            attendus pour des cas simples.
            """
            self.assertEqual(dollars_to_dirhams(1), 10.5)  # Test avec 1 dollar
            self.assertEqual(dollars_to_dirhams(0), 0)    # Test avec 0 dollar

        def test_meters_to_kilometers(self):
            """
            Teste la conversion de mètres en kilomètres.

            Vérifie si la fonction meters_to_kilometers retourne les résultats
            attendus pour des cas simples.
            """
            self.assertEqual(meters_to_kilometers(1000), 1)  # Test avec 1000 mètres
            self.assertEqual(meters_to_kilometers(0), 0)     # Test avec 0 mètre

        # Indique si tous les tests ont réussi
        print("Everything seems good")

    except Exception as e:
        # Affiche une erreur si une exception est levée
        print(f"Error: {e}")

if __name__ == '__main__':
    # Lancer les tests unitaires
    unittest.main()
