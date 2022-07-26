"""Uso de la libreria datetime"""
"""Usando la funcion strptime"""

from datetime import datetime

print("La fecha actual {}".format(datetime.now()))

date = datetime.strptime("01-07-2022 20:20:00", "%d-%m-%Y %H:%M:%S")

print(date.strftime("%d/%m del año %Y, son las %H horas con %M minutos"))