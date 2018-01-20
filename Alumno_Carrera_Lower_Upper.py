#esta practica es una modificacion de alumno_carrera, la cual va a ser tolerante y va a convertir en minùsculas la infromaciòn ingresada, para que
#python lo pueda comparar sin importar en la maner que el usuario escribiò la informaciòn ingresada

print("Asignaturas Optativas Ano 2017")

print("Asignaturas optativas: Informática gráfica - Usabilidad y accesibilidad - Prueba de software")

opcion=input("Escoge la asignatura escogida: ")
#ahora en lugar de cambiar automaticamente Asignatura en el valor que hay que ingresar, use otra variabe, a la cual se le va a aplicar una funcio qu lo vuelva en 
#minusculas
Asignatura=opcion.lower()

if Asignatura in ("informática gráfica","usabilidad y accesibilidad","prueba de software"):
	
	print("Asignatura elegida: " + Asignatura)
	
	#siendo ambos valores de texto (str), nos deja unirlos o cancatenarlos con un operador de suma.

else:
	print( Asignatura + " no existe.")

print("Gracias por usar este programa!")

