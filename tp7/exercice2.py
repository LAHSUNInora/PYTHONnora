import os
import math
from datetime import datetime

# Répertoire courant
print("Répertoire courant :", os.getcwd())

# Date et heure actuelles
print("Date et heure actuelles :", datetime.now())

# Racine carrée
nombre = float(input("Entrez un nombre : "))
print(f"La racine carrée de {nombre} est {math.sqrt(nombre)}")
