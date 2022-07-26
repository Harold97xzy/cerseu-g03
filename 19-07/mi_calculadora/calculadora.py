"""Funcion principal"""
"""Llama a las demás funciones de mi módulo externo"""

from funciones import suma, resta, multiplicar, division

x = int(input("Ingrese un valor: "))
y = int(input("Ingrese un segundo valor: "))


print("El resultado de las suma de los dos valores ingresados es: {}".format(suma(x, y)))

print("El resultado de la resta de los dos valores ingresados es: {}".format(resta(x, y)))

print("El resultado de la multiplicacion de los dos valores ingresados es: {}".format(multiplicar(x, y)))

print("El resultado de la division de los dos valores ingresados es: {}".format(division(x, y)))