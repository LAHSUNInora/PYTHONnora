# Définition de la classe "Personne"
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def ajouter_ami(self, ami):
        self.amis.append(ami)
        print(f"{ami} a été ajouté à la liste des amis de {self.prenom}.")

    def afficher_amis(self):
        print(f"Amis de {self.prenom} : {', '.join(self.amis) if self.amis else 'Aucun ami'}")# Test de la classe Personne
# Création d'une instance de Personne
pers = Personne("Nora", "LAHSUNI", 21)

# Ajout d'amis
pers.ajouter_ami("IMANE")
pers.ajouter_ami("NAOUAL")

# Affichage des amis
pers.afficher_amis()




