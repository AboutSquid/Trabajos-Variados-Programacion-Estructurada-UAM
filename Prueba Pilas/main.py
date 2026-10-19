from collections import deque
"""========================================
 SISTEMA DE SOPORTE TÉCNICO UNIVERSITARIO
========================================

1. Registrar solicitud
2. Procesar siguiente solicitud
3. Consultar próxima solicitud
4. Mostrar solicitudes pendientes
5. Consultar cantidad de solicitudes
6. Salir
"""
FilaDeSolicitudes = []
HistorialDesolicitudes = []

#Funciones a realizar
CantidadDeSolicitudes = 0
def RegistrarSolicitud():
    global CantidadDeSolicitudes
    Nombre = input("Ingrese su nombre: ")
    EquipoAfectado = input("Ingrese el equipo afectado: ")
    Descripcion = input("Ingrese la descripcion del problema: ")
    FilaDeSolicitudes = deque()
    FilaDeSolicitudes.append([Nombre, EquipoAfectado, Descripcion])
    CantidadDeSolicitudes += 1

def ProcesarSolicitud():
    global CantidadDeSolicitudes

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
            case 6:
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        print("Error en el formato")


