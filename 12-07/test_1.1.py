"""Manejo de Excepciones"""

"""Para controlar el error de division entre cero y el tipo de datos"""
"""Multiples excepts en uno solo"""

try:
    valor1 = 500/0
    suma = "Hola" + 5000
except (ZeroDivisionError, TypeError):
    print("Ha ocurrido un error en DivisionZero o TypeError")