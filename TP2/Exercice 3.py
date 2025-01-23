class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
        return self.solde
    def retirer(self,montant):
        if (self.solde >= montant):
            self.solde -= montant
        else :
            print("le solde est suffisante pour effecture cette opération ")
    def affichier_solde(self):
        print("votre solde est "+ str(self.solde)+ " dh")
# création d'une instance de la clasee CompteBancaire pour faire le teste des méthodes
Compte1 = CompteBancaire("imane",7000)
Compte2 = CompteBancaire("wissal",8000)
Compte1.deposer(2000)
Compte2.retirer(5000)
Compte1.affichier_solde()
Compte2.affichier_solde()
# test si la condition dans la méthode retirer est bien travaillé
Compte2.retirer(4000)