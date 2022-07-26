import random

def generarNumeros():
    lista = []
    for i in range(15):
        num = random.randint(1, 50)
        lista.append(num)
    return print(lista)

"""Funcion para ordenar la lista"""
def ordenar(lista):
    return lista.sort()

"""Funcion para imprimir el valor de la lista"""
def imprimir(lista):
    print(lista)