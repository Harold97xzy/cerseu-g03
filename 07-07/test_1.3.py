"""Programacion funciones"""

var1 = int(input("Ingrese un primer valor: "))
var2 = int(input("Ingrese un segundo valor valor: "))

def resta(x, y, z=20):
    resultado = x-y-z
    return resultado

""""""
print("El resutlado de mi funcion es: {}".format(resta(var1, var2, 40)))