#Exercice 04 :
list = ['Nora','Aya','Imane','Nora','Nora','Aya']
def compte_occurences(list):
    dictionnaire = {}
    for i in list :
        dictionnaire[i] = list.count(i)
    return dictionnaire
print(compte_occurences(list))