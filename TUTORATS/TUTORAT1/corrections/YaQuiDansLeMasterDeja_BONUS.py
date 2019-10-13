#!/bin/Python
# -*- coding: utf-8 -*-

def initMaster() :
    master = {}
    print "=> Dictionnaire créé"
    return master

def addMember(master) :
    name = raw_input("Nom du nouveau membre : ")
    statut = raw_input("Statut du nouveau membre : ")
    master[name] = statut
    return master

def delMember(master) :
    name = raw_input("Nom du membre à supprimer : ")
    if gestionErreur(master,name,"n") :
        del master[name] 
    return master

def displayMaster(master) :
    for key,value in master.items() : 
        print ">", key, "("+value+")"

def getStatut(master) :
    name = raw_input("Nom du membre : ")
    if gestionErreur(master,name,"n"):
        print "Statut de",name,":",master[name]

def getNames(master) :
    statut = raw_input("Statut des membres à trouver : ")
    if gestionErreur(master,statut,"s") :
        names = [] # on ne sait pas combien de personnes ont ce statut, il faut donc initialiser une liste à laquelle on ajoutera des éléments (les noms) si le statut correspondant est bien celui qu'on cherche
        for key,value in master.items() :
            if value == statut :
                names.append(key)
        print "Noms de ceux étant", statut, ":", names

def menu():
    answer = input("--------------\nChoisis une option :\n1 - Créer le dictionnaire 'master'\n2 - Ajouter un membre\n3 - Supprimer le membre de ton choix\n4 - Afficher le contenu du dictionnaire 'master'\n5 - Afficher le statut d'un membre\n6 - Obtenir le nom de tous les membres ayant un statut particulier\n0 - Quitter le menu\nTon choix : ")
    return answer

def gestionErreur(dico, element, option) :  # l'option vaut soit n (pour name), soit s (pour statut) => ceci indique à la fonction de vérifier pour n que l'element est bien présent dans les clés, et pour s dans les valeurs
    if element not in dico.keys() and option == "n" :
        print "Désolé, le nom que vous avez donné n'est pas présent dans le dictionnaire 'master'"
        return False
    elif element not in dico.values() and option == "s" :
        print "Désolé, le statut que vous avez donné n'est pas présent dans le dictionnaire 'master'"
        return False
    else :
        return True

while True :
    answer = menu()
    if answer == 1 :
        master = initMaster()
    elif answer == 2 : 
        master = addMember(master)
    elif answer == 3 : 
        master = delMember(master)
    elif answer == 4 : 
        displayMaster(master)
    elif answer == 5 :
        getStatut(master)
    elif answer == 6 : 
        getNames(master)
    elif answer == 0 : 
        print "----- Au revoir -----"
        break
    else : 
        print "Désolé, ceci n'est pas une option possible. Merci de choisir entre 0, 1, 2, 3, 4, 5 et 6 uniquement."
    print ""
