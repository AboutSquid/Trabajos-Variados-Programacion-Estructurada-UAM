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

CantidadDeSolicitudes = 0
def RegistrarSolicitud():
    global CantidadDeSolicitudes
    Nombre = input("Ingrese su nombre: ")
    EquipoAfectado = input("Ingrese el equipo afectado: ")
    Descripcion = input("Ingrese la descripcion del problema: ")
    FilaDeSolicitudes = deque()
    FilaDeSolicitudes.append([Nombre, EquipoAfectado, Descripcion])
    CantidadDeSolicitudes += 1

