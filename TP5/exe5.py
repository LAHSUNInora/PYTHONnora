import json
donnees = {
    "etudiants": [
        {"Nom": "Alice", "Age": 30, "Ville": "Paris"},
        {"Nom": "Bob", "Age": 25, "Ville": "Lyon"},
        {"Nom": "nora", "Age": 20, "Ville": "Agadir"}
    ]
}

with open ('etudiants.json','w') as fichier:
    json.dump(donnees,fichier,indent=4)
with open ('etudiants.json','r') as fichier: 
    donnees = json.load(fichier) 
    print(donnees)
   