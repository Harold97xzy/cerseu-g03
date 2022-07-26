"""Uso de la libreria datetime"""
"""Operacion resta"""

from datetime import  datetime

datetime1 = datetime.strptime("01-07-2022 20:20:00", "%d-%m-%Y %H:%M:%S")
datetime2 = datetime.strptime("15-07-2022 20:20:00", "%d-%m-%Y %H:%M:%S")

tiempo = datetime1-datetime2
print("El tiempo final es: {}".format(tiempo))