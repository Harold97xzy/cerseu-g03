"""
3. Escribir un programa para gestionar los errores en Python
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrás la facultad de volver a pedir el
número hasta que se ingrese correctamente.
"""

def datos(nun1, nun2):
    a = int(input("Ingrese primer numero: "))
    b = int(input("Ingrese segundo numero: "))
def divioncero(a, b):
    try:
        divisioncero = a / b
    except ZeroDivisionError:
        print("No es posible una division entre cero")
def sumaincorrecto(a, b):
    try:
        sumaincorrecto = a + b
    except TypeError:
        print("No es posible sumar tipo string")

datos(4, 2)
divioncero()
sumaincorrecto()

