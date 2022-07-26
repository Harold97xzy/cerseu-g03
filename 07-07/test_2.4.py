"""Problema 05"""

"""
-Solicitar al usuario que ingrese un numero entero
-solicitar al usuario que ingrese un digito
-Mediante una funcion indicar cuantas veces aparece el digito en el numero ingresado
"""

def frecuencia(numero, digito):
    i=0
    while numero!=0:
        ultDigito = numero%10
        if ultDigito==digito:
            i = i+1
        numero = int(numero/10)
    return i

num = int(input("Ingrese un numero: "))
uDigito = int(input("Ingrese el digito a encontrar: "))
print("La frecuencia con la que aparece el digito: {uDigito}, en el numero: {numero} es de {frecuencia} veces"
      .format(uDigito = uDigito, numero = num, frecuencia = frecuencia(num, uDigito)))