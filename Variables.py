#En Python es buena practica poner las variables con nombres separados por "_"

#Le doy valor a "mi_variable" de "Esto es una variable"
mi_variable_str = "Esto es una variable"
print(mi_variable_str) #Imprime el valor que le he dado a "mi_variable"
mi_variable_int = 3
mi_variable_bool = True

 #Las variables se pueden separar por comas
print(mi_variable_str, mi_variable_int, mi_variable_bool)

 #Esto convierte la variable en un str
variable_int_a_str = str(mi_variable_int)

 #El len() cuenta los caracteres (espacios incluidos) que hay entreparentesis
print(len(mi_variable_str))

#Se puede juntar un texto con una variable separandolo por comas
print("Este es el valor de:", mi_variable_int)

 #Se puede crear varias variables en una misma linea
nombre, apellido, años = "Rafael", "Caro", 33
print("Hola me llamo:", nombre, apellido, "y tengo:", años, "años")

 #Pide por la terminal que introduzcas los datos
hora = input("Que hora es: ")
print("Son las:", hora)