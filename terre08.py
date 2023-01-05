# /usr/bin/env python3
#Taille d'une chaîne
"""Créez un programme qui affiche le nombre de caractères d'une chaîne de caractères
passée en argument."""

import sys

if len(sys.argv) != 2 :
	print("erreur.")
	exit()

chaine = sys.argv[1]

if chaine.isnumeric():
	print("erreur.")
	exit()
else :
	print(len(chaine))
