"""Programacion funciones"""

var1 = int(input("Ingrese un primer valor: "))
var2 = int(input("Ingrese un segundo valor valor: "))

"""El nombre de la funcion en general es lo que va a realizar la funcion"""
"""input: Son los parametros"""
def multiplicar(a, b):
    resultado = a*b
    return resultado #Es el output: El valor que retorna la funcion

print("El resultado de mi funcion es: {}".format(multiplicar(var1, var2)))