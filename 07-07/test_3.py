"""Programacion orientada a objetos"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que va a tener por defecto la clase cuando se le instancia la clase"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self. velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad

"""Instanciando nuestra clase"""

carro1 = Carro("Negro", 50)
print("El color de mi carro1 es: {}".format(carro1.color))
print("La aceleracion de mi carro1 es: {}".format(carro1.aceleracion))
print("La cantidad de ruedas de mi primer carro1 es: {}".format(carro1.ruedas))

carro2 = Carro("Blanco", 30)
print("El color de mi carro2 es: {}".format(carro2.color))
print("La aceleracion de mi carro2 es: {}".format(carro2.aceleracion))