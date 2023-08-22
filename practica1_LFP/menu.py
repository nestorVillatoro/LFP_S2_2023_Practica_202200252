print("----------------------------------------------------------------")
print("| practica 1 - Lenguajes formales y de programación seccion B+ |")
print("----------------------------------------------------------------")
nombres = []
cantidades =[]
precios = []
ubicaciones = []
def cargarInvIn():
    print("-----------Cargar inventario inicial-----------")
    print("Que desea hacer?")
    print("1. Exportar")
    print("2. Agregar manualmente")
    op = int(input("Ingrese una opción: "))
    match op:
        case 1:
            ruta = input("Ingrese la ruta del archivo: ")
            archivo = open(ruta, "r", encoding="utf-8")

            for linea in archivo.readlines():
                remp = linea.split(" ")
                items = remp[1].split(";")
                nombres.append(items[0])
                cantidades.append(int(items[1]))
                precios.append(float(items[2]))
                ubicaciones.append(items[3].strip("\n"))

            archivo.close()

            print("Nombres:", nombres)
            print("Cantidades:", cantidades)
            print("Precios:", precios)
            print("Ubicaciones:", ubicaciones)
        case 2:
            print("-----------Cargar inventario inicial-----------")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("ingrese la cantidad: "))
            precio = float(input("ingrese el precio: "))
            ubicacion = input("ingrese la ubicacion: ")

            for i in range(len(nombres)):
                if nombre == nombres[i] & ubicacion == ubicaciones[i]:
                    print("el producto ya existe en esta ubicacion")
                    menu()

            nombres.append(nombre)
            cantidades.append(cantidad)
            precios.append(precio)
            ubicaciones.append(ubicacion)
            archivo = open('inventario.inv', 'a+')
            archivo.write("\ncrear_producto " + nombre + "; " + str(cantidad) + "; " + str(precio) + "; " + ubicacion + " ")
            archivo.seek(0)
            var_inv = archivo.read()
            print("")
            print(var_inv)
            print("")
            archivo.close()
        case _:
            print("Opción no válida")
            menu()
    input("Presione una tecla para continuar...")

def cargarInsMov():
    print("-----------Cargar Instrucciones de Movimientos-----------")
    print("Que desea hacer?")
    print("1. Exportar")
    print("2. Cargar manualmente")
    ops = int(input("Ingrese una opción: "))
    match ops:
        case 1: 
            ruta = input("Ingrese la ruta del archivo: ")
            archivo = open(ruta, "r", encoding="utf-8")

            for linea in archivo.readlines():
                remp = linea.strip().split(";")
                items = remp[0].split(" ")
                accion = items[0]
                nombre = items[1]
                cantidad = int(remp[1])
                ubicacion = remp[2]
                if accion == "agregar_stock":
                    com = False
                    for i in range(len(ubicaciones)):
                        if ubicacion == ubicaciones[i] and nombre == nombres[i]:
                                cantidades[i] = cantidades[i] + cantidad
                                com = True
                                break
                    if com == False:
                        print("Producto o Ubicación no encontrados!")

                elif accion == "vender_producto":
                    com = False
                    for i in range(len(ubicaciones)):
                        if ubicacion == ubicaciones[i] and nombre == nombres[i]:
                                if cantidad <= cantidades[i]:
                                    cantidades[i] = cantidades[i] - cantidad
                                else:
                                    print("La cantidad a vender no puede ser mayor al stock!")
                                com = True
                                break
                        
                    if com == False:
                        print("Producto o Ubicación no encontrados!")

                else:
                    break
                
            archivo.close()

            print("Nombres:", nombres)
            print("Cantidades:", cantidades)
            print("Precios:", precios)
            print("Ubicaciones:", ubicaciones)
        case 2:
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
                    com = False
                    for i in range(len(ubicaciones)):
                        if ubicacion == ubicaciones[i] and nombre == nombres[i]:
                                cantidades[i] = cantidades[i] + cantidad
                                com = True
                                break
                        
                    if com == False:
                        print("Producto o Ubicación no encontrados!")
                        cargarInsMov()

                    archivo = open('movimientos.mov', 'a+')
                    archivo.write("\nagregar_stock " + nombre + "; " + str(cantidad) + "; " + ubicacion + " ")
                    archivo.seek(0)
                    var_mov = archivo.read()
                    print("")
                    print(var_mov)
                    print("")
                    archivo.close()
        
                case 2:
                    nombre = input("Ingrese el nombre del producto que desea vender: ")
                    cantidad = int(input("Ingrese la cantidad que desea vender: "))
                    ubicacion = input("Ingrese la ubicacion donde desea vender: ")
                    com = False
                    for i in range(len(ubicaciones)):
                        if ubicacion == ubicaciones[i] and nombre == nombres[i]:
                                if cantidad <= cantidades[i]:
                                    cantidades[i] = cantidades[i] - cantidad
                                else:
                                    print("La cantidad a vender no puede ser mayor al stock!")
                                    cargarInsMov()
                                com = True
                                break
                        
                    if com == False:
                        print("Producto o Ubicación no encontrados!")
                        cargarInsMov()

                    archivo = open('movimientos.mov', 'a+')
                    archivo.write("\nagregar_stock " + nombre + "; " + str(cantidad) + "; " + ubicacion + " ")
                    archivo.seek(0)
                    var_mov = archivo.read()
                    print("")
                    print(var_mov)
                    print("")
                    archivo.close()
                    print("Opción no válida")
                    cargarInsMov()
        case _:
            print("Opcion no valida")
            menu()
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