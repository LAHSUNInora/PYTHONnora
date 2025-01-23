class Voiture:
  def __init__(self,marque,modele,annee):
    self.marque=marque
    self.modele=modele
    self.annee=annee
  def afficher_info(self):
    print("la marque : "+self.marque+"-------------- le modéle : " +self.modele+" ------------ lannée c est : "+ str(self.annee))
    #on peut aussi utiliser Autre Méthode pour afficher les informations on utilisons format
    #print("la marque :{} , le modéle : {} , l'année c'est :{} ".format(self.marque , self.modele , self.annee))

#création des plusieurs instances de la classe voiture 
V1 = Voiture ("Tessla","modele 3",2022)
V2 = Voiture("BMW","modele M",2024)
V3 = Voiture ("mersidis","modele r",2020)
V4 = Voiture("honday","modele t",2023)
V1.afficher_info()
V2.afficher_info()
V3.afficher_info()
V4.afficher_info()
