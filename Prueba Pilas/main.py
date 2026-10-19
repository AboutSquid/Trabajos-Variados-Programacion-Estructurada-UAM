from collections import deque

FilaDeSolicitudes = deque()
HistorialDesolicitudes = []

#Funciones a realizar
CantidadDeSolicitudes = 0
def RegistrarSolicitud():
    global CantidadDeSolicitudes
    Nombre = input("Ingrese su nombre: ")
    EquipoAfectado = input("Ingrese el equipo afectado: ")
    Descripcion = input("Ingrese la descripcion del problema: ")
    FilaDeSolicitudes.append([Nombre, EquipoAfectado, Descripcion])
    CantidadDeSolicitudes += 1

def ProcesarSolicitud():
    global CantidadDeSolicitudes
def consultarProximaSolicitud(CantidadSolicitud):
    if CantidadSolicitud >0:
        proxima = FilaDeSolicitudes[0]
        print(f"---------  Próxima solicitud  ---------\nNombre: {proxima[0]}, Equipo: {proxima[1]}, Descripción: {proxima[2]}")
    else:
        print("No se han registrado solicitudes")



#Main
while True:
    print(f"""
    ========================================
     SISTEMA DE SOPORTE TÉCNICO UNIVERSITARIO
    ========================================

    1. Registrar solicitud
    2. Procesar siguiente solicitud
    3. Consultar próxima solicitud
    4. Mostrar solicitudes pendientes
    5. Consultar cantidad de solicitudes
    6. Salir""")
    try:
        Seleccion = int(input("Ingrese el numero de la opcion: "))
        match Seleccion:
            case 1:
                RegistrarSolicitud()
            case 3:
                consultarProximaSolicitud(CantidadDeSolicitudes)
            case 6:
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        print("Error en el formato")


