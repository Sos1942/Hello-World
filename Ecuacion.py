def Ecuacion_Cuadratica(a,b,c):
	d= c * a *(-4)
	e=b**2
	f=d+e
	g=f**.5
	h= -b+g
	j=-b-g
	k=2*a
	l=h/k
	m=j/k
	x1=l
	x2=k

	print("X1 es igual a: ",x1, "Y X2 es igual a ",x2)

Ecuacion_Cuadratica(float(input("Escribe el valor de a. . . ")),float(input("Escribe el valor de b. . . ")),float(input("Escribe el valor de c. . . ")))

