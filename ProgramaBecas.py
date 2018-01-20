print("Programas para derecho a Beca.")

distancia = int(input("Introduce la distancia a la que vive el alumno con respecto a le escuela: "))
print(distancia)
hermanos= int(input("Introduce la cantidad de hermanos que tiene el alumno: "))
print(hermanos)
salario = int(input("Introduce el salario anual neto de la familia: "))
print(salario)

if distancia>40 and hermanos>=2 or salario<=20000:
	#aqui al inicio dejé un "and " entre hermanos y salario, PERO, si lo cambio por un "Or", da igual si las 2 anteriores  se cumple, o no se cumplen.
	#en este caso darems una pequeña tolerancia a los alumnos que vivan cerca, no tengan hermanos, pero tenga un salario inferior a 20000 bitcoin (xddd) 
	print("Tienes derecho a beca.")

else:
	print("No tienes derecho a beca.")

print("Gracias por usar este programa!")
