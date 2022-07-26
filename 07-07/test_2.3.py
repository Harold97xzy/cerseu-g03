"""Problema 04"""

"""
-Solicitar al usuario que ingrese un numero entero
-Indicar si este numero es primo o no
-utilizar una funcion para el desaroolo de este problema
"""

def primo(numero):
    for valor in range(2, numero):
        if numero%valor==0:
            return False
    return True

num = int(input("Ingrese un numero a evaluar: "))
if primo(num):
    print("El numero ingresado es primo!!")
else:
    print("El numero no es primo!!")
