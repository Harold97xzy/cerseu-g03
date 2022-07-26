"""E/S Python"""
"""Entradas en Python"""

usuario = input("Ingrese su nombre de ususario:")
nombre = input("¿Cuál es su nombre?")

print("¡Bienvenido {}!".format(nombre))

telefono = input("Ingrese su número de celular: ")
print("{} tienes el siguiente número telefónico: {}".format(nombre, telefono))

edad = int(input("¿Cuál es tu edad?"))
print(type(edad))
print("Usted tiene {} años".format(edad))

"""Usando condiciones"""
if edad >= 18:
    print("Usted es mayor de edad")
elif edad < 18:
    print("Usted es menor de edad")