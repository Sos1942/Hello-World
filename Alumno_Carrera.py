print("Asignaturas Optativas Ano 2017")

print("Asignaturas optativas: Informática gráfica - Usabilidad y accesibilidad - Prueba de software")

print("Escribe la asignatura tal y como està arriba.")

Asignatura=input("Escoge la asignatura escogida: ")

if Asignatura in ("Informática gráfica","Usabilidad y accesibilidad","Prueba de software"):
	
	print("Asignatura elegida: " + Asignatura)
	
	#siendo ambos valores de texto (str), nos deja unirlos o cancatenarlos con un operador de suma.

else:
	print( Asignatura + " no existe.")

print("Gracias por usar este programa!")