"""Problema 01"""

"""
-pedir al usuario su email y mostrarlo por pantalla indicando que es su direccion
-validar si es una direccion de correo electronico
-el email se considera si tiene el simbolo del '@'

"""

def validar(email):
    caracterpedido = "@"
    for letra in email:
        if letra == caracterpedido:
            return True
    return False

emailusuario = input("Ingrese su email por favor: ")

if validar(emailusuario):
    print("Email valido")
else:
    print("Email incorrecto")