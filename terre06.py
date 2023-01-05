# /usr/bin/env python3
# Divisions
"""Créez un programme qui affiche le résultat et le reste d'une division entre deux nombres."""

import sys

if len(sys.argv) != 3 :
        print("erreur.")
        exit()

argument1, argument2 = sys.argv[1], sys.argv[2]

try :
        for i in [argument1, argument2]:
                if int(i) != float(i):
                        print("erreur.")
                        exit()
except :
        print("erreur.")
        exit()

nombre1, nombre2 =int(argument1), int(argument2)

if (nombre1 < nombre2) or (nombre2 <= 0) :
	print("erreur.")
	exit()

resultat = nombre1//nombre2
reste = nombre1%nombre2

print("résultat: ", resultat)
print("reste: ", reste)
