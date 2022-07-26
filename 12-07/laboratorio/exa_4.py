"""Ejercicio Nª4 de clases en Python"""
"""
1. Crear un programa que pueda realizar depositos y extracciones de dinero

Reglas:
-El banco va a requerir que al finalizar el dia calcule el dinero que se ha depositado
-Crear dos clases, una clase cliente y otra clase banco
-la clase cliente tendras los atributos de nombre y cantidad
-crear los metodos constructor, depositar, extraer, mostrar el total de dinero depositado
-el banco tendra 3 atributos de la clase cliente, el metodo constructor, operar y deposito total
-Instanciar para el caso de 3 personas
-Mostrar los datos de los clientes, incluyendo el monto total de cada uno
"""

class Banco():

    def __init__(self):
        self.cliente1 = Cliente("Susana")
        self.cliente2 = Cliente("Jorge")
        self.cliente3 = Cliente("Elizabeth")

    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(100)
        self.cliente3.depositar(80)
        self.cliente1.extraer(40)

    def depositos(self):
        total = self.cliente1.mostrarCantidad() + self.cliente2.mostrarCantidad() + self.cliente3.mostrarCantidad()
        print("El total de dinero que tiene el banco es: {}".format(total))
        self.cliente1.imprimiDatos()
        self.cliente2.imprimiDatos()
        self.cliente3.imprimiDatos()

class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto > self.cantidad:
            print("No tiene suficiente saldo para que retire")
        elif self.cantidad == 0:
            print("No tienes saldo para retirar")
        else:
            self.cantidad -= monto

    def mostrarCantidad(self):
        return self.cantidad

    def imprimiDatos(self):
        print("{} tiene una canitad depositada de: {}".format(self.nombre, self.cantidad))

banco = Banco()
banco.operar()
banco.depositos()

banco.cliente1.imprimiDatos()