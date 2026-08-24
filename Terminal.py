import os
import sys
import time
import random


# Los participantes están organizados en 8 grupos (según las 8 líneas originales).
GRUPOS = {
    "Grupo 1": ["Gretchen Aburto", "Leah Dávila", "Sofía Martínez", "Guillermo Ayerdis"],
    "Grupo 2": ["Alyssa Rodríguez", "Alejandro Mondragón", "Esmeralda Rodríguez-Salinas"],
    "Grupo 3": ["Camilo Cruz", "Reynaldo Mondragón", "Miguel Suárez"],
    "Grupo 4": ["Gylbert Ordoñez", "Shane Rodríguez", "Julissa Somarriba"],
    "Grupo 5": ["Francisco Álvarez", "Raúl Castillo", "Mauricio Lacayo", "Jocksand Valladares"],
    "Grupo 6": ["José René Bonilla", "William Hawkins", "Dorian Martínez", "Francisco Silva"],
    "Grupo 7": ["Carlos Benavides", "Alex Carballo", "Evenyer Solórzano"],
    "Grupo 8": ["Carlos Castillo"],
}


def construir_nombre_a_grupo():
    mapa = {}
    for grupo, nombres in GRUPOS.items():
        for nombre in nombres:
            mapa[nombre] = grupo
    return mapa


NOMBRE_A_GRUPO = construir_nombre_a_grupo()


def todos_los_nombres():
    resultado = []
    for nombres in GRUPOS.values():
        resultado.extend(nombres)
    return resultado


NOMBRES_BASE = todos_los_nombres()

EQUIPO = ["Raul", "Jocksand", "Francisco", "Mauricio", "Braxus Calzones"]


def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        # secuencia ANSI: no depende del comando externo "clear" ni de TERM
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()


def pausa():
    input("\nPresiona ENTER para continuar...")


def encabezado(titulo):
    ancho = 60
    print("=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho)


def menu():
    while True:
        limpiar()
        encabezado("RULETA DE SORTEO")
        print("\n  1) Empezar")
        print("  2) Créditos")
        print("  3) Salir\n")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # La ruleta SIEMPRE incluye a todos los grupos y participantes.
            sorteo(list(NOMBRES_BASE))
        elif opcion == "2":
            creditos()
        elif opcion == "3":
            print("\n¡Hasta luego!")
            sys.exit(0)
        else:
            input("Opción inválida. Presiona ENTER para intentar de nuevo...")


def creditos():
    limpiar()
    encabezado("CRÉDITOS")
    print()
    for persona in EQUIPO:
        print(f"  •  {persona}")
    pausa()


def mostrar_participantes(activos):
    print(f"\nParticipantes activos ({len(activos)}):")
    if not activos:
        print("  (no quedan participantes)")
        return
    for i, nombre in enumerate(activos, start=1):
        grupo = NOMBRE_A_GRUPO.get(nombre, "sin grupo")
        print(f"  {i:>2}. {nombre}  [{grupo}]")


def mostrar_grupos_restantes(activos):
    grupos_presentes = sorted(
        {NOMBRE_A_GRUPO.get(nombre, "sin grupo") for nombre in activos},
        key=lambda g: (g not in GRUPOS, g),
    )
    print(f"\nGrupos restantes en la ruleta ({len(grupos_presentes)}):")
    if not grupos_presentes:
        print("  (no quedan grupos)")
        return
    for grupo in grupos_presentes:
        print(f"  •  {grupo}")


def girar(activos):
    ganador = random.choice(activos)

    pasos = random.randint(18, 26)
    demora = 0.05
    for paso in range(pasos):
        if paso == pasos - 1:
            nombre_mostrado = ganador
        else:
            nombre_mostrado = random.choice(activos)
        sys.stdout.write(f"\r  Girando... -> {nombre_mostrado}")
        sys.stdout.flush()
        time.sleep(demora)
        demora *= 1.12

    print()
    print(f"\n¡El ganador es: {ganador}! 🎉\n")
    return ganador


def eliminar_grupo_del_ganador(activos, ganador):
    """Elimina de la lista de activos a TODOS los integrantes del grupo
    al que pertenece el ganador (incluyendo al propio ganador)."""
    grupo_ganador = NOMBRE_A_GRUPO.get(ganador)
    if grupo_ganador is None:
        # Si por alguna razón no pertenece a ningún grupo conocido,
        # solo se elimina a esa persona.
        if ganador in activos:
            activos.remove(ganador)
        return []

    integrantes_grupo = [n for n in GRUPOS[grupo_ganador] if n in activos]
    for nombre in integrantes_grupo:
        activos.remove(nombre)
    return integrantes_grupo


def editar_lista(activos):
    print("\nEscribe un nombre por línea. Escribe una línea vacía para terminar.")
    print("(Esto reemplaza la lista actual de participantes)\n")
    nuevos = []
    while True:
        linea = input(f"Nombre {len(nuevos) + 1} (o ENTER para terminar): ").strip()
        if linea == "":
            break
        nuevos.append(linea)

    if nuevos:
        activos.clear()
        activos.extend(nuevos)
        print("\nLista actualizada.")
    else:
        print("\nNo se ingresó ningún nombre, se mantiene la lista anterior.")
    pausa()


def eliminar_manual(activos):
    mostrar_participantes(activos)
    if not activos:
        pausa()
        return
    seleccion = input("\nNúmero del participante a eliminar (o ENTER para cancelar): ").strip()
    if seleccion == "":
        return
    if seleccion.isdigit() and 1 <= int(seleccion) <= len(activos):
        eliminado = activos.pop(int(seleccion) - 1)
        print(f"\nSe eliminó a {eliminado}.")
    else:
        print("\nSelección inválida.")
    pausa()


def sorteo(activos_iniciales):
    activos = list(activos_iniciales)
    eliminar_al_ganar = True

    while True:
        limpiar()
        encabezado("RULETA DE SORTEO — Girando")
        mostrar_participantes(activos)
        mostrar_grupos_restantes(activos)

        estado_eliminar = "SI (elimina TODO el grupo del ganador)" if eliminar_al_ganar else "NO"
        print(f"\nEliminar grupo completo al ganar: {estado_eliminar}")
        print("\n  1) Girar")
        print("  2) Editar lista de participantes")
        print("  3) Eliminar un participante manualmente")
        print("  4) Restablecer lista original")
        print("  5) Activar/desactivar eliminar grupo al ganar")
        print("  6) Volver al menú\n")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if not activos:
                input("\nNo quedan participantes. Presiona ENTER...")
                continue
            limpiar()
            encabezado("RULETA DE SORTEO — Girando")
            ganador = girar(activos)
            if eliminar_al_ganar:
                grupo_ganador = NOMBRE_A_GRUPO.get(ganador, "sin grupo")
                eliminados = eliminar_grupo_del_ganador(activos, ganador)
                if len(eliminados) > 1:
                    print(f"Se eliminó todo el {grupo_ganador} de la ruleta:")
                    for nombre in eliminados:
                        print(f"  •  {nombre}")
                else:
                    print(f"Se eliminó a {ganador} de la ruleta.")
            pausa()
        elif opcion == "2":
            editar_lista(activos)
        elif opcion == "3":
            eliminar_manual(activos)
        elif opcion == "4":
            activos = list(activos_iniciales)
            input("\nLista restablecida. Presiona ENTER...")
        elif opcion == "5":
            eliminar_al_ganar = not eliminar_al_ganar
        elif opcion == "6":
            return
        else:
            input("Opción inválida. Presiona ENTER para intentar de nuevo...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
        sys.exit(0)