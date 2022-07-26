"""Creacion de una lista"""
"""Una variable que contenta 30 numeros aleatorios"""
"""Mostrar los valores al cuadrado y al cubo de los datos de la lista random"""

import random
listRandom = []

for indice in range(30):
    listRandom.append(random.randint(5, 20))

print(listRandom)

"""Obtener el tamano de mi lista"""
print("El tamaño de mi lista es: {}".format(len(listRandom)))

"""Para elevar al cuadrado y al cubo
valor1 = 3**2
valor2 = 3**3"""

for valor in listRandom:
    print("El valor del cuadrado es: {} y el valor cubo es: {}".format(valor**2, valor**3))

for indice in range(1, 31):
    val = random.randint(5, 20)
    print("Número randon original: {}".format(val))
    print("Cuadrado: {} y el cubo es: {}".format(val**2, val**3))