#Estos simbolos son para hacer operaciones
print(3 + 8) #Esto suna
print(8 / 2) #Esto divide
print(3 * 3) #Esto multiplica
print(2 - 2) #Esto resta
print(10 % 5) #Esto nos da el resto
print(10 // 3) #Esto nos da la solucion pero aproximada a un numero entero
print(2 ** 3) #Esto eleva los numeros
print(2 ** 3 + 3 - 7 / 1 // 4) #Se puede hacer varias operaciones en una misma linea

#Se puede concatenar textos con el "+"
print("Hola " + "mundo")
print("Hola " + 5) #No se puede concatenar diferentes variables
print("Hola " + str(5)) #Pero si se convierte el int en un str ya se podra concatenar

#Si multiplicas el texto por un int se imprimira las veces que tu le pongas
print("Hola" * 3) #Esto imprimira "Hola" 3 veces
print("Hola" * 2.5) #Pero solo numeros int

#Estos simbolos son para comparar
print(3 > 4) #Esto es mayor que
print(3 < 4) #Esto es menor que
print(3 >= 4) #Esro es mayor o igual que
print(4 <= 4) #Esto es menor o igual que
print(3 == 4) #Esto es igual que
print(3 != 4) #Esto es distindo que

#Tambien se puede comparar textos pero esto compara por el orden alfabetico por ASCII
print("Hola" > "mundo")
print("Hola" < "Lara")
print("Hola" >= "Geronimo")
print("Adios" <= "Rafa")
print("Adios" == "Pedro")
print("Adios" != "Don Jose")
print(len("AAAA") == len("ABCD")) #Este cuenta lo caracteres

#Tambien estan los operadore logicos
print(3 < 4 and "Hola" > "mundo") #Esto compara si la primera y segunda se cumplen
print(3 < 4 or "Hola" > "mundo") #Esto compara si la primera o segunda se cumple
print(3 < 4 or "Hola" > "mundo" and 4 == 4) #Se puede hacer varios en una misma linea
print(3 < 4 or ("Hola" > "mundo" and 4 == 4)) #Se puede dar prioridad a una operacion poniendole parentesis
print(not(3 < 4)) #Se niega la condicion