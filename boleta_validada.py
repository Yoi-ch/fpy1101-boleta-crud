import os

boleta = []
nombre = ""
precio = 0
opcion = ""

def agregar_producto(nombre, precio):

    
    if nombre.strip() == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return

    
    if precio <= 0:
        print("Error: El precio debe ser mayor que cero.")
        return

    
    for producto in boleta:
        if producto["nombre"].lower() == nombre.lower():
            print("Error: El producto ya existe en la boleta.")
            return

    producto = {"nombre": nombre, "precio": precio}
    boleta.append(producto)
    print(f"Producto '{nombre}' agregado correctamente")


def calcular_total():
    total = 0
    for producto in boleta:
        total = total + producto["precio"]
    return total


def mostrar_boleta():
    if len(boleta) == 0:
        print("Tu boleta se encuentra vacia")
    else:
        print("\n-----BOLETA-------")
        for producto in boleta:
            print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f" TOTAL: ${calcular_total()}")
        print("--------------------\n")


def actualizar_precio(nombre, nuevo_precio):

    
    if nuevo_precio <= 0:
        print("Error: El precio debe ser mayor que cero.")
        return

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

    opcion = input("Opcion: ")

    if opcion == "1":
        os.system("cls")
        nombre = input("Nombre: ")

        
        try:
            precio = int(input("Precio: "))

            
            agregar_producto(nombre, precio)

        except ValueError:
            print("Error: El precio debe ser un número.")

        input("Enter para continuar...")

    elif opcion == "2":
        os.system("cls")
        mostrar_boleta()
        input("Enter para continuar...")

    elif opcion == "3":
        os.system("cls")
        nombre = input("Nombre: ")

        
        try:
            precio = int(input("Precio: "))

            
            actualizar_precio(nombre, precio)

        except ValueError:
            print("Error: El precio debe ser un número.")

        input("Enter para continuar...")

    elif opcion == "4":
        os.system("cls")
        nombre = input("Nombre: ")
        eliminar_producto(nombre)
        input("Enter para continuar...")

    elif opcion == "5":
        os.system("cls")
        print("Salir...")
        input("Enter para continuar...")
        break

    else:
        os.system("cls")
        print("Opcion invalida")
        input("Enter para continuar...")