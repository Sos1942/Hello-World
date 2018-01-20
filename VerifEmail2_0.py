x=0
y=0
for i in input("Correo: "):
	if i== "@":
		x=x+1
	elif i==".":
		y=y+1
	else:
		ver= 123

if x==1 and y>=1:
	print("Correo Ok")
else:
	print("Correo erróneo")

print("Gracias por usar!s")
