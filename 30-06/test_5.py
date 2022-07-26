"""Asignacion múltiple"""
"""Referente a dos o mas variables"""

nombre = input("Hola, ¿Cuál es tu nombre?")
correo = input("Digite su correo electrònico")
edad = input("¿Cuál es su edad?")

nombreUsuario, correoUsuario, edadUsuario = nombre, correo, edad

print("El nombre de usuario es: {}".format(nombreUsuario))
print("Correo: {}".format(correoUsuario))
print("Su edad es: {} años".format(edadUsuario))