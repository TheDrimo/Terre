# /usr/bin/env python3

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

if (nombre <= 1) :
        print("erreur.")
        exit()

if (nombre != float(argument)) :
        print("erreur.")
        exit()

limite=int(nombre**0.5)+1
prems = True

for i in range(2, limite) :
	if nombre%i == 0 :
		prems = False

if prems :
	print("Oui, {} est un nombre premier.".format(nombre))
else :
	print("Non, {} n'est pas un nombre premier.".format(nombre))

