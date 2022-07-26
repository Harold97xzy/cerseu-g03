""" 2. Usando el concepto y funciones de lista, realizar un programa con las
siguiente características:
Reglas:
- Crear una lista con 10 valores random o alatorios
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas."""

import random
listRandom = []

for indice in range(10):
    listRandom.append(indice)
print(listRandom)

for valor in listRandom:
    print("El valor del cubo es: {}".format(valor**3))













