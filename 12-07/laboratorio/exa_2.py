"""Ejercicio Nª2 de clases en Python"""

"""
2.Crear un programa que tenga la clase Persona.
Regla:
-La clases tendras como atributo el nombre y la edad de una persona
-Implementar los metodos para inicializar los atributos
-Implementar un metodo para mostrar e indicar si la persona es mayor de edad
"""

class Persona():
    """Incicalizar los atributos en el constructor"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print("Su nombre es: {}".format(self.nombre))
        print("Y sue dad es: {}".format(self.edad))

    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

persona1 = Persona("Ivana", 25)
persona2 = Persona("Carlos", 16)

"""Imprimir los resultado si es mayor de edad o no"""

persona1.mostrarDatos()
persona1.mayorEdad()

persona2.mostrarDatos()
persona2.mayorEdad()
