#

from FUNCIONESEJ1 import *



seguir = "s"

while seguir == "s":
    print("menu de opciones: \n1-alta de productos(porducto nuevo) \n2-Baja de productos (producto existente) \n3-Modificar productos (cantidad, ubicación) \n4-Listar productos \n5-Lista de productos ordenado por nombre \n6-salir")
    opcion = int(input("seleccione opcion: "))

    match opcion:
        case 1:
            dar_alta_productos()
        case 2:
            dar_baja_productos()
        case 3:
            modificar_productos()
        case 4:
            mostrar_listas()
        case 5:
            mostrar_listas_productos_ordenados()
        case 6:
            seguir = "n"