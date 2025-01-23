def get_positive_integer():
    while True:
        try:
            number = int(input("entrez un nomber positife"))
            if number < 0 :
                raise ValueError("L'entier doit etre positife")
                return number
        except ValueError as e :
            print(f"erreur:{e}.veuillez ressayer")
#exmple
positive_integer = get_positive_integer()
print (f"vous avez saisé : {positive_integer}")