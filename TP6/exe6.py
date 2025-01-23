def safe_division(a, b):
    try:
       resultat= a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro.")
    else:
        
        print("la operation et effuctee")
        return resultat
    finally:
        print("Fin du traitement.")        

   
print(safe_division(10, 2))  
print(safe_division(10, 0))