#!/bin/Python
# -*- coding: utf-8 -*-
from numpy import unique

# Obtenir la liste des personnages qui parlent
def getNames(file) :
    fichier = open(file,"r")
    personnages = []
    for line in fichier.readlines() :
        if line[0] == ">" :
            line = line.split()
            nom = " ".join(line[1:])
            if nom not in personnages :
                personnages.append(nom)
    fichier.close()
    
    return personnages

# Obtenir le nombre de fois que chaque perso parle 

def getNombreBlabla(file) :
    BlablaPersonnages = {}

    fichier = open(file,"r")
    for line in fichier.readlines() :
        if line[0] == ">" :
            line = line.split()
            nom = " ".join(line[1:])
            if nom in BlablaPersonnages.keys() :
                BlablaPersonnages[nom] +=1
            elif nom not in BlablaPersonnages.keys():
                BlablaPersonnages[nom] = 1
    fichier.close()

    return BlablaPersonnages

# Identifier le personnage qui parle le plus

def getPersoMaxBlabla(BlablaPersonnages) :
    PersonnageMax = BlablaPersonnages.keys()[0]
    for perso,blabla in BlablaPersonnages.items() :
        if blabla > BlablaPersonnages[PersonnageMax] :
            PersonnageMax = perso
    return PersonnageMax

# Enregistrer les personnages dans un fichier 'blabla.txt'

def savePersoBlabla(BlablaPersonnages) :
    nomFic = raw_input("Dnas quel fichier voulez-vous enregistrer ces informations ? ")
    fichier = open(nomFic,"w")
    i = 1
    for nb in sorted(unique(BlablaPersonnages.values()),reverse=True) : 
        for perso,blabla in BlablaPersonnages.items() :
            if nb == blabla :
                fichier.write(str(i)+" - "+perso+" parle "+str(blabla)+" fois\n")
                i+=1
    fichier.close()
    print "=> Le contenu du dictionnaire a bien été enregistré dans le fichier",nomFic

# NB : sur la ligne 52 :
# unique() est une fonction de la libraire numpy qui permet d'obtenir une liste sans doublons
# sorted() est une fonction de base qui permet de trier les éléments d'une liste dans l'ordre croissant. 
# sorted() a un attribut 'reverse' : si il est égal à 'True' (comme ici), la liste est triée dans l'ordre décroissant


nomFic = raw_input("Quel fichier voulez-vous ouvrir ? ")
print " \nLes personnages parlant :\n", getNames(nomFic)
dico = getNombreBlabla(nomFic)
print "\nLe nombre de fois où chaque personnage parle :\n",dico
print "\nLe personnage parlant le plus est ", getPersoMaxBlabla(dico),"\n"
savePersoBlabla(dico)