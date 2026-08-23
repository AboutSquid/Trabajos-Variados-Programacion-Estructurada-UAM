import tkinter as tk

ventana = tk.Tk()
ventana.title("Ruleta")
ventana.geometry("400x300")
ventana.resizable(True, True)
ventana.configure(background="white")

#Inicio
etiqueta = tk.Label(ventana, text="Bienvenido a la ruleta",
                    font=("Arial", 14, "bold"),
                    fg="white", bg="steelblue")
etiqueta.pack(pady=10)
btnEmpezar = tk.Button(ventana,font=("Arial", 14, "bold"), text="Empezar",bg="steelblue",fg="white")
btnEmpezar.pack(pady=10)

ventana.mainloop()