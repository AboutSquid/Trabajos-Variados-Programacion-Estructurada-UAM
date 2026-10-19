def ConsultarCantidad(FilaDeSolicitudes):
    Cantidad = len(FilaDeSolicitudes)
    if Cantidad == 0:
        print("No hay solicitudes pendientes.")
    elif Cantidad == 1:
        print("Hay 1 solicitud pendiente.")
    else:
        print(f"Hay {Cantidad} solicitudes pendientes.")
    return Cantidad
