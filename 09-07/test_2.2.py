"""Gestion de errores"""
"""Estructura y uso"""

while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
    except:  #Dentro del except se activa una accion si ocurre cierto tipo de error dentro del "try"
        print("No es un valor entero")

        print("Se encontro un dato erróneo en la posicion 80")