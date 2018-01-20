primeraTupla = ("Esto es un Texto",1,1.2,3,4,5,6,7,8,9)
#aqui creo mi primera tupla
segundalista = ["Segunda lista", 2, 3,4]
#creo segunda lista
print(primeraTupla[7])
#imprimo el valor 7 de la primera tupla

la_Lista_de_prueba = list(primeraTupla)
#creo una lista a partir de la primera tupla
la_Lista_de_prueba.append("Esto va al final de la lista")
#agrego cosas a la primera lista... 		
la_Lista_de_prueba.extend(["Esto va al final de el final de la lista", "esto depues de lo anterior"])
#mas cosas...
la_Lista_de_prueba.insert(1, "esto va depues de 1 y antes de 1.2")
#mas cositas...
print(la_Lista_de_prueba.index("Esto es un Texto"))
#pregunto por el numero de indice de "esto es un texto"

print(la_Lista_de_prueba[:])
# imprimo la lista hecha a partir de la tupla


print("Esto es un Texto" in la_Lista_de_prueba)
#pregunto por true o false

print("esto es una mentira" in la_Lista_de_prueba)
#pregunto por true o flase
print(segundalista[:])
#imprimo segunda lista
segundaTupla = tuple(segundalista)
#creo segunda tupla a prtir de la segunda lista
print(segundaTupla)
#imprimo segunda Tupla

#fin