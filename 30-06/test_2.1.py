"""Listas"""

"""Eliminando un elemento de la lista por indice: del"""

lista = []
lista.append("2022")
lista.append("Junio")
lista.append("Python Modulo I")
lista.append(30)

print(lista)

"""Eliminando un elemento de la lista original"""

del lista[3]
print("Mi lista actualizada es: {}".format(lista))

"""No es posible eliminar un elemento que no tiene indice en la lista"""
#del lista[8]
#print(lista)
