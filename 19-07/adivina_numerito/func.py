
import random

"""Funcion para pedir un numero"""
def cargar():
    return int(input("Ingrese un numero: "))

"""Funcion para obtener un numero aleatorio"""
def cargarAleatorio():
    return random.randint(1, 40)

"""Funcion para adivinar el nuemro"""
def adivinaNumero():
    numero = cargarAleatorio()
    print("Bienvenido al juego de adivina al numerito!!")
    esNumero = False
    while esNumero == False:
        x = cargar()
        if numero == x:
            print("Has ganado!!")
            esNumero = True
        elif numero < x:
            print("El valor ingresado es menor")
        else:
            print("El valor es mayor")