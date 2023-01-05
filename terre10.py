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

res=nombre**0.5

if int(res) == res :
	res = int(res)

print(res)
