# /usr/bin/env python3
#L'alphabet
"""Créez un programme qui affiche l'alphabet en lettres minuscules suivi d'un retour à la ligne."""

import string

res = ""
for i in string.ascii_lowercase :
	res += i
print(res)
