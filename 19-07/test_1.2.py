"""Importacion y uso de librerias"""
"""Uso especifico de una funcionalidad para una libreria a dependencia"""

from math import sqrt, pow
import math
numero=int(input("Por favor ingrese un numero: "))

valorRaiz = sqrt(numero)

print("La raiz cuadrada de su número ingresado es: {}".format(valorRaiz))

valorPotencia = pow(5, 6)
print("El valor de mi potencia es: {}".format(valorPotencia))

print("Todas funciones que tiene la libreria math es: {}".format(dir(math)))