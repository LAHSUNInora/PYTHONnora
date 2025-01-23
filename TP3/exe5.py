class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher(self):
        return f"Employé : {self.nom} {self.prenom}, Salaire : {self.salaire:.2f} dh"

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = []  
    def ajouter_employe(self, employe):
        self.employes_supervises.append(employe)

    def afficher_employes_supervises(self):
        print(f"Manager : {self.nom} {self.prenom}")
        for employe in self.employes_supervises:
            print(f" - {employe.afficher()}")

# Test des classes Employe et Manager
employe1 = Employe("ELHILALI", "NAOUAL", 19000)
employe2 = Employe("barat", "imane", 19100)
manager = Manager("LAHSUNI", "NORA", 20000)
manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)
manager.afficher_employes_supervises()
