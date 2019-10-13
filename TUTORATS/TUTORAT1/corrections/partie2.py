#!/bin/Python
# -*- coding: utf-8 -*-

# exercice 1
print "### EXERCICE 1 ###\n"

# question a
print "# Question a #"

n = input("Jusque quel chiffre ? ")  # en python2, input() permet de demander un chiffre à l'utilisateur 
for i in range(n) :
    print i+1 

# question b 
print "\n# Question b #"

n = input("Test pair ou impair : jusque quel chiffre ? ")
for i in range(n):
    if (i+1) % 2 == 0 :
        print i+1,"-> pair"
    else : 
        print i+1, "-> impair"

# NB : au lieu d'ajouter 1 à chaque fois afin de dénombrer de 1 à n au lieu de 0 à n-1, on peut modifier la boucle for ainsi : 
# for i in range(1,n+1)

#######################################################################################

# exercice 2
print "\n### EXERCICE 2 ###\n"

import random  # la bibliothèque random permet d'obtenir des valeurs au hasard dans un intervalle donné

# question a
print "# Question a #"

number = random.randint(1,10)   # random.randint(a,b) permet d'obtenir un chiffre entier tiré au hasard dans l'intervalle [a;b]
user = input("Propose un nombre entier entre 1 et 10 : ")
while number != user :
    user = input("Raté ! Essaye encore : ")
print "Bravo ! Le bon chiffre était bien", number    

# question b
print "\n# Question b #" 

number = random.randint(1,10)
user = input("Propose un nombre entier entre 1 et 10 : ")
while number != user :
    if user > number : # on teste la valeur donnée par l'utilisateur par rapport à celle obtenue au hasard
        user = input("Raté ! Le bon chiffre est plus petit. Essaye encore : ")
    elif user < number :
        user = input("Raté ! Le bon chiffre est plus grand. Essaye encore : ")
print "Bravo ! Le bon chiffre était bien", number
    
#######################################################################################

# exercice 3 - BONUS
print "\n### EXERCICE 3 - BONUS ###\n"

U0 = 0  # on initialise les valeurs
U1 = 1
n = input("Pour quel n voulez vous obtenir le Un ? Attention, n doit être un entier positif : ")   # on récupère quel Un on veut obtenir
if n == 0 :  # on connait déjà Un pour n=0
    print "Un =", U0
elif n == 1 : # on connait déjà Un pour n=1
    print "Un =", U1
elif n > 1 : 
    i=2
    while i != n+1 :
        Un = U0 + U1
        U0 = U1
        U1 = Un
        print i, Un 
        i+=1
    print "Un =", Un