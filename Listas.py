#Existen 2 formas de crear listas
mi_lista = list()
otra_lista = []

print(len(mi_lista)) #Imprime el numero 0 ya que en este momento no hay nada en la lista

#Añade varios valores a la lista
mi_lista = [33, 43, 68, 75, 19, 19, 64]
print(mi_lista) #Esto imprimira lo que hay en la lista
print(len(mi_lista)) #Esto imprimira cuantas cosas hay en la lista

otra_lista = [19, 1.90, "Rafa", "Caro"]

print(type(otra_lista)) #Dice que esto es una lista 

print(otra_lista[0]) #Para poder escoger el dato de la lista que quiero coger tengo que escribirlo empezando desde 0
print(otra_lista[-1]) #Esto cogera el ultimo elemento porque empezara desde el final
print(otra_lista.count(19)) #Esto cuenta cuantas veces aparece el mismo dato en la lista

edad, altura, nombre, apellido = otra_lista #Con esto le das una variable a cada dato que hay en la lista
print(altura)

print(mi_lista + otra_lista) #Esto es para concatenar listas

#Funciones que podemos hacer con las listas
mi_lista.append(333) #Esto añade un dato mas al final de la lista
mi_lista.insert(1, 111) #Esto añade un dato donde yo quiera en la lista 
mi_lista.remove(111) #Esto elimina el valor que quiera pero si hay varias iguales solo elimina la primera
mi_lista.pop() #Elimina el ultimo elemento pero lo guarda
mi_pop = mi_lista.pop #Guarda el elemento que he eliminado en una variable
print(mi_pop)
del mi_lista[1] #Elimina el elemento que le indico
otra_lista.insert(1, "Rojo")
otra_lista[1] = "Verde" #De esta forma puedo cambiar el valor que he añadido en la lista
otra_lista.clear #Elimina todo en mi lista
mi_nueva_lista = mi_lista.copy #Esto copia la lo que hay en la lista
mi_lista.reverse #Le da la vuelta a la lista
mi_lista.sort() #Ordena la lista
mini_lista = mi_lista[1:3] #Esto es para crear sublistas

mi_lista = "Hola" # Si le añado un valor de esta manera la lista pasa a ser un avariable y se borra la lista
print(mi_lista)
print(type(mi_lista))