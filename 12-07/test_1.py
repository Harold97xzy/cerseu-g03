"""Manejo de Excepciones"""

"""Para controlar el error de division entre cero y el tipo de datos"""

try:
    #val1 = 100/0
    suma = 1000 + "HOLA"
except ZeroDivisionError:
    print("No es posible una division entre cero !!")
except typeError:
    print("No es posible sumar tipo de dato entero y tipo string")