# Primero tenemos que importar
# la funcion print (que viene del modulo)
# __future__ para poder utilizar a print
# como una funcion

from __future__ import print_function

def mi_funcion():
    print("Hola mundo")


def nombres(nombre, apellido):
    nombre_completo = "Mi nombre es %s %s" % (nombre, apellido)
    print(nombre_completo)

nombres("Eduardo ", "Echeverria ")
