# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:56:23 2014

@author: Fernando
"""
#puntos de nivel
puntos_lvl = 8
vida=0
ataque=0
defensa=0
evasion=0
print "inicia tu epica aventura, tienes 4 habilidades que puedes subir de nivel con un maxicmo de 10 puntos cada una."
print "al inicio del juego se te otorgan 8 puntos que podras repartir entre las siguientes habilidades:"
print "a) Vida"
print "b) Defensa"
print "c) Ataque"
print "d) Evasion"
while puntos_lvl >1 :
    print "Que estadisticas quieres subir?(tienes que gastar todos los puntos)"
    opcion=raw_input()
    if opcion == "a":
        print "cuantos puntos deseas agregar a vida?"
        puntos_add=int(raw_input())
        if puntos_add > puntos_lvl:
            print "valor fuera de rango"
        else:
            vida =vida+puntos_add
            puntos_lvl=puntos_lvl - puntos_add
    if opcion =='b':
        print "cuantos puntos deseas agregar a defensa?"
        puntos_add=int(raw_input())
        if puntos_add > puntos_lvl:
            print "valor fuera de rango"
        else:
            defensa =defensa+ puntos_add
            puntos_lvl=puntos_lvl - puntos_add
    if opcion== 'c':
        print "cuantos puntos deseas agregar a ataque?"
        puntos_add=int(raw_input())
        if puntos_add > puntos_lvl:
            print "valor fuera de rango"
        else:
            ataque =ataque+ puntos_add
            puntos_lvl= puntos_lvl - puntos_add
    if opcion =='d':
        print "cuantos puntos deseas agregar a evasion?"
        puntos_add=int(raw_input())
        if puntos_add > puntos_lvl:
            print "valor fuera de rango"
        else:
            evasion =evasion+ puntos_add
            puntos_lvl= puntos_lvl - puntos_add
        
    print "te quedan", puntos_lvl, "puntos para subir de nivel"
print "Tus estadisticas quedaron de asi"
print "Vida: ", 15+vida, " puntos"
print "Defensa: ", 3+defensa, " puntos"
print "Ataque: ", 3+ataque," puntos"
print "Evasion: ",2+evasion," puntos" 
    
