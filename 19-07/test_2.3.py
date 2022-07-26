
"""Uso de la libreria de fechas y tiempo"""
"""Conversion total del tiempo"""

from datetime import datetime

"""
    H: hora
    M: minutos
    S: segundos
"""
timeNow = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversion de nuestro valor en tiempo es: {}".format(timeNow))