from abc import ABC, abstractmethod
import math

# Classe abstraite Forme
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

# Classe Cercle
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * (self.rayon ** 2)  # Retour de la surface

# Classe Rectangle
class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_surface(self):
        return self.largeur * self.longueur  # Retour de la surface

# Création des objets
cercle1 = Cercle(6)
rectangle1 = Rectangle(6, 7)

# Impression des résultats
print(f"Surface du cercle : {cercle1.calculer_surface():.2f}")
print(f"Surface du rectangle : {rectangle1.calculer_surface():.2f}")