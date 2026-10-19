from collections import deque
from filecmp import clear_cache


def consultarProximaSolicitud(FilaDeSolicitudes,CantidadSolicitud):
    if CantidadSolicitud >0:
        proxima = FilaDeSolicitudes[0]
        print(f"---------  Próxima solicitud  ---------\nNombre: {proxima[0]}, Equipo: {proxima[1]}, Descripción: {proxima[2]}")
    else:
        print("No se han registrado solicitudes")

