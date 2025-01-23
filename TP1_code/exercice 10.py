#Exercice 10 :
def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()
    for cle, valeur in dict2.items():
        if cle in fusion:
            fusion[cle] += valeur
        else:
            fusion[cle] = valeur
    return fusion
dict1 = {"Nora":4, "Aya":2, "Imane":6}
dict2 = {"Aya":2, "Nora":1, "mama":9}
print(fusionner_dicts(dict1,dict2))