#Exercice 02  :
tuple = (85,6,332,12,-5,123.2) 
max = tuple[0]
longeur = len(tuple)
def max_tuple(tuple):
     global max
     for i in range(longeur):
          if tuple[i] >= max:
               max = tuple[i]
     return max
print("le nombre plus grand dans le tuple est  ", max_tuple(tuple))
#ona Autre Méthode on utilise la function sum 
