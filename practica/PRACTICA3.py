"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos
Reglas:
- Crear una diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Convertir el diccionario a una lista y mostrar en pantalla el tipo de dato.
- Agregar un key adicional con el nombre de “profesion”
- Eliminar el key dni y mostrar el nuevo diccionario."""

diccionario = {"Nombre": "", "Apellido": "", "Edad": "", "DNI": "" }

nom= input("¿Cuàl es tu nombre?: ")
ape= input("¿Cuàl es tu apellido?: ")
edad = input("¿Cuantos años tienes?")
dni = input("¿Cuál es tu dni?")

print("Nombre : {}", "Apellido : {}", "edad : {}", "dni : {}".format(nom, ape, edad, dni))
list(diccionario)

print(type(diccionario))

diccionario["Profesion"] = "Ingeniero de sistemas"

print("El valor de mi nuevo diccionario es: {}".format(diccionario))

del diccionario["DNI"]
print("Mi diccionario actualizado es: {}".format(diccionario))