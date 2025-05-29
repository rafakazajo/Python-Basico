#Hay algunos caracteres que si los añades hacen cosas con el texto
mi_str_salto = "Esto es un str \ncon salto de linea" #Si pones "\n" al str el texto salta de linea sin la necesidad de que hagas otro "print"
print(mi_str_salto)
mi_str_tabulado = "\tEsto es un str con tabulado" #Si pones "\t" al str el texto empezara con una tabulacion
print(mi_str_tabulado)
mi_str_escapado = "\\tEsto es un str con tabulado" #Si escribes otra "\" antes del "\t" o "\n" se anula la tabulacion o el salto de linea

#Tambien se puede formatear str
nombre, apellido, edad = "Rafa", "Caro", 19
print("Mi nombre es: {} {} y mi edad es: {}".format(nombre, apellido, edad)) #Se puede formater poniendo "{}" en donde quieras poner los datos y despues el "".format()"
print("Mi nombre es: %s %s y mi edad es: %d" %(nombre, apellido, edad)) #O poner "%s" para los str, "%d" para los enteros y despues el "%()"
print(f"Mi nombre es: {nombre} {apellido} y mi edad es: {edad}") #Esta forma tambien sirve para formatear

#Se puede desenpaquetar caracteres
saludo = "Buenos dias"
a, b, c, d, e, f, g, h, i, j, k = saludo #Esto lo que hace que le valor a cada variable de las letras que tiene como: (a = H, b = o, c = l, d = a)
print(a) #Se imprime la letra que corresponde a cada variable
print(b)
print(c)
print(d)
print(e)
print(f)

#Se puede dividir
dividido = saludo [7:11] #Coge los caracteres que se encuentran entre los numeros que estan dentro de [] sin contar el ulimo numero que hemos puesto y contando desde 0
print(dividido)
dividido = saludo [1:] #Coge todos los caracteres a partir del numero que escribimos 
print(dividido)
dividido = saludo [-2] #Coge los caracteres desde el numero que escribimos contando desde atras
print(dividido)

#Tambien le puedes dar la vuelta
al_reves = saludo [ :: -1] #le da la vuelta al texto
print(al_reves)

#
print(saludo.capitalize()) #Te pone la primera letra en mayuscula
print(saludo.upper()) #Pone todas la letra en mayuscula
print(saludo.count("s")) #Cuenta cuantas lo que le pongas entre "()"
print("33".isnumeric()) #Te dice si es numerico
print(saludo.lower()) #Pone todas las letras en minuscula
print(saludo.upper().isupper()) #Puedes poner varias como la de poner todas en mayuscula y preguntar si son mayusculas
print(saludo.startswith("Buenos")) #Pregunta si empieza con los que pongas entre "()"