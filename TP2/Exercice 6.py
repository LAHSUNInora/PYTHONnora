class Rectangle:
    def __init__(self,largeur,longeur):
        self.largeur = largeur
        self.longeur = longeur
    def calculer_surface(self):
        return self.largeur * self.longeur
    def calculer_perimetre(self):
        p = (self.largeur + self.longeur)*2
        return p
R1 = Rectangle(12 , 5)
print("le surface de cet Rectangle est :" , R1.calculer_surface())
print ("le perimetre est :" , R1.calculer_perimetre())