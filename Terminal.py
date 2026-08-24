import os
import sys
import time
import random


NOMBRES_BASE = [
    "Gretchen Aburto", "Francisco Álvarez", "Guillermo Ayerdis", "Carlos Benavides",
    "José René Bonilla", "Alex Carballo", "Carlos Castillo", "Raúl Castillo", "Camilo Cruz",
    "Leah Dávila", "William Hawkins", "Mauricio Lacayo", "Sofía Martínez", "Dorian Martínez",
    "Reynaldo Mondragón", "Alejandro Mondragón", "Gylbert Ordoñez", "Alyssa Rodríguez", "Shane Rodríguez",
    "Esmeralda Rodríguez-Salinas", "Francisco Silva", "Evenyer Solorzáno", "Julissa Somarriba",
    "Miguel Suarez", "Jocksand Valladares"
]

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
            sorteo()
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
        print(f"  {i:>2}. {nombre}")


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


def sorteo():
    activos = list(NOMBRES_BASE)
    eliminar_al_ganar = True

    while True:
        limpiar()
        encabezado("RULETA DE SORTEO — Girando")
        mostrar_participantes(activos)

        estado_eliminar = "SI" if eliminar_al_ganar else "NO"
        print(f"\nEliminar participante al ganar: {estado_eliminar}")
        print("\n  1) Girar")
        print("  2) Editar lista de participantes")
        print("  3) Eliminar un participante manualmente")
        print("  4) Restablecer lista original")
        print("  5) Activar/desactivar eliminar al ganar")
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
                activos.remove(ganador)
            pausa()
        elif opcion == "2":
            editar_lista(activos)
        elif opcion == "3":
            eliminar_manual(activos)
        elif opcion == "4":
            activos = list(NOMBRES_BASE)
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
