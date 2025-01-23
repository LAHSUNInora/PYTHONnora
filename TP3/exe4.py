class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom       
        self.__prix = prix     
    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    def get_prix(self):
        return self.__prix
    def set_prix(self, prix):
        self.__prix = prix
    def calculer_prix_remise(self, remise):
        """Applique une remise si le prix est supérieur à 100."""
        if self.__prix > 100:
            return self.__prix * (1 - remise / 100)
        return self.__prix
# Test de la classe Produit
produit = Produit("Ordinateur", 7000)
print(f"Prix avec remise : {produit.calculer_prix_remise(10):.2f} dh")  
