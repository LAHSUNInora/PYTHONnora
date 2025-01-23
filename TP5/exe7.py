phrase1= input("tu peut entrez le premier phrase.")
phrase2= input("tu peut entrez la deuxemee phrase.")
phrase3= input("tu peut entrez la troisieme phrase.")
with open ("journal.txt","w") as fichier:
    fichier.writelines(phrase1+"\n")
    fichier.writelines(phrase2+"\n")
    fichier.writelines(phrase3+"\n")
import shutil 
source= "journal.txt"
destination="journal_copie.txt"
try:
    shutil.copy(source,destination)
    print(f"Fichier copie de {source} a {destination}.")
except FileNotFoundError:
    print("Le fichier source n'a pas ete trouver.") 
except IOError:
    print("Erreur lors de la copie du fichier.")   
import shutil 
source= "journal.txt"
destination= "archives/ journal_deplace.txt"
try:
    shutil.move(source,destination)
    print(f"Fichier deplacer de {source} a {destination}.")
except FileNotFoundError:
    print("Le fichier source n'a pas ete trouver.") 
except IOError:
    print("Erreur lors du deplacement du fichier.")  