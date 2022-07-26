

"""Decoradores en Python"""


import time


def mesureTime(func):

    def calculator(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        total = time.time() - start

        print("Tiempo de ejecución es: {}".format(total))

        return result

    return calculator


@mesureTime
def suma(a, b):
    time.sleep(1)
    resultado = a + b
    return resultado


@mesureTime
def resta(x, y):
    time.sleep(1)
    return x - y


print(suma(90, 500))
print(resta(90, 500))
