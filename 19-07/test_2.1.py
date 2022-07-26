"""Uso de la libreria de fechas y de tiempo"""

from datetime import datetime

strFecha = "02/06/2023"

"""
    d: dia
    m: mes
    y: año
"""
convertion = datetime.strptime(strFecha, "%m/%d/%Y")
print("La fecha formateada es: {}".format(convertion))


"""Traer el mes de la fecha con formato letras: strftime de datetime"""

convertionMes = datetime.strftime(convertion, "%b %d %Y")
print("Nuestra fecha con cambio en el mes es el siguiente: {}".format(convertionMes))

"""b: Reemplaza a 'm'"""