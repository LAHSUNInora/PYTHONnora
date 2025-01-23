class Personne:
    # Constructeur pour initialiser les attributs
    def __init__(self, nom, prenom, age):  
        self._nom = nom
        self._prenom = prenom
        self._age = age

    # Getter et Setter pour _nom
    def getNom(self):
        return self._nom

    def setNom(self, nom):
        self._nom = nom

    # Getter et Setter pour _prenom
    def getPrenom(self):
        return self._prenom

    def setPrenom(self, prenom):
        self._prenom = prenom

    # Getter et Setter pour _age
    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    # Méthode pour afficher les informations de la personne
    def afficher(self):
        return f"Votre nom est {self._nom} {self._prenom}, votre âge est {self._age} ans."

# Création d'une instance de la classe Personne
etud = Personne("LAHSUNI", "NORA", 21)

# Affichage des informations
print(etud.afficher())