"""Problema 03"""

"""
-Pedir numeros al usuario hasta que ingrese 0 para finalizar
-Mostrar la suma de sus digitos y la suma de todos los numeros que hemos ingresado
-reutilizar la funcion que se creo es el ejemplo anterior
"""

def sumaDigito(numero):
    suma =0
    while numero!=0 :
        digito = numero%10
        suma = suma+digito
        numero = int(numero/10)
    return suma

sumatoria=0
num = int(input("Ingrese un numero a procesar: "))

while num!=0:
    print("La suma de los digitos es: {}".format(sumaDigito(num)))
    sumatoria= sumatoria+num
    num = int(input("Ingrese un numero a procesar: "))

print("La suma de todos los numeros que has ingresado es: {}".format(sumatoria))
print("La suma de todos los digitos es: {}".format(sumaDigito(sumatoria)))
