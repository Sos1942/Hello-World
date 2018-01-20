print("Introduce 2 numeros y te diré el mayor de ellos: ")

def DevuelveMax(Num1,Num2):
	if Num1 >= Num2:
		print("El número mas alto es :",Num1) 
	else:
		print("El número mas alto es :",Num2)



DevuelveMax(int(input("Primer numero: ")),int(input("Segundo numero: ")))