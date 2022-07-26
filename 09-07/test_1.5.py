"""ProgramaciónOrientada a Objetos"""
"""Encapsulamiento"""

class A():

    def __init__(self):
        """Encapsulamiento"""
        self.inicial = False
        self._contador = 0  #Definiendo atributos como privado

    def incrementar(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador

class B():

    def __init__(self):
        """Encapsulamiento"""
        self.inicial = True
        self.__contador = 10  #Definiendo atributos como privado

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

varA = A()
varA._contador
varA.inicial = True
varA.incrementar()
varA.incrementar()
varA.incrementar()

print("El estado actual del contador: {}".format(varA.cuenta()))
print("El valor de mi estado inicial es: {}".format(varA.inicial))

varB = B()
varB.inicial = False
varB.incrementa()
varB.incrementa()
varB.incrementa()
varB.incrementa()

print("El estado actual del contador: {}".format(varB.cuenta()))
print(varB.inicial)

"""No es posible invocarlo porque el encapsulamiento es fuerte por los dos guiones que le asignamos"""
print("Contador B: {}".format(varB.__contador))
