class Personne:
    def __init__(self,nom , prenom , age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        print("My name is : {} {} and I'm {} years old ". format(self.nom , self.prenom ,self.age))

class Etudiant(Personne):
    def __init__(self, nom , prenom , age , matricule ):
        super().__init__(nom , prenom , age)
        self.matricule = matricule
    def etudier(self):
        print(f"etudiant(e) {self.nom} {self.prenom} est : {self.matricule}") 
        
        
#faire des testes sur la classe principale Personne et sur la sous classe Etudian,t

personne1 = Personne("LAHSUNI","NORA",21)
etudiant1 = Etudiant("BARAKAT","IMANE",21,"math")
personne1.se_presenter()
etudiant1.se_presenter()
etudiant1.etudier()

         
