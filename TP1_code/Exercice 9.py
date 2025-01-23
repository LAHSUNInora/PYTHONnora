# Exercice 09 :
texte = "je suis l'étudiante LAHSUNI Nora en master IIES Groupe2  "
def analyse_texte(texte):
    texte = texte.strip()
    mots = texte.split()
    nombre_de_mots = len(mots)
    nombre_de_caracteres = len(texte.replace(" "," "))
    
    return{"nombre_de_mots": nombre_de_mots, "nombre_de_caracteres" : nombre_de_caracteres}
print(analyse_texte(texte))