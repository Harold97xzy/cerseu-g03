
"""Uso de la libreria de fechas y tiempos"""

from datetime import date, time, datetime

fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()
print("El tiempo actual es: {}".format(tiempo))

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Año actual es: {}".format(anio))
print("Mes actual es: {}".format(mes))
print("Día actual es: {}".format(dia))

"""Uso del datetime para extraer la hora, minuto y el segundo"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("La hora exacta son las: {} horas con {} minutos y {} segundos".format(hora, minuto, segundo))