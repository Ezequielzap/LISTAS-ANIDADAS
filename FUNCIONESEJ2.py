#
              #0              #1             #2             #3
estanteria = [[["to12",65],["to16",86],["to20",65],["to25",45]],
               [["to30",68],["to35",73],["to40",85],["to45",89]], 
              [["ta4",58],["ta5",48],["ta6",64],["ta7",96]], 
              [["ta8",36],["ta10",72],["ta12",78],["ta14",71]]]



#1
def reponer_mercaderia()->list:
            for i in range(len(estanteria)):
                for j in range(len(estanteria[i])):
                    print("fila: ", j,"    columna: ", i,"    producto: ", estanteria[i][j])
            columna = int(input("en que columna esta el producto: "))
            fila = int(input("en que fila esta el prodructo: "))

            nueva_cantidad = int(input("cuanta mercaderia queres reponer: "))
            estanteria[columna][fila][1] += nueva_cantidad
            print(estanteria[columna])


#2

def vender_mercaderia()->list:
            for i in range(len(estanteria)):
                for j in range(len(estanteria[i])):
                    print("fila: ", j,"    columna: ", i,"    producto: ", estanteria[i][j])
            columna = int(input("en que columna esta el producto que quiere comprar: "))
            fila = int(input("y en que fila se encuentra el producto que quiere comprar: "))
            cantidad_de_compra = int(input("cuanta cantidad quiere comprar ?: "))

            if cantidad_de_compra > estanteria[columna][fila][1]:
                print("no tenemos suficiente stock")
            else:
                estanteria[columna][fila][1] -= cantidad_de_compra
            print(estanteria[columna])


#3

def mostrar_invertario()->list:
            for i in range(len(estanteria)):
                for j in range(len(estanteria[i])):
                    print("fila: ", j,"    columna: ", i,"    producto: ", estanteria[i][j])


#4
def salir_del_menu():
    seguir = "n"

