#Existen 2 formas de definir una tupla y las tuplas son listas ceradas que no se pueden modificar
mi_tupla = tuple()
otra_tupla = ()

mi_tupla = (19, 1.90, "Rafa", "Caro")
otra_tupla = ("España", "Verde")
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[1])

print(mi_tupla.index("Rafa")) #Esto lo que nos dice es en donde esta lo que le hemos puesto entre parentesis

#Las tuplas no se pueden modificar
#mi_tupla[2] = "Javier" #Esto nos da un error porque no podemos cambiar una tupla
suma_de_tuplas = mi_tupla + otra_tupla
print(suma_de_tuplas) #Esta es la unica forma de modificar +- la tupla

#Esta es una forma de modificar la tupla
mi_tupla = list(mi_tupla) #Convirtiendo la tupla en una lista
print(type(mi_tupla))
mi_tupla[1] = 1.92
mi_tupla.insert(0, "Rafakazajo")
print(mi_tupla)
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))