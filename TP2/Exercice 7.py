class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
class Bibliotheque:
    def __init__(self):
        self.livres = []
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté à la bibliothèque.")
    def afficher_livres(self):
        print("Livres dans la bibliothèque :")
        for livre in self.livres:
            print(f"- {livre.titre} par {livre.auteur} (Publié en {livre.annee_publication})")
# Création d'une instance de Bibliotheque
biblio = Bibliotheque()
# Création de deux instances de Livre
livre1 = Livre("la boit a merveil", "safrioui", 1949)
livre2 = Livre("mis", "victor hugo", 1943)
# Ajout des livres à la bibliothèque
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
# Affichage des livres de la bibliothèque
biblio.afficher_livres()

