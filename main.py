import tkinter as tk
from tkinter import ttk


#Ventana
ventana = tk.Tk()
ventana.title("Ruleta")
ventana.configure(background="lightblue")
ventana.geometry("600x600")
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

    btnEmpezar = ttk.Button(ventana, text="Empezar", style="Azul.TButton")
    btnEmpezar.pack(pady=10)

    btnSalir = ttk.Button(ventana, text="Salir", style="Azul.TButton", command=Salir)
    btnSalir.pack(pady=10)

    btnCreditos = ttk.Button(ventana, text="Creditos", style="Azul.TButton", command=creditos)
    btnCreditos.pack(pady=10)

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