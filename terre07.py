# /usr/bin/env python3
# Inverser une chaîne
"""Créez un programme qui affiche l'inverse de la chaîne de caractères donnée en argument."""

import sys

if len(sys.argv) != 2:
	exit()

chaine = sys.argv[1][::-1]

print(chaine)
