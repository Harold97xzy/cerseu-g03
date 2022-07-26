
"""Uso de la libreria de fechas y tiempo"""
"""Comparacion de fechas"""

import datetime

fecha1 = datetime.datetime(2023, 4, 19) #Tipo de datos datetime
fecha2 = datetime.datetime(2023, 4, 15) #Tipo de datos datetime

if fecha1 == fecha2:
    print("Nacieron el mismo dia")
elif fecha1 < fecha2:
    print("EL niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")