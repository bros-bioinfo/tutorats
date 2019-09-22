#!/bin/Python
# -*- coding: utf-8 -*-

# exercice 1
print "### EXERCICE 1 ###\n"

master = ["Coralie","Etienne","Elsa","Domitille","Amelie"]
master.append("Tata")  # la méthode liste.append permet d'ajouter un élément en fin de liste
master.remove("Tata")  # la méthode liste.remove() permet d'enlever l'élément dont la valeur est donnée en argument (ici "Tata")
print "Contenu de la liste :", master
print "Longuer de la liste :", len(master)  # la fonction len(liste) donne la longueur/le nombre d'élements contenus dans la liste passée en argument

###################################################""

# exercice 2
print "\n### EXERCICE 2 ###\n"

master_complet = {   # initialisation du dictionnaire avec 7 personnes du master
    "Coralie": "M2", 
    "Elsa": "M2", 
    "Etienne": "M2", 
    "Tata": "prof", 
    "Tatie": "prof",
    "Mick": "M1",
    "Mathieu": "M1"}

master_complet["Tonton"] = "prof"  # ajout de 2 personnes dans le dictionnaire
master_complet["Louis"] = "M1"

print "Statut de Tatie :", master_complet["Tatie"]   # affiche le statut de Tatie (attention aux majuscules !!)

del master_complet["Tatie"]  # supprime l'élément ayant pour clé "tatie"

print "Contenu de master_complet :", master_complet   # affiche le contenu du master
print "Noms contenus dans la structure :", master_complet.keys()   # affiche uniquement le nom des membres -> la méthode dico.keys() donne une liste des clés du dictionnaire
print "Statuts contenus dans la structure :", master_complet.values()  # affiche uniquemnet les statuts -> la méthode dico.values() donne une liste des valeurs du dictionnaire