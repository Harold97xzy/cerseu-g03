
"""Estructura de datos"""

"""Listas: Hacer una copia de la lista original en otra"""

var1 = ["sqlserver", "rDS", "mysql", "postgresql"]

"""Usando: copy()"""

var2 = var1.copy()
var2.append("sqlite3")
var2.remove("rDS")

print("Mi lista originales es: {}".format(var1))
print("La copia de mi lista original es: {}".format(var2))