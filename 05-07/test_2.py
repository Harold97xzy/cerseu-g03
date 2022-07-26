
"""Uso del for"""

ingienerias = ["software", "sistemas", "industrial", "electronica", "quimica"]
i = 0

print("El tamaño de nuestra lista es: {}".format(len(ingienerias)))

for ingieneria in ingienerias:

    print("Ingieneria {}".format(ingieneria))
    i = i + 1
    print("Esta es la vuelta numero: {}".format(i))

print("llego al final de nuestro for")