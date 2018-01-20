valido= False

email=input("Introduce el email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido==True
if valido:
	print("Email correcto.")
else:
	print("Email Incorrecto.")