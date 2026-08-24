import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import random

COLOR_BG = "#eef3fb"
COLOR_HEADER = "#1c4e80"
COLOR_CARD = "#ffffff"
COLOR_PRIMARY = "#f2994a"
COLOR_PRIMARY_ACTIVE = "#d97f2e"
COLOR_SECONDARY = "#2c5f8a"
COLOR_SECONDARY_ACTIVE = "#1c4a68"
COLOR_TEXT = "#22303f"
COLOR_MUTED = "#5a6b7b"

FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_SUBTITULO = ("Arial", 11)
FUENTE_SECCION = ("Arial", 11, "bold")
FUENTE_TEXTO = ("Arial", 12)

#Ventana
ventana = tk.Tk()
ventana.title("Ruleta")
ventana.configure(background=COLOR_BG)
ventana.geometry("560x560")

#Estilo creado
estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure("Primary.TButton",
                 background=COLOR_PRIMARY,
                 foreground="white",
                 font=("Arial", 14, "bold"),
                 borderwidth=0,
                 padding=12)
estilo.map("Primary.TButton",
           background=[("active", COLOR_PRIMARY_ACTIVE)])

estilo.configure("Secondary.TButton",
                 background=COLOR_SECONDARY,
                 foreground="white",
                 font=("Arial", 12, "bold"),
                 borderwidth=0,
                 padding=10)
estilo.map("Secondary.TButton",
           background=[("active", COLOR_SECONDARY_ACTIVE)])

estilo.configure("Info.TCheckbutton",
                 background=COLOR_CARD,
                 foreground=COLOR_TEXT,
                 font=("Arial", 10, "bold"))
estilo.map("Info.TCheckbutton", background=[("active", COLOR_CARD)])


# Funciones a llamar
def Salir():
    ventana.destroy()
def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()
#Menu
def menu():
    limpiar()
    ventana.title("Ruleta")
    ventana.geometry("560x560")
    ventana.configure(background=COLOR_BG)

    tarjeta = tk.Frame(ventana, bg=COLOR_CARD, highlightbackground=COLOR_SECONDARY, highlightthickness=2)
    tarjeta.place(relx=0.5, rely=0.5, anchor="center", width=420, height=400)

    tk.Label(tarjeta, text="O", font=("Arial", 48), bg=COLOR_CARD).pack(pady=(30, 5))
    tk.Label(tarjeta, text="Ruleta de Sorteo", font=FUENTE_TITULO,
             fg=COLOR_HEADER, bg=COLOR_CARD).pack(pady=(0, 5))
    tk.Label(tarjeta, text="Gira, elimina participantes y encuentra al ganador",
             font=FUENTE_SUBTITULO, fg=COLOR_MUTED, bg=COLOR_CARD).pack(pady=(0, 25))

    btnEmpezar = ttk.Button(tarjeta, text="Empezar", style="Primary.TButton", command=empezar, width=22)
    btnEmpezar.pack(pady=6)

    btnCreditos = ttk.Button(tarjeta, text="Créditos", style="Secondary.TButton", command=creditos, width=22)
    btnCreditos.pack(pady=6)

    btnSalir = ttk.Button(tarjeta, text="Salir", style="Secondary.TButton", command=Salir, width=22)
    btnSalir.pack(pady=6)
#Empezar
def empezar():
    limpiar()
    ventana.title("Ruleta — Girando")
    ventana.geometry("1020x700")
    ventana.configure(background=COLOR_BG)

    encabezado = tk.Frame(ventana, bg=COLOR_HEADER)
    encabezado.pack(side="top", fill="x")
    tk.Label(encabezado, text="Ruleta", font=("Arial", 18, "bold"),
             fg="white", bg=COLOR_HEADER).pack(pady=14)

    contenido = tk.Frame(ventana, bg=COLOR_BG)
    contenido.pack(fill="both", expand=True, padx=25, pady=20)
    contenido.columnconfigure(0, weight=1)
    contenido.columnconfigure(1, weight=0)

    panel_ruleta = tk.Frame(contenido, bg=COLOR_BG)
    panel_ruleta.grid(row=0, column=0, sticky="n")

    lienzo = tk.Canvas(panel_ruleta, width=600, height=600, bg=COLOR_BG, highlightthickness=0)
    lienzo.pack()

    # colores para la ruleta
    colores = [
        "red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta",
        "pink", "gold", "coral", "violet", "turquoise", "lime", "salmon", "khaki",
        "plum", "orchid", "olive", "teal", "navy", "crimson", "tomato", "skyblue", "black"
    ]

    panel_controles = tk.Frame(contenido, bg=COLOR_BG)
    panel_controles.grid(row=0, column=1, sticky="n", padx=(25, 0))

    alumnos(panel_controles, lienzo, colores)


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

    marco_lista = tk.LabelFrame(botones, text="Participantes", font=FUENTE_SECCION,
                                 fg=COLOR_HEADER, bg=COLOR_CARD, bd=2, relief="groove",
                                 padx=12, pady=12)
    marco_lista.pack(fill="x", pady=(0, 16))

    ListaDeRandoms = tk.Text(marco_lista, width=26, height=12, bg="white", fg=COLOR_TEXT,
                              relief="flat", highlightthickness=1, highlightbackground=COLOR_SECONDARY,
                              font=("Arial", 10))
    ListaDeRandoms.pack(pady=(0, 10))
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
            lienzo.tag_raise("frente")
            return

        paso = 360 / n
        angulo = -paso
        for i in range(n):
            angulo = angulo + paso
            arco_id = lienzo.create_arc(50, 50, 550, 550, start=angulo, extent=paso,
                                        fill=colores[i % len(colores)], outline=COLOR_CARD, width=1, tags="rueda")
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

        # el aro, el eje y la flecha siempre deben quedar por encima de la rueda
        lienzo.tag_raise("frente")

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

    # aro decorativo, eje central y flecha fija que señala al ganador
    lienzo.create_oval(45, 45, 555, 555, outline=COLOR_HEADER, width=4, tags="frente")
    lienzo.create_oval(280, 280, 320, 320, fill="white", outline=COLOR_HEADER, width=3, tags="frente")
    lienzo.create_polygon(285, 22, 315, 22, 300, 55, fill=COLOR_PRIMARY, outline="white", width=2, tags="frente")

    dibujar_ruleta()

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

    btnActualizar = ttk.Button(marco_lista, text="Actualizar lista", style="Secondary.TButton",
                                command=recargar_lista, width=22)
    btnActualizar.pack()

    marco_controles = tk.LabelFrame(botones, text="Controles", font=FUENTE_SECCION,
                                     fg=COLOR_HEADER, bg=COLOR_CARD, bd=2, relief="groove",
                                     padx=12, pady=12)
    marco_controles.pack(fill="x")

    chkEliminar = ttk.Checkbutton(marco_controles, text="Eliminar participante al ganar",
                                   variable=eliminar_var, style="Info.TCheckbutton")
    chkEliminar.pack(anchor="w", pady=(0, 12))

    btnGirar = ttk.Button(marco_controles, text="Girar", style="Primary.TButton", command=girar, width=22)
    btnGirar.pack(pady=(0, 8))

    btnSalir = ttk.Button(marco_controles, text="Salir al menú", style="Secondary.TButton",
                           command=menu, width=22)
    btnSalir.pack()


#Creditos
def creditos():
    limpiar()
    ventana.title("Créditos")
    ventana.geometry("560x560")
    ventana.configure(background=COLOR_BG)

    tarjeta = tk.Frame(ventana, bg=COLOR_CARD, highlightbackground=COLOR_SECONDARY, highlightthickness=2)
    tarjeta.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

    tk.Label(tarjeta, text="Créditos", font=FUENTE_TITULO, fg=COLOR_HEADER, bg=COLOR_CARD).pack(pady=(30, 20))

    equipo = ["Raul", "Jocksand", "Francisco", "Mauricio", "Braxus Calzones"]
    for persona in equipo:
        tk.Label(tarjeta, text=f"•  {persona}", font=FUENTE_TEXTO, fg=COLOR_TEXT,
                 bg=COLOR_CARD, anchor="w").pack(fill="x", padx=60, pady=4)

    btnSalir = ttk.Button(tarjeta, text="Volver", style="Secondary.TButton", command=menu, width=18)
    btnSalir.pack(pady=25)


menu()
ventana.mainloop()
