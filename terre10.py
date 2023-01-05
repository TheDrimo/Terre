# /usr/bin/env python3
#Racine carrée d'un nombre
"""Créez un programme qui affiche la racine carrée d'un entier positif"""

import sys

if len(sys.argv) != 2 :
        print("erreur.")
        exit()

argument = sys.argv[1]

try :
        nombre = int(argument)
except :
        print("erreur.")
        exit()

if (nombre <= 0) :
        print("erreur.")
        exit()

if (nombre != float(argument)) :
	print("erreur.")
	exit()

i = 0
while (i+1)**2 <= nombre :
        i += 1
while (i+0.1)**2 <= nombre :
        i += 0.1
while (i+0.01)**2 <= nombre :
        i += 0.01

if round(i)**2 == nombre :
        i = int(i)
else :
        i = round(i, 2)

print(i)
