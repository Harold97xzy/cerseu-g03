"""Programacion funciones"""

var1 = int(input("Ingrese la base: "))
var2 = int(input("Ingrese la potencia: "))

def potencia(a, b):
    resultado = a**b
    return resultado

print("Mi valor al usar mi funcion potencia es: {}".format(potencia(var1, var2)))