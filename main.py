import tkinter as tk

ventana = tk.Tk()                 # crea la ventana principal
ventana.title("Mi aplicación")
ventana.geometry("400x300")       # ancho x alto
ventana.resizable(False, False)   # bloquea redimensionar (x, y)

ventana.mainloop()                # bucle de eventos: SIEMPRE al final