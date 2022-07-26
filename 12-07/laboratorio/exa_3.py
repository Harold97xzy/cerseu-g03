"""Ejercicio Nª3 de clases en Python"""
"""
1. Crear un programa que cargue los datos de un triangulo

Reglas:
-Crear una clase triangulo y metodo para inicializar sus atributos
-Crear un metodo para imprimir el valor de un lado con un tamaño mayor
-Crear un metodo para saber que tipo de triangulo es(Equilatero, isósceles o escaleno)
"""

class Triangulo():

    def __init__(self):
        self.lado1 = input("Ingrese el valor del primer lado")
        self.lado2 = input("Ingrese el valor del segundo lado")
        self.lado3 = input("Ingrese el valor del tercer lado")

    def mostrarDatos(self):
        print("Los lados del triangulo tienen los siguientes valores")
        print("Lado 1: {}".format(self.lado1))
        print("Lado 2: {}".format(self.lado2))
        print("Lado 3: {}".format(self.lado3))

    def comparar(self):
        print("El mayor lado es: ")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("Lado 1 con valor: {}".format(self.lado1))
        elif self.lado2 > self.lado3 and self.lado2 > self.lado1:
            print("Lado 2 con valor: {}".format(self.lado2))
        elif self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("Lado 3 con valor: {}".format(self.lado3))
        elif self.lado3 == self.lado2 and self.lado2 != self.lado1:
            print("Hay dos lados iguales")
        else:
            print("Los tres lados son iguales")

    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isósceles")

figura = Triangulo()
figura.mostrarDatos()
figura.comparar()
figura.tipo()