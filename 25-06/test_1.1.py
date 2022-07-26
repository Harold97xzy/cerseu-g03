"""Tipos de Datos"""
"""Flotante: float"""

"""Creando nuestra variable"""

var1 = 10.4
var2 = 20.5600 + var1


""".format indica en donde se va a imprimir la variable acompañado con llaves {}"""
print("El valor de mi variable var1 es: {}".format(var1))
print("El valor de mi variable var2 es: {}".format(var2))

"""Imprimiendo con 2 decimales"""
print(f'{var2:.2f}')


print("el valor de mi variable var1 es: {} y el valor de mi variable var2 es: {}".format(var1, var2))