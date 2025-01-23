phrase1= input("tu peut entrez le premier phrase.")
phrase2= input("tu peut entrez la deuxemee phrase.")
phrase3= input("tu peut entrez la troisieme phrase.")
with open ("phrases.txt","w") as fichier:
    fichier.writelines(phrase1+"\n")
    fichier.writelines(phrase2+"\n")
    fichier.writelines(phrase3+"\n")
