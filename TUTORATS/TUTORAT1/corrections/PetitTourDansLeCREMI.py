#!/bin/Python
# -*- coding: utf-8 -*-

def initGrid(size) : # initialise la grille
    grid = []
    for i in range(size) :
        grid.append([])
        for j in range(size) :
            grid[i].append(0)
    return grid

def initPosition(grid,x,y) :
    grid[y][x] = "X"
    return grid

def displayGrid(grid) :
    print ""
    for i in grid :
        for j in i :
            print j,
        print ""
    print ""

def findCoord(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            if grid[i][j] == "X" :
                x = j
                y = i
    return x,y

def move(grid) :
    size = len(grid)
    x,y = findCoord(grid)
    direction = raw_input("Dans quelle direction veux-tu aller ?\n- z pour en haut\n- d pour à droite\n- q pour à gauche\n- s pour en bas\nTon choix : ")
    if direction == "z" and y != 0 :
        grid[y][x] = 0
        y = y-1
        grid[y][x] = "X"
    elif direction == "s" and y != (size-1) :
        grid[y][x] = 0
        y = y+1
        grid[y][x] = "X"
    elif direction == "q" and x != 0 :
        grid[y][x] = 0
        x = x-1
        grid[y][x] = "X" 
    elif direction == "d" and x != (size-1) :
        grid[y][x] = 0
        x = x+1
        grid[y][x] = "X"
    else : 
        if direction in ["z","q","s","d"] :
            print "Attention, tu entres dans un mur !"
        else :
            print "Choisis entre z, q, s et d uniquement."
    displayGrid(grid)
    return grid

# initialiser la grille
size = 10
xPos = 5 # l'axe x correspond à l'axe horizontal, donc à la position de "X" dans la liste interne, donc à sa colonne
yPos = 5 # l'axe y correspond à l'axe vertical, donc à la position de "X" dans la grande liste globale, donc à son rang
grid = initPosition(initGrid(size),xPos,yPos)
displayGrid(grid)

# bouger dans la grille
while True :
    move(grid)
