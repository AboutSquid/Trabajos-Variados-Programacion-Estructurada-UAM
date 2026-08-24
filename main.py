import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import random

#Ventana
ventana = tk.Tk()
ventana.title("Ruleta")
ventana.configure(background="lightblue")
ventana.geometry("800x900")
#Estilo creado
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Azul.TButton",
                 background="steelblue",
                 foreground="white",
                 font=("Arial", 14, "bold"),
                 borderwidth=0,
                 padding=10)
estilo.map("Azul.TButton",
           background=[("active", "#2c5f8a")])


# Funciones a llamar
def Salir():
    ventana.destroy()
def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()
#Menu
def menu():
    limpiar()
    etiqueta = tk.Label(ventana, text="Bienvenido a la ruleta",
                    font=("Arial", 14, "bold"),
                    fg="white", bg="steelblue")
    etiqueta.pack(pady=10)

    btnEmpezar = ttk.Button(ventana, text="Empezar", style="Azul.TButton", command = empezar)
    btnEmpezar.pack(pady=10)

    btnSalir = ttk.Button(ventana, text="Salir", style="Azul.TButton", command=Salir)
    btnSalir.pack(pady=10)

    btnCreditos = ttk.Button(ventana, text="Creditos", style="Azul.TButton", command=creditos)
    btnCreditos.pack(pady=10)
#Empezar
def empezar():
    limpiar()
    lienzo = tk.Canvas(ventana, width=600, height=600, bg="lightblue")
    ventana.title("RULETA")

    # colores para la ruleta
    colores = [
        "red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta",
        "pink", "gold", "coral", "violet", "turquoise", "lime", "salmon", "khaki",
        "plum", "orchid", "olive", "teal", "navy", "crimson", "tomato", "skyblue", "black"
    ]

    lienzo.grid(column=10, row=0)

    botones = tk.Frame(ventana, bg="lightblue", bd=10, relief="flat")
    alumnos(botones, lienzo, colores)

    botones.grid(column=10, row=2)


#Sistema de Nombres y de la ruleta
def alumnos(botones, lienzo, colores):
    # nombres de los estudiantes
    nombres = [
        "Gretchen Aburto", "Francisco Álvarez", "Guillermo Ayerdis", "Carlos Benavides",
        "José René Bonilla", "Alex Carballo", "Carlos Castillo", "Raúl Castillo", "Camilo Cruz",
        "Leah Dávila", "William Hawkins", "Mauricio Lacayo", "Sofía Martínez", "Dorian Martínez",
        "Reynaldo Mondragón", "Alejandro Mondragón", "Gylbert Ordoñez", "Alyssa Rodríguez", "Shane Rodríguez",
        "Esmeralda Rodríguez-Salinas", "Francisco Silva", "Evenyer Solorzáno", "Julissa Somarriba",
        "Miguel Suarez", "Jocksand Valladares"
    ]

    cx = 300
    cy = 300
    R = 250

    ListaDeRandoms = tk.Text(botones, width=20, height=10, bg="white")
    ListaDeRandoms.grid(column=10, row=1, rowspan=11, padx=40, pady=11)
    for nombre in nombres:
        ListaDeRandoms.insert(tk.END, f"{nombre}\n")

    # participantes actualmente en la ruleta (se van quitando si se elige eliminar)
    activos = list(nombres)

    # bool que decide si el ganador de cada giro se elimina de la ruleta o no
    eliminar_var = tk.BooleanVar(value=True)

    arco_ids = []
    texto_ids = []
    inicios_base = []
    medios_base = []
    estado = {"offset": 0.0, "velocidad": 0.0, "girando": False, "n": 0}

    def dibujar_ruleta():
        lienzo.delete("rueda")
        arco_ids.clear()
        texto_ids.clear()
        inicios_base.clear()
        medios_base.clear()

        n = len(activos)
        estado["n"] = n
        estado["offset"] = 0.0
        if n == 0:
            return

        paso = 360 / n
        angulo = -paso
        for i in range(n):
            angulo = angulo + paso
            arco_id = lienzo.create_arc(50, 50, 550, 550, start=angulo, extent=paso,
                                        fill=colores[i % len(colores)], tags="rueda")
            medio = angulo + paso / 2
            rad = math.radians(medio)
            x = cx + (R - 10) * math.cos(rad)
            y = cy - (R - 10) * math.sin(rad)

            texto_id = lienzo.create_text(x, y, text=str(activos[i]),
                               fill="white", font=("Arial", 9, "bold"),
                               angle=medio, anchor="e", tags="rueda")

            arco_ids.append(arco_id)
            texto_ids.append(texto_id)
            inicios_base.append(angulo)
            medios_base.append(medio)

    def recargar_lista():
        # toma lo que el usuario haya escrito/editado en el cuadro de texto
        # y lo vuelve la lista de participantes activos de la ruleta
        texto_nuevo = ListaDeRandoms.get("1.0", tk.END).strip().split('\n')
        nombres_limpios = [n for n in texto_nuevo if n.strip() != ""]
        if len(nombres_limpios) > 0:
            activos.clear()
            activos.extend(nombres_limpios)
            dibujar_ruleta()
            btnGirar.state(["!disabled"])

    dibujar_ruleta()

    # flecha fija que señala al ganador (no rota con la ruleta)
    lienzo.create_polygon(285, 30, 315, 30, 300, 55, fill="black", outline="white")

    def dibujar_rotacion():
        offset = estado["offset"]
        for i in range(estado["n"]):
            nuevo_inicio = (inicios_base[i] + offset) % 360
            lienzo.itemconfig(arco_ids[i], start=nuevo_inicio)

            nuevo_medio = medios_base[i] + offset
            rad = math.radians(nuevo_medio)
            x = cx + (R - 10) * math.cos(rad)
            y = cy - (R - 10) * math.sin(rad)
            lienzo.coords(texto_ids[i], x, y)
            lienzo.itemconfig(texto_ids[i], angle=nuevo_medio % 360)

    def animar():
        estado["offset"] = (estado["offset"] + estado["velocidad"]) % 360
        dibujar_rotacion()
        estado["velocidad"] *= 0.97
        if estado["velocidad"] > 0.3:
            ventana.after(20, animar)
        else:
            estado["girando"] = False
            anunciar_ganador()

    def anunciar_ganador():
        n = estado["n"]
        paso = 360 / n
        relativo = (90 - estado["offset"]) % 360
        indice = int(relativo // paso) % n
        ganador = activos[indice]
        messagebox.showinfo("Ganador", f"¡El ganador es {ganador}!")

        if eliminar_var.get():
            del activos[indice]
            dibujar_ruleta()

        if len(activos) == 0:
            btnGirar.state(["disabled"])
        else:
            btnGirar.state(["!disabled"])

    def girar():
        if estado["girando"] or len(activos) == 0:
            return
        estado["girando"] = True
        btnGirar.state(["disabled"])
        estado["velocidad"] = random.uniform(28, 36)
        animar()

    btnActualizar = ttk.Button(botones, text="Actualizar lista", style="Azul.TButton", command=recargar_lista)
    btnActualizar.grid(column=3, row=0, pady=11)

    chkEliminar = ttk.Checkbutton(botones, text="Eliminar participante al ganar", variable=eliminar_var)
    chkEliminar.grid(column=3, row=1, pady=5)

    btnGirar = ttk.Button(botones, text="Girar", style="Azul.TButton", command=girar)
    btnGirar.grid(column=3, row=2, pady=11)

    btnSalir = ttk.Button(botones, text="Salir", style="Azul.TButton", command=menu)
    btnSalir.grid(column=3, row=3, pady=11)


#Creditos
def creditos():
    limpiar()
    Titulo = tk.Label(ventana, text="Creditos",
                    font=("Arial", 14, "bold"),
                    fg="white", bg="steelblue")
    Titulo.pack(pady=10)
    PersonasTxT = tk.Label(ventana, text="""1. Raul
    2. Jocksand
    3. Francisco
    4. Mauricio
    5. Braxus Calzones

    FIN""", font=("Arial", 14, "bold"),
                    fg="white", bg="steelblue")
    PersonasTxT.pack(pady=10)
    btnSalir = ttk.Button(ventana, text="Salir", style="Azul.TButton", command=menu)
    btnSalir.pack(pady=10)
menu()
ventana.mainloop()
