#
from FUNCIONESEJ2 import *


seguir = "s"

while seguir == "s":
    print("menu de opciones: \n1- Reponer mercadería (productos existentes) \n2- Vender mercadería (producto existente, solo si alcanza el stock) \n3- Listar inventario \n4- Salir")
    opcion = int(input("seleccione opcion: "))

    match opcion:
        case 1:
            reponer_mercaderia()
        case 2:
            vender_mercaderia()
        case 3:
            mostrar_invertario()
        case 4:
            seguir = "n"