"""Manejo de Excepciones"""

"""Analisis del try except"""

try:
    valor1 = 100/0
except:
    print("Entro al except, ha ocurrido una excepcion!!! ")
else:
    print("Entro al else, no ha ocurrido un error")