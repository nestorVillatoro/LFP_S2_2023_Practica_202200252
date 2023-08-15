print("----------------------------------------------------------------")
print("| practica 1 - Lenguajes formales y de programación seccion B+ |")
print("----------------------------------------------------------------")
nombres = []
cantidades =[]
precios = []
ubicaciones = []
def cargarInvIn():
    print("-----------Cargar Inventario Inicial-----------")
    nombre = input("Ingrese el nombre del producto: ")
    nombres.append(nombre)
    cantidad = int(input("ingrese la cantidad: "))
    cantidades.append(cantidad)
    precio = float(input("ingrese el precio: "))
    precios.append(precio)
    ubicacion = input("ingrese la ubicacion: ")
    ubicaciones.append(ubicacion)
    archivo = open('inventario.inv', 'a+')
    archivo.write("\ncrear_producto " + nombre + "; " + str(cantidad) + "; " + str(precio) + "; " + ubicacion + " ")
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
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            ubicacion = input("Ingrese la ubicacion donde desea agregar: ")
            for i in range(len(nombres)):
                if nombre == nombres[i]:
                    if ubicacion == ubicaciones[i]:
                        cantidades[i] = cantidades[i] + cantidad
                        archivo = open('movimientos.mov', 'a+')
                        archivo.write("\nagregar_stock " + nombre + "; " + str(cantidad) + "; " + ubicacion + " ")
                        archivo.seek(0)
                        var_mov = archivo.read()
                        print("")
                        print(var_mov)
                        print("")
                        archivo.close()
                    else:
                        print("El producto no existe en esa ubicacion!")
            
        case 2:
            nombre = input("Ingrese el nombre del producto que desea vender: ")
            cantidad = int(input("Ingrese la cantidad que desea vender: "))
            ubicacion = input("Ingrese la ubicacion donde desea vender: ")
            for i in range(len(nombres)):
                if nombre == nombres[i]:
                    if ubicacion == ubicaciones[i]:
                        if cantidad<cantidades[i]:
                            cantidades[i] = cantidades[i] - cantidad
                            archivo = open('movimientos.mov', 'a+')
                            archivo.write("\nvender_producto " + nombre + "; " + str(cantidad) + "; " + ubicacion + " ")
                            archivo.seek(0)
                            var_mov = archivo.read()
                            print("")
                            print(var_mov)
                            print("")
                            archivo.close()
                        else:
                            print("No hay suficientes existencias!")
                    else:
                        print("El producto no existe en esa ubicacion!")
        case _:
            print("Opción no válida")
            cargarInsMov()
    input("Presione una tecla para continuar...")

def crearInfoInv():
    print("-----------Crear Informe de inventario-----------")
    archivo = open('informe.txt', 'w+')
    archivo.write("--------------------- INFORME DE INVENTARIO ---------------------")
    archivo.write("\nProducto | Cantidad | Precio Unitario | Valor Total | Ubicacion")
    archivo.write("\n----------------------------------------------------------------")
    for i in range(len(nombres)):
        valorTotal = cantidades[i]*precios[i]
        archivo.write("\n" + nombres[i] + "    " + str(cantidades[i]) + "    " + str(precios[i]) + "    " + str(valorTotal) + "    " + ubicaciones[i])
    archivo.seek(0)
    var_informe = archivo.read()
    print("")
    print(var_informe)
    print("")
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