# Classe de base représentant un véhicule générique
class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    # Méthode pour afficher les informations du véhicule
    def afficher_info(self):
        print(f"La marque : {self.marque}")
        print(f"Le modèle : {self.modele}")
        print(f"L'année : {self.annee}")

# Classe représentant les caractéristiques d'un moteur
class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    # Méthode pour afficher les informations du moteur
    def afficher_info(self):
        print(f"La puissance : {self.puissance} chevaux")
        print(f"Le type de moteur : {self.type_moteur}")

# Classe représentant une voiture, héritant de Vehicule et Moteur
class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    # Méthode pour afficher les informations de la voiture
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_info(self)
        print(f"Nombre de places : {self.nombre_de_places}")

# Classe représentant une moto, héritant de Vehicule et Moteur
class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    # Méthode pour afficher les informations de la moto
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_info(self)
        print(f"Type de moto : {self.type_moto}")

# Création d'une instance de la classe Voiture avec des valeurs spécifiques
voiture = Voiture("Mercedes", "w201", 2000, 120, "Essence", 6)

# Création d'une instance de la classe Moto avec des valeurs spécifiques
moto = Moto("Tmax", "Tiger", 2020, 120, "Essence", "Sport")

# Affichage des informations de la voiture
print("Les informations de la Voiture sont :")
voiture.afficher_info()

# Affichage des informations de la moto
print("Les informations de la Moto sont :")
moto.afficher_info()

