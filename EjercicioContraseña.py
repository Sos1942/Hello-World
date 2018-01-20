a = 1
rpg= input("Ingrese su contraseña: ")

if len(rpg)<8:
	a=a+1
else:
	a=1

for i in rpg:
	if  i==" ":
		a=a+1		

if a==1:
	print("Contraseña ok.")
else:
	print("Contraseña errónea.")