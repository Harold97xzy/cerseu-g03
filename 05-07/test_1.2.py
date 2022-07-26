"""Bucle white"""
"""
Reglas:

Ingresar números enteros por teclado hasta que el usuario ingrese 1
-  Realizar la sumatoria de todos los números ingresados

"""

numero = int(input("Ingrese un numero: "))

total = 0
while numero!=1:
    total = total + numero
    print("Mis uma hasta el momento es: {}".format(total))
    numero = int(input("Ingrese un numero: "))

print("La sumatoria de todos los numeros ingresados es: {}".format(total))
