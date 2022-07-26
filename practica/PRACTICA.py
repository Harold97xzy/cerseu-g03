"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente.
Reglas:
- Pedir por consola nombre y edad.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos ingresados.
- Pedir los nombre para dos personales y finalmente mostrar en pantalla la
suma de ambos."""


nom = input("¿Bienvenido, Cuál es tu nombre?: ")
edad = int(input("¿Cúantos años tienes?: "))

nom2 = input("¿Bienvenido, Cuál es tu nombre?: ")
edad2 = int(input("¿Cúantos años tienes?: "))

print("El Tipo de dato nombre es : {}".format(type(nom)))
print("El Tipo de dato edad es : {}".format(type(edad)))
print("El Tipo de dato nombre es : {}".format(type(nom2)))
print("El Tipo de dato edad es : {}".format(type(edad2)))

suma = str(nom + nom2)
suma2 = edad + edad2
print("La suma del primer nombre y segundo nombre es: {} y la suma de las edades es: {} ".format(suma, suma2))


