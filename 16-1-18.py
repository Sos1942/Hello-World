amistad=1
print("Hola! Soy una maquina que habla contigo. . . Asi de antisocial es mi creador. . . ")
print(". . . ")
Nombre = input("Cual es tu nombre? ")
print("Mucho gusto " + Nombre + "!")
print(". . . ")
Amistad = input("Quieres ser mi amig@? ")
if Amistad== "si" or Amistad== "Si" or Amistad== "se":
	print("Que bien!")
	amistad=amistad+1
else:
	print("Vale. . . ")
	amistad=amistad-1
print(amistad)