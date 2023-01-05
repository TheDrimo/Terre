# /usr/bin/env python3
#Pair ou impair
"""Créez un programme qui permet de déterminer si l'argument donné est
un entier pari ou impair."""

import sys

if len(sys.argv) != 2 :
	print("Tu ne me la mettras pas à l'envers")
	exit()

argument = sys.argv[1]

try :
	if int(argument) != float(argument):
                        print("Tu ne me la mettras pas à l'envers")
                        exit()
except :
	print("Tu ne me la mettras pas à l'envers")
	exit()

nombre=int(argument)**2

if nombre%2==1 :
	print("impair")
else :
	print("pair")

