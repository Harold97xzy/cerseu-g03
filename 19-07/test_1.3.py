"""Importacion y uso de librerias"""
"""Poniendole un nombre a una funcionalidad especifica"""

from math import sqrt as raiz, pow as pot

numero=int(input("Por favor ingrese un numero: "))

valorRaiz = raiz(numero)

print("La raiz cuadrada de su número ingresado es: {}".format(valorRaiz))

valorPotencia = pot(5, 6)
print("El valor de mi potencia es: {}".format(valorPotencia))
