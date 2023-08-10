print("----------------------------------------------------------------")
print("| practica 1 - Lenguajes formales y de programación seccion B+ |")
print("----------------------------------------------------------------")

def cargarInvIn():
    print("-----------Cargar Inventario Inicial-----------")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("ingrese la cantidad: "))
    precio = float(input("ingrese el precio: "))
    ubicacion = input("ingrese la ubicacion: ")
    crear_producto = [nombre, cantidad, precio, ubicacion]
    archivo = open('inventario.inv', 'a+')
    archivo.write("\n crear_producto " + crear_producto[0] + "; " + str(crear_producto[1]) + "; " + str(crear_producto[2]) + "; " + crear_producto[3] + " ")
    archivo.seek(0)
    var_inv = archivo.read()
    print("")
    print(var_inv)
    print("")
    archivo.close()
    input("Presione una tecla para continuar...")

def cargarInsMov():
    print("-----------Cargar Instrucciones de Movimientos-----------")
    print("Que desea hacer?")
    print("1. Agregar stock")
    print("2. Vender producto")
    op = int(input("Ingrese una opción: "))
    match op:
        case 1:
            nombre = input("Ingrese el nombre del producto que desea agregar: ")
            cantidad = input("Ingrese la cantidad que desea agregar: ")
            ubicacion = input("Ingrese la ubicacion donde desea agregar: ")
            archivo = open("inventario.inv", "a+")
            archivo.seek(1)
            lineas = archivo.readlines()
            archivo.close
            
        case 2:
            cargarInsMov()
        case _:
            print("Opción no válida")
            cargarInsMov()

    archivo = open('movimientos.mov', 'r+')
    var_informe = archivo.read()
    print(var_informe)
    archivo.close()
    input("Presione una tecla para continuar...")

def crearInfoInv():
    print("-----------Crear Informe de inventario-----------")
    archivo = open('informe.txt', 'w+')
    archivo.write("\n------------ INFORME DE INVENTARIO ------------\n")
    var_informe = archivo.read()
    print(var_informe)
    archivo.close()
    input("Presione una tecla para continuar...")

def salir():
    print("Saliendo del programa...")

def menu():
    print("--------------------MENU--------------------")
    print("| 1. Cargar Inventario Inicial             |")
    print("| 2. Cargar Instrucciones de Movimientos   |")
    print("| 3. Crear Informe de inventario           |")
    print("| 4. Salir                                 |")
    print("--------------------------------------------")
    opc = int(input("Ingrese una opción: "))
    match opc:
        case 1:
            cargarInvIn()
            menu()
        case 2:
            cargarInsMov()
            menu()
        case 3:
            crearInfoInv()
            menu()
        case 4:
            salir()
        case _:
            print("")
            print("Opción no válida")
            print("")
            menu()

menu()