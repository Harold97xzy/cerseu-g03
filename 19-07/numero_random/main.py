
"""
2. Hacer un programa que pueda generar 15 numeros aleatorios entre 1 y 50

REGLAS:
-Mostrar la lista con los números random que se han obtenido
-Ordenar los valores de la lista e imprimirlos en pantalla
-Modularizar o dividir nuestro programa en funciones.
"""
from func import *

milista = generarNumeros()
imprimir(milista)
ordenar(milista)
imprimir(milista)