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
    while True:

        try:
            FilaDeSolicitudes[0][0]
            print("La primera solicitud a procesar es: ")
            print("=====================================")
            print("1.-----------------------------------")
            print("Nombre: ", FilaDeSolicitudes[0][0])
            print("Equipo Afectado: ", FilaDeSolicitudes[0][1])
            print("Descripcion: ", FilaDeSolicitudes[0][2])
            print("1.-----------------------------------")
            print("""
            1.Eliminar solicitud
            2.Salir""")
            print("======================================")
            try:
                Seleccion = int(input("Ingrese el numero de la opcion: "))
                match Seleccion:
                    case 1:
                        ValorEliminado = FilaDeSolicitudes.popleft()
                        print("El valor eliminado es: ", ValorEliminado)
                    case 2:
                        break
                    case _:
                        print("Opcion invalida")
            except ValueError:
                print("Error en el formato")

        except IndexError:
            print("No hay problemas por resolver")
            break


def consultarProximaSolicitud(CantidadSolicitud):
    if CantidadSolicitud >0:
        print("La próxima solicitud a procesar es: ")
        print("=====================================")
        print("-----------------------------------")
        print("Nombre: ", FilaDeSolicitudes[0][0])
        print("Equipo Afectado: ", FilaDeSolicitudes[0][1])
        print("Descripción: ", FilaDeSolicitudes[0][2])
        print("-----------------------------------")
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
            case 2:
                ProcesarSolicitud()
            case 3:
                consultarProximaSolicitud(CantidadDeSolicitudes)
            case 6:
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        print("Error en el formato")


