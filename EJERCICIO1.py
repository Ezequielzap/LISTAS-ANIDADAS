#

gondola = [   
            [[],["botellas",3],[],["frascos",8],[]],
            [[],[],["fideos",4],[],[]],
            [[],[],[],["leche",6],[]]
            ]
seguir = "s"
while seguir == "s":

    print("menu de opciones: \n1-alta de productos(porducto nuevo) \n2-Baja de productos (producto existente) \n3-Modificar productos (cantidad, ubicación) \n4-Listar productos \n5-Lista de productos ordenado por nombre \n6-salir")
    opcion = int(input("seleccione opcion: "))
    
    
    
    match opcion:
        case 1:
            producto_nuevo = input("ingrese nuevo producto: ")
            cantidad = int(input("ingrese la cantidad del producto: "))
            columna = int(input("a que columna lo quiere agregar(0-4): "))
            fila = int(input("a que fila lo quiere agregar(0-2): "))
            if gondola[fila][columna] == []:
                gondola[fila][columna] = [producto_nuevo,cantidad]
                print(gondola[fila])   
            else:
                print("!EL ESPACIO SELECCIONADO NO ESTA VASIO!")
        case 2:
            for i in range(len(gondola)):
                for j in range(len(gondola[i])):
                    print("fila: ", i,"    columna: ", j,"    producto: ", gondola[i][j])
            columna = int(input("en que columa esta el producto (0-4): "))
            fila = int(input("en que fila esta ese producto (0-2): "))
            
            gondola[fila][columna] = []
            print("GONDOLA ACTUALIZADA")
            for i in range(len(gondola)):
                for j in range(len(gondola[i])):
                    print("fila: ", i,"    columna: ", j,"    producto: ", gondola[i][j])
        case 3:
            for i in range(len(gondola)):
                for j in range(len(gondola[i])):
                    print("fila: ", i,"    columna: ", j,"    producto: ", gondola[i][j])
            modificar = input("que modificacion quieres hacer (cantidad/ubicacion/ambas): ")
            if modificar == "cantidad":
                columna = int(input("en que columa esta el producto (0-4): "))
                fila = int(input("en que fila esta ese producto (0-2): "))
                nueva_cantidad = int(input("ingrese nueva cantidad: "))
                gondola[fila][columna][1] = nueva_cantidad
                print(gondola[fila])
            elif modificar == "ubicacion":
                fila = int(input("en que fila se encuentra el producto: "))
                columna = int(input("en que columna se encuentra el producto: "))
                producto = gondola[fila][columna]
                print("INICIANDO CAMBIO DE UBICACION")        
                nueva_columna = int(input("caul sera su nueva columna: "))
                nueva_fila = int(input("cual sera su nueva fila: "))                  
                if gondola[nueva_fila][nueva_columna] == []:
                    gondola[nueva_fila][nueva_columna] = producto
                    gondola[fila][columna] = []
                    print(gondola[nueva_fila])
                else:
                    print("EL LUGAR SELECCIONADO NO ESTA VACIO")
            else:
                columna = int(input("en que columa esta el producto (0-4): "))
                fila = int(input("en que fila esta ese producto (0-2): "))
                nueva_cantidad = int(input("ingrese nueva cantidad: "))
                producto = gondola[fila][columna]

                nueva_columna = int(input("caul sera su nueva columna: "))
                nueva_fila = int(input("cual sera su nueva fila: ")) 
                if gondola[nueva_fila][nueva_columna] == []:
                    gondola[nueva_fila][nueva_columna] = [producto[0],nueva_cantidad]
                    gondola[fila][columna] = []
                    print(gondola[nueva_fila])
                else:
                    print("EL LUGAR SELECCIONADO ESTA OCUPADO")
        case 4:
            for i in range(len(gondola)):
                for j in range(len(gondola[i])):
                    print("fila: ", i,"    columna: ", j,"    producto: ", gondola[i][j])
        case 5:
            listas_productos_ordenados = []
            for i in range(len(gondola)):
                for j in range(len(gondola[i])):
                    if gondola[i][j]:
                        listas_productos_ordenados.append(gondola[i][j])

            for i in range(len(listas_productos_ordenados)- 1):
                for j in range(i + 1,len(listas_productos_ordenados)):
                    if listas_productos_ordenados[i][0] > listas_productos_ordenados[j][0]:

                        aux = listas_productos_ordenados[i]
                        listas_productos_ordenados[i] = listas_productos_ordenados[j]
                        listas_productos_ordenados[j] = aux
            for e_lista in listas_productos_ordenados:
                print(e_lista[0], e_lista[1])
        case 6:
            seguir = "n"

