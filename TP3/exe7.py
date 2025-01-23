from abc import ABC, abstractmethod
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass
class Voiture(Vehicule):
    def deplacer(self):
        return "La voiture roule sur la route."
class Bicyclette(Vehicule):
    def deplacer(self):
        return "La bicyclette pédale sur la piste cyclable."
# Test des classes Voiture et Bicyclette
voiture = Voiture()
bicyclette = Bicyclette()
print(voiture.deplacer())
print(bicyclette.deplacer())