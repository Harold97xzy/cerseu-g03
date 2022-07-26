"""
1. Realizar un programa que contenga una clase llamada Alumno

Reglas:
-Debe tener los atributos de nombre y la nota para el alumno
-Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota.
-Mostrar en el mensaje si el alumno aprobó o no
-Instanciar por lo menos 2 alumnos


"""
class Alumno():
    """Inicializar los atributos"""

    def __ini__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    """Metodo para imprimir los datos"""
    def imprimir(self):
        print("Nombre del alumno: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))

    """Metodo para obtener el resultado"""
    def resultado(self):
        if self.nota < 11:
            print("El alumno ha desaprobado el curso")
        else:
            print("El alumno aprobo")

"""Creando las nuevas instancias"""
alumno1 = Alumno("Lucia", 9)
alumno2 = Alumno("Javier", 17)

""""""
alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()