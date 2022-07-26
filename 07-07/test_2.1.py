"""Problema 02"""

"""
-Pedir numeros al usuario hasta que ingrese 0.
-Mostrar la suma de sus digitos
-Crear una funcion que realice dicha suma
"""

def sumaDigito(numero):
    suma =0
    while numero!=0 :
        digito = numero%10
        suma = suma+digito
        numero = int(numero/10)
    return suma

num = int(input("Ingrese numero a procesar: "))
while num!=0:
    print("Suma {}".format(sumaDigito(num)))
    num = int(input("Ingrese numero a procesar: "))