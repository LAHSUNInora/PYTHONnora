class Produit:
    def __init__(self, nom, prix):
        self._nom = nom  
        self._prix = prix  
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, value):
        if isinstance(value, str) and value != "":
            self._nom = value
        else:
            raise ValueError("Le nom doit être une chaîne non vide.")
    # Propriétés pour le prix du produit
    @property
    def prix(self):
        return self._prix
    @prix.setter
    def prix(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._prix = value
        else:
            raise ValueError("Le prix doit être un nombre positif.")

    def afficher(self):
        print(f"Produit: {self.nom}, Prix: {self.prix:.2f} dh")
class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit  
        self.quantite = quantite  
    @property
    def total(self):
        return self.produit.prix * self.quantite
    def afficher(self):
        print(f"Commande: {self.produit.nom}, Quantité: {self.quantite}, Total: {self.total:.2f} dh")
class Panier:
    def __init__(self):
        self.commandes = []  
    def ajouter_commande(self, commande):
        self.commandes.append(commande)
    @property
    def total(self):
        return sum(commande.total for commande in self.commandes)
    def afficher(self):
        print("Liste des commandes dans le panier :")
        for commande in self.commandes:
            commande.afficher()
        print(f"Total du panier: {self.total:.2f} dh")  
# Créer des produits
produit1 = Produit('telephone', 1000)
produit2 = Produit('iphone', 2000)

# Créer des commandes
commande1 = Commande(produit1, 3)
commande2 = Commande(produit2, 5)

# Créer un panier et ajouter des commandes
panier = Panier()
panier.ajouter_commande(commande1) 
panier.ajouter_commande(commande2)  
panier.afficher()