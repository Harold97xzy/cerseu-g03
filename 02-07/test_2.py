"""Conversion de datos"""

var1 = "2023"
var2 = type(int(var1))

var3 = "Año 2023"
"""Esto no es posible porque el valor contiene una letra"""

var4 = type(int(var3))

print("El tipo de dato de mi var2 es: {}".format(var2))
print("El tipo de dato de mi var2 es: {}".format(var4))