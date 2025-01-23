# Exercice 08 :
def sum (*args):
    somme = 0
    for i in args :
        somme += i
    return somme 
print("la somme des arguments prend est : ", sum(2,55,3,88))