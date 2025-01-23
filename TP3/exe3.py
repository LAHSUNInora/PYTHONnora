from abc import ABC, abstractmethod
import math
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self, rayon):  
        self.rayon = rayon

    def calculer_surface(self):
        return math.pi * (self.rayon ** 2)
class Rectangle(Forme):
    def __init__(self, largeur, longueur): 
        self.largeur = largeur
        self.longueur = longueur
    def calculer_surface(self):
        return self.largeur * self.longueur
def afficher_surface(formes):
    for forme in formes:
        surface = forme.calculer_surface()
        print(f"Surface de {type(forme).__name__} : {surface:.2f}")
cercle1 = Cercle(6)
rectangle1 = Rectangle(6, 7)
print(f"Surface du cercle1 : {cercle1.calculer_surface():.2f}")
print(f"Surface du rectangle1 : {rectangle1.calculer_surface():.2f}")
# Création d'autres formes
cercle2 = Cercle(5)
rectangle2 = Rectangle(4, 6) 
formes = [cercle2, rectangle2]
afficher_surface(formes)
