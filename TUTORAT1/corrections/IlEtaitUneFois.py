#!/bin/Python
# -*- coding: utf-8 -*-

# Obtenir la liste des personnages qui parlent

fichier = open("partie5.txt","r")
personnages = []
for line in fichier.readlines() :
    if line[0] == ">" :
        line = line.split()
        nom = " ".join(line[1:])
        if nom not in personnages :
            personnages.append(nom)
fichier.close()

print personnages

# Obtenir le nombre de fois que chaque perso parle 

BlablaPersonnages = {}

fichier = open("partie5.txt","r")
for line in fichier.readlines() :
    if line[0] == ">" :
        line = line.split()
        nom = " ".join(line[1:])
        if nom in BlablaPersonnages.keys() :
            BlablaPersonnages[nom] +=1
        elif nom not in BlablaPersonnages.keys():
            BlablaPersonnages[nom] = 1
fichier.close()

print BlablaPersonnages

# Identifier le personnage qui parle le plus

PersonnageMax = BlablaPersonnages.keys()[0]
print PersonnageMax
for perso,blabla in BlablaPersonnages.items() :
    if blabla > BlablaPersonnages[PersonnageMax] :
        PersonnageMax = perso
print PersonnageMax
