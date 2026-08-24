import tkinter as tk
from random import random
from tkinter import ttk
import math

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
    lienzo = tk.Canvas(ventana, width=600, height=600, bg= "lightblue")
    ventana.title("RULETA")

    # colores para la ruleta
    colores = [
        "red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta",
        "pink", "gold", "coral", "violet", "turquoise", "lime", "salmon", "khaki",
        "plum", "orchid", "olive", "teal", "navy", "crimson", "tomato", "skyblue", "black"
    ]

    lienzo.grid(column=10, row=0)

    botones = tk.Frame(ventana, bg="lightblue", bd = 10, relief="flat")
    alumnos(botones, lienzo, colores)

    botones.grid(column=10, row=2)
    btnGirar = ttk.Button(botones, text="Girar", style="Azul.TButton")
    btnGirar.grid(column=3, row=1, pady=11)
    btnSalir = ttk.Button(botones, text="Salir", style="Azul.TButton", command=menu)
    btnSalir.grid(column=3, row=2, pady=11)


#Sistema de Nombres
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



    ListaDeRandoms = tk.Text(botones, width=20, height=10, bg="white")
    ListaDeRandoms.grid(column=10, row=1, rowspan=11, padx=40, pady=11)
    for nombre in nombres:
        ListaDeRandoms.insert(tk.END, f"{nombre}\n")

    contenido =ListaDeRandoms.get("1.0", tk.END)
    lista_nombres = contenido.strip().split('\n')
    actualizar(lista_nombres, colores, lienzo)

   # btnanadir = ttk.Button(ventana, text )
   # Menusito = tk.OptionMenu(ventana, nombres, *nombres)
    #Menusito.pack(pady=10)

#actualizar ruleta
def actualizar(lista_nombres, colores, lienzo):
    contador = 0
    num = 360 / len(lista_nombres)  # para calcular el angulo que debe tener cada trozo
    angulo = num*-1
    cx = 300
    cy = 300
    R = 250
    while contador < len(lista_nombres):
        angulo = angulo + num
        lienzo.create_arc(50, 50, 550, 550, start=angulo, extent=num, fill=colores[contador % len(colores)])
        medio = angulo + num / 2
        rad = math.radians(medio)
        x = cx + (R - 10) * math.cos(rad)
        y = cy - (R - 10) * math.sin(rad)

        lienzo.create_text(x, y, text=str(lista_nombres[contador]),
                           fill="white", font=("Arial", 9, "bold"),
                           angle=medio, anchor="e")
        contador = contador + 1
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
    5. Cristhian y Franko por los calzones
    
    FIN""", font=("Arial", 14, "bold"),
                    fg="white", bg="steelblue")
    PersonasTxT.pack(pady=10)
    btnSalir = ttk.Button(ventana, text="Salir", style="Azul.TButton", command=menu)
    btnSalir.pack(pady=10)
menu()
ventana.mainloop()