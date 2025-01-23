import csv
donnees=[["Nom","Age","Ville"],
         ["Alice",30,"Paris"],
         ["Bob",25,"Lyon"]]
with open ('contacts.csv','w',newline='')as fichier:
    ecrir=csv.writer(fichier)
    ecrir.writerows(donnees)
with open ('contacts.csv','r',newline='')as fichier:  
    lecture = csv.reader(fichier) 
    for ligne in lecture:
        print(ligne)
