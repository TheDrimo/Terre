# /usr/bin/env python3
#L'alphabet à partir de
"""Créez un programme qui affiche l'alphabet à partir de la lettre donnée en argument
en lettres minuscules suivi d'un retour à la ligne."""

import string
import sys

alphabet = string.ascii_lowercase
res = ""
if len(sys.argv) != 2 :
	exit()
else :
	lettre = sys.argv[1]
affichage = False
if (len(lettre)!=1) or (lettre not in alphabet) :
	exit()
for i in alphabet :
	if lettre==i :
		affichage=True
	if affichage==True:
		res += i
print(res)
