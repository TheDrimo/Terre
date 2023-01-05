# /usr/bin/env python3
#Afficheur d'arguments
"""Créez un programme qui affiche les arguments qu'il reçoit ligne par ligne, peu importe
le nombre d'arguments."""

import sys

arguments = sys.argv
if len(arguments)>1 :
	for a in arguments[1:] :
		print(a)
