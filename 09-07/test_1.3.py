"""Herencia entre clases"""

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

"""Aplicando herencia"""
"""Creando nuestra clase hija"""

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro1 = Carro("rojo", 30)
"""Instanciando"""
carVolador = CarroVolador("Blanco", 40)

print("El color de mi carro volador es: {}".format(carVolador.color))
print("La aceleración de mi carro volador es: {}".format(carVolador.aceleracion))
print("La velocidad inicial de mi carro volador es: {}".format(carVolador.aceleracion))

"""Aqui aplicamos el efecto de herencia al usar el metodo de la clase padre 'Carro'"""

carVolador.acelera()
carVolador.acelera()

print("La velocidad actual de mi carro volador es: {}".format(carVolador.velocidad))

""""""
print("El estado de vuelo de mi carro 1 es: {}".format(carro1.))