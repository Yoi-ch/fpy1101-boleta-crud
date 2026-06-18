import os 
boleta = []
nombre = ""
precio = 0
opcion = ""

def agregar_producto (nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    boleta.append(producto)
    print(f"Producto '{nombre}' agregado correctamente")

def calcular_total():
    total = 0
    for producto in boleta :
        total = total + producto["precio"]
    return total

boleta= []
def mostrar_boleta():
    if len(boleta) == 0:
        print("Tu boleta se encunetra vacia")
    else:
        print("\n-----BOLETA-------")
        for producto in boleta:
             print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f" TOTAL: ${calcular_total()}")
        print("--------------------\n")

def actualizar_precio(nombre, nuevo_precio):
    for producto in boleta:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
            return
    print(f"Producto '{nombre}' no encontrado.")




def eliminar_producto(nombre):
    for producto in boleta:
        if producto["nombre"] == nombre:
            boleta.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

    



while True:
    os.system("cls")
    print("-----Administrador de Boletas-----")
    print("1.-Agregar Producto")
    print("2.-Mostrar Boleta")
    print("3.-Modificar Producto")
    print("4.-Eliminar Producto")
    print("5.-Salir")
    print("----------------------------------")
    opcion =input("Opcion: ")

    if opcion == "1":
        os.system("cls")
        nombre=input("Nombre: ")
        precio= int(input("Precio: "))
        agregar_producto(nombre,precio)
        input("Enter para continuar...")
    elif opcion == "2":
        os.system("cls")
        mostrar_boleta()
        input("Enter para continuar...")
    elif opcion == "3":
        os.system("cls")
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        actualizar_precio(nombre,precio)
        input("Enter para continuar...")

    elif opcion =="4":
        os.system("cls")
        nombre= input("Nombre: ")
        eliminar_producto(nombre)
        input("Enter para continuar...")
    elif opcion =="5":
        os.system("cls")
        print("Salir...")
        input("Enter para continuar...")
        break
    else:
        os.system("cls")
        print("opcion invalida")
        input("Enter para continuar...")

