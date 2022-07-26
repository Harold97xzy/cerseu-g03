"""
1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla)
"""
from datetime import date
from datetime import datetime
#Día actual
today = date.today()

#Fecha actual
now = datetime.now()
class Persona():

    def __init__(self, nombre, edad):
        #try:
            self.nombre = nombre
            self.edad = edad
            self.nacionalidad = "Peruana"
        #except TypeError :
            #print("no hay problema con el tipo de dato")
    #- Un método cumpleaños donde cada vez que invoque aumentará en un año la edad de la persona
    def cumple(self):
        self.edad = self.edad + 1
        print("Mi edad aumentada en 1 año más es: {}".format(self.edad))
    #Crear una función que retorne solamente la fecha, hora y minuto que se ha
    # registrado esta persona (Mostrar por pantalla)
    def fecha(self):

        print("Te registraste en la fecha: {}-{}-{} siendo : {} horas con: {} minutos"
              .format(now.day, now.month, now.year, now.hour, now.minute))

persona1 = Persona("Maria", 20)
print("Edad incial : {}".format(persona1.edad))
persona1.cumple()
persona1.cumple()

print("Mi edad actual es: {}".format(persona1.edad))

persona1.fecha()





