"""ProgramaciónOrientada a Objetos"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("Guauuu")

class Gato():
    def sonido(self):
        print("Miauu")

class Vaca():
    def sonido(self):
        print("Muuu")

vaca = Vaca()
perro = Perro()
gato = Gato()

listaanimales = [vaca, perro, gato]


def cantar(animales):
    for animal in listaanimales:
        animal.sonido()

"""Aplicando polimorfismo: Es el uso de los metodos que tienen las clases con el mismo nombre pero diferentes 
acciones"""

cantar(listaanimales)


