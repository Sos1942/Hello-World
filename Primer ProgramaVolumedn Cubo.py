#Inicio practica calculadora de volumenes de figuras

print("Este programa te dara el volumen de un cubo, una esfera y un prisma rectangular");

def Volumen_Cubo(Lado):
	
	volumen = Lado**3

	print("El volumen es :", volumen)

def esfera(Radio):
	volumen = 4/3*3.1416*Radio**3

	print("El volumen es :", volumen)

def rectangulo(largo,altura,ancho):

	volumen = largo*ancho*altura

	print("El volumen es :", volumen)

Volumen_Cubo(float(input("""Escribe el valor de un lado de el cubo. . .
""")))
 
esfera(float(input("""Escribe el valor de el radio de la esfera . . . 
""")))

print("Escribe los siguientes datos de el prisma rectangular. . . ")

rectangulo(float(input("Altura: ")),float(input("Largo: ")),float(input("Anchura: ")))


print("Gracias por usar este programa!")