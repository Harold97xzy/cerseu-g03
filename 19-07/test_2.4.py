"""Uso de la libreria datetime"""

from datetime import datetime

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

d = datetime.strptime("2022/07/19 20:40:00", "%Y/%m/%d %H:%M:%S")
print(dias[d.weekday()]+" dia")