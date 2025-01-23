# exercice 05 :
while True :
    n = int(input("veuillez saisir la valeur de N : "))
    if n>=0 :
        break
def factorielle (n):
    if n == 0 :
        return 1
    else :
        F = 1
        for i in range(2,n+1) : 
            F = F*i
        return F
print("la factorielle d'un nombre entier :" , factorielle(n))