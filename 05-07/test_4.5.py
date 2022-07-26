"""Manejo de cadenas"""

cadena = "Conexion a base de datos con Python"
cadena2 = cadena.replace(cadena[0:6], "cccc")
print("Cadena con reemplazo tiene el siguiente valor: {}".format(cadena2))

"""Eliminanado espacio en blanco antes dde mi cadena"""
cadena3 = "     Conexión a base de datos con Python"
print("Mi valor original de mi variable cadena3 es: {}".format(cadena3))
cadena4 = cadena3.lstrip()
print("Mi cadena con espacios en blanco elimando es: {}".format(cadena4))


cadena5 = "Conexion a base de datos"
cadena6 = cadena5.rstrip()
print("Mi cadena con espacios en blanco elimando es: {}".format(cadena6))
