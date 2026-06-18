
boleta = []   


def agregar_producto(nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    boleta.append(producto)
    print(f"Producto '{nombre}' agregado.")


def calcular_total():
    total = 0
    for producto in boleta:
        total = total + producto["precio"]
    return total

def mostrar_boleta():
    if len(boleta) == 0:
        print("La boleta está vacía.")
    else:
        print("\n------ BOLETA ------")
        for producto in boleta:
            print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f"  TOTAL: ${calcular_total()}")
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
            print(f"Producto '{nombre}' eliminado.")
            return
    print(f"Producto '{nombre}' no encontrado.")



agregar_producto("Leche",   1200)
agregar_producto("Pan",     850)
agregar_producto("Queso",   3200)


mostrar_boleta()


actualizar_precio("Leche", 1350)


eliminar_producto("Pan")


mostrar_boleta()