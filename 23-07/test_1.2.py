
"""Decoradores en Python"""
"""Creación de una función decoradora"""


def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Antes de ejecutar la funcion a decorar")
        resultado = funcionB(*args, **kwargs)
        print("Despues de ejecutar la funcion a decorar")
        return resultado
    return funcionC


@funcionA
def saludar(name, lastname, age):

    return print("Hola {} {}, usted tiene {} años".format(name, lastname, age))


nombre = input("Ingrese su nombre por favor: ")
ape = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad finalmente: ")
saludar(nombre, ape, edad)
