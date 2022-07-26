"""Estructura de datos"""
"""Listas: Cantidad de veces que se repite un elemento de una lista"""

varlista = ["Python", "PHP", "Ruby"]

varlista.append("Python")
varlista.append("Python")
varlista.append("Ruby")

print("Mi nueva lista es: {}".format(varlista))
print("La cantidad de veces que repite python es: {}".format(varlista.count("Python")))
print("La cantidad de veces que repite ruby es: {}".format(varlista.count("Ruby")))
print("La cantidad de veces que repite 1000 es: {}".format(varlista.count(1000)))