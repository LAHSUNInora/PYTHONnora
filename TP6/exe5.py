def process_input(user_input):
    try:
        user_input=int(input("Entrez un nombre :"))

        resultat=10/user_input
    except ValueError:
        print("Erreur : ce n'at pas un nombre valide.") 
    except ZeroDivisionError:
        print("division par zero")
    else:    
        print(f"Le rsultat est {resultat}.")
    finally:
        print("Fin du traitement.")  
print(process_input("abc"))          
