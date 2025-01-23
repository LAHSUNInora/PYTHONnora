#Exercice 03 /
ensemble1 = {'Nora','Imane','Nawal'}
ensemble2 = {'LAHSUNI','BARAKAT','ELHILLALI'}
def inserction(ensemble1,ensemble2):
    ensemble3 = ensemble1.union(ensemble2) 
    return ensemble3
print (" les éléments présents dans les deux ensembles :",inserction(ensemble1,ensemble2))
