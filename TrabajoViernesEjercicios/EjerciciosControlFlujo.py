def Ejercicio1IF():
    ListaProductos = ["Coca-cola", "Pepsi"]
    ListaUnidades = [5,10]
    #La pulpería La Esquina necesita reponer un producto cuando quedan menos de 5 unidades. Solicita el nombre y la existencia; muestra una alerta cuando corresponda.
    while True:
        print("""
        -------------------
        Sistema de pulperia
        -------------------
        1. Ver los productos
        2. Agregar Productos
        3. Salir""")
        while True:
            try:
                InputSeleccionar = int(input("Introduce un numero entero: "))
                while True:
                    match InputSeleccionar:
                        case 1:
                            print("La lista de los productos es: ")
                            print("|Nombre|", "|Cantidad|", "|Observaciones")
                            for i in range(len(ListaProductos)):
                                print(ListaProductos[i], ListaUnidades[i], " Alerta pocas unidades" if ListaUnidades[i] <= 5 else "Suficientes unidades")
                            break
                        case 2:
                            print("Agrega productos: ")
                            productosnombre = input("Introduce el nombre del producto: ")
                            while True:
                                try:
                                    cantidadproductos = int(input("Introduce la cantidad de productos: "))
                                    while True:
                                        if cantidadproductos < 0:
                                            print("Introduce un numero mayor a 0")
                                            cantidadproductos = int(input("Introduce la cantidad de productos: "))
                                        else:
                                            ListaUnidades.append(cantidadproductos)
                                            break
                                    break
                                except ValueError:
                                    print("Introduce un numero entero")

                            ListaProductos.append(productosnombre)
                            break
                        case 3:
                            print("Adios")
                            break


                        case _:
                            print("Selecciona una opcion valida")



                            break


                break
            except ValueError:
                print("Introduce un numero entero de la opcion deseada")
        if InputSeleccionar == 3:
            break

def Ejercicio2IF():
    #Una tienda de Masaya aplica una promocion simulada de 10% cuando la compra supera C$1,500. Solicita el monto y muestra el total.
    print("""
    ------------------------
    Promocion de una tienda
    ------------------------""")
    while True:
        try:
            MontoCompra = float(input("Introduce el monto de la compra en C$: "))
            if MontoCompra < 0:
                print("Introduce un numero mayor a 0")
            else:
                break
        except ValueError:
            print("Introduce un numero valido")

    if MontoCompra > 1500:
        Descuento = MontoCompra * 0.10
        TotalPagar = MontoCompra - Descuento
        print("Aplica la promocion del 10%")
        print("El descuento es de C$", Descuento)
    else:
        TotalPagar = MontoCompra
        print("No aplica la promocion, la compra no supera C$1500")

    print("El total a pagar es de C$", TotalPagar)


def Ejercicio3IF():
    #Un emprendimiento fija una meta diaria de C$4,000. Lee el total vendido e informa si se alcanzo; muestra cuanto falto o cuanto se supero.
    MetaDiaria = 4000
    print("""
    ---------------
    Meta de ventas
    ---------------""")
    while True:
        try:
            TotalVendido = float(input("Introduce el total vendido en C$: "))
            if TotalVendido < 0:
                print("Introduce un numero mayor a 0")
            else:
                break
        except ValueError:
            print("Introduce un numero valido")

    if TotalVendido >= MetaDiaria:
        print("Se alcanzo la meta diaria de C$", MetaDiaria)
        print("Se supero la meta por C$", TotalVendido - MetaDiaria)
    else:
        print("No se alcanzo la meta diaria de C$", MetaDiaria)
        print("Falto C$", MetaDiaria - TotalVendido)


def Ejercicio4IF():
    #Un comedor realiza entrega sin recargo desde C$300. Indica si la entrega es gratuita o suma un recargo simulado de C$40.
    print("""
    ----------------------
    Entrega de un comedor
    ----------------------""")
    while True:
        try:
            MontoPedido = float(input("Introduce el monto del pedido en C$: "))
            if MontoPedido < 0:
                print("Introduce un numero mayor a 0")
            else:
                break
        except ValueError:
            print("Introduce un numero valido")

    if MontoPedido >= 300:
        TotalPagar = MontoPedido
        print("La entrega es gratuita")
    else:
        TotalPagar = MontoPedido + 40
        print("La entrega tiene un recargo de C$ 40")

    print("El total a pagar es de C$", TotalPagar)


def Ejercicio5IF():
    #Una bodega espera sacos de 46 kg. Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.
    PesoEsperado = 46
    print("""
    ------------------
    Peso de productos
    ------------------""")
    while True:
        try:
            PesoSaco = float(input("Introduce el peso del saco en kg: "))
            if PesoSaco < 0:
                print("Introduce un numero mayor a 0")
            else:
                break
        except ValueError:
            print("Introduce un numero valido")

    if PesoSaco >= PesoEsperado:
        print("El saco cumple con el peso esperado de", PesoEsperado, "kg")
    else:
        print("El saco debe revisarse, esta debajo del peso esperado")
        print("Faltan", PesoEsperado - PesoSaco, "kg")
