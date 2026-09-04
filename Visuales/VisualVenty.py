import tkinter as tk

def CrearVentana(NombreVentana, TamanoVentana, ColorVentana):
    ventana = tk.Tk()
    ventana.title(NombreVentana)
    ventana.geometry(TamanoVentana)
    ventana.config(background=ColorVentana)
    return ventana

def CrearBoton(Ventana, Texto, Accion, posicionx, posiciony, colorTexto, colorDelineado, colorFondo):
    boton = tk.Button(Ventana, text=Texto, command=Accion, highlightbackground=colorDelineado,bg=colorFondo, fg=colorTexto)
    boton.grid(row=posiciony, column=posicionx, padx=10, pady=10)
    return boton

def CrearTexto(Ventana, Texto):
    texto = tk.Text(Ventana, Texto)

shit = CrearVentana("Hi","500x500","green")
def saludar():
    print("Saludo")
CrearTexto(shit,"a")
CrearBoton(shit,"Mima", saludar,0,0, "red", "black", "White")
tk.mainloop()
