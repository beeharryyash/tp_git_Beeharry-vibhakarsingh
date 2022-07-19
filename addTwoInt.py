#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
	return a+b

#tester si le nombre d'argument est correct
nbr_arg=len(sys.argv)-1
if (nbr_arg < 2):
	print("erreur Vous avez oublié de mettre les 2 valeurs du variable a et b")
	x=int(input("Entrer la première valeur: "))
	y=int(input("Entrer la deuxième valeur: "))
elif (nbr_arg > 2):
	print("veuillez mettez uniquement les 2 valeurs des variable a ajouter")
else :
	x=int(sys.argv[1])
	y=int(sys.argv[2])

print(add(x,y))
