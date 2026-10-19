
def Validar(StringIsINT, Min, Texto):
    while True:
        try:
            if StringIsINT == "Si":
                Cantidad = int(input(Texto))
            else:
                Cantidad = float(input(Texto))

            if Cantidad <= Min:
                print(f"Introduce un numero mayor que {Min}")
            else:
                return Cantidad

        except ValueError:
            print("Introduce un numero")


def RegistrarProductos(ListaProductosNombre, ListaProductosCantidad, ListaProductosPrecio):
    print("---Proceso de registro---")
    Nombre = input("Introduce el nombre del producto: ")
    Nombre = Nombre.lower()
    if Nombre == "fin":
        return False
    else:
        Cantidad = Validar("Si", 0, "Ingrese la cantidad de productos: ")
        Precio = Validar("No", 0, "Ingrese el precio del producto: ")
        ListaProductosNombre.append(Nombre)
        ListaProductosCantidad.append(Cantidad)
        ListaProductosPrecio.append(Precio)
        return True


def MostrarFactura(ListaProductosNombre, ListaProductosCantidad, ListaProductosPrecio):
    if len(ListaProductosNombre) == 0:
        print("No hay productos registrados")
        return

    print("\n---Factura---")
    Total = 0
    for i in range(len(ListaProductosNombre)):
        Subtotal = ListaProductosCantidad[i] * ListaProductosPrecio[i]
        Total = Total + Subtotal
        print(f"Producto: {ListaProductosNombre[i]}, Cantidad: {ListaProductosCantidad[i]}, Precio: {ListaProductosPrecio[i]:.2f}, Subtotal: {Subtotal:.2f}")

    print(f"\nTotal sin descuento: {Total:.2f}")

    if Total >= 3000:
        Descuento = Total * 0.08
        print(f"Descuento del 8%: -{Descuento:.2f}")
    else:
        Descuento = 0
        print("No aplica descuento (el total no llega a 3000)")

    TotalConDescuento = Total - Descuento
    print(f"Total con descuento: {TotalConDescuento:.2f}")

    IVA = TotalConDescuento * 0.15
    TotalFinal = TotalConDescuento + IVA
    print(f"IVA del 15%: +{IVA:.2f}")
    print(f"Total a pagar: {TotalFinal:.2f}")


ListaProductosNombre = []
ListaProductosCantidad = []
ListaProductosPrecio = []
cmd = 0
while cmd != 2:
    print("""
----------------------
Programa de ferreteria
----------------------
1. Ingresar nombre producto, precio y cantidad
2. Salir""")
    cmd = Validar("Si", 0, "Introduce el numero de la opcion deseada: ")
    if cmd == 1:
        print("Ingresa los datos, escribe <fin> cuando termines los productos")
        d = "s"
        while d == "s":
            if RegistrarProductos(ListaProductosNombre, ListaProductosCantidad, ListaProductosPrecio) == False:
                break
            d = input("Quieres continuar s/n? ")
            d = d.lower()

        MostrarFactura(ListaProductosNombre, ListaProductosCantidad, ListaProductosPrecio)

    elif cmd != 2:
        print("Opcion no valida")

print("Programa terminado")
