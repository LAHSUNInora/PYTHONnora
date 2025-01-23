def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return"Erreur : Ce n'est pas un entier valide"

      

print(convert_to_int("abc"))
print(convert_to_int("123"))
