import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

MAX_INTENTOS = 5          # limite de intentos para no caer en un ciclo infinito
NOTA_MINIMA_APROBAR = 60  # escala 0-100

#Ventana
ventana = tk.Tk()
ventana.title("Calificaciones")
ventana.configure(background="lightblue")
ventana.geometry("500x600")

#Estilo
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Azul.TButton",
                 background="steelblue",
                 foreground="white",
                 font=("Arial", 12, "bold"),
                 borderwidth=0,
                 padding=8)
estilo.map("Azul.TButton",
           background=[("active", "#2c5f8a")])


def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()
    # se quitan los binds de la rueda del mouse de la pantalla anterior,
    # si no se acumulan y terminan apuntando a un canvas ya destruido
    ventana.unbind_all("<MouseWheel>")
    ventana.unbind_all("<Button-4>")
    ventana.unbind_all("<Button-5>")


def pedir_cantidad_estudiantes():
    # WHILE: no se sabe de antemano cuantos intentos va a necesitar el
    # usuario para escribir un numero valido, se repite MIENTRAS el dato
    # siga siendo invalido. Se limita con MAX_INTENTOS para no quedar en
    # un ciclo infinito si el usuario nunca da un valor correcto.
    intentos = 0
    cantidad = None
    while intentos < MAX_INTENTOS and cantidad is None:
        respuesta = simpledialog.askinteger(
            "Grupo",
            "¿Cuántos estudiantes tiene el grupo?",
            parent=ventana, minvalue=1, maxvalue=100
        )
        if respuesta is None:
            ventana.destroy()
            return None

        if respuesta > 0:
            cantidad = respuesta
        else:
            intentos += 1
            messagebox.showwarning("Dato inválido", "Ingresa un número mayor a 0.")

    if cantidad is None:
        messagebox.showerror("Sin datos", "No se ingresó una cantidad válida. Se cerrará el programa.")
        ventana.destroy()
        return None

    return cantidad


def pantalla_ingreso(cantidad):
    limpiar()
    ventana.title("Ingresar notas")

    titulo = tk.Label(ventana, text=f"Notas de {cantidad} estudiantes (3 parciales, 0 a 100 c/u)",
                       font=("Arial", 13, "bold"), fg="white", bg="steelblue")
    titulo.pack(side="top", pady=10, fill="x")

    # --- pie fijo: resultado general y botones (siempre visibles) ---
    pie = tk.Frame(ventana, bg="lightblue")
    pie.pack(side="bottom", fill="x")

    resultado = tk.Label(pie, text="", font=("Arial", 12, "bold"), bg="lightblue", justify="left")
    resultado.pack(pady=(10, 0))

    botones = tk.Frame(pie, bg="lightblue")
    botones.pack(pady=10)

    # --- zona central deslizable: Canvas + Scrollbar ---
    zona_scroll = tk.Frame(ventana, bg="lightblue")
    zona_scroll.pack(side="top", fill="both", expand=True)

    canvas = tk.Canvas(zona_scroll, bg="lightblue", highlightthickness=0)
    scrollbar = ttk.Scrollbar(zona_scroll, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    contenedor = tk.Frame(canvas, bg="lightblue")
    contenedor_id = canvas.create_window((0, 0), window=contenedor, anchor="nw")

    def _actualizar_scrollregion(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def _ajustar_ancho(event):
        canvas.itemconfig(contenedor_id, width=event.width)

    contenedor.bind("<Configure>", _actualizar_scrollregion)
    canvas.bind("<Configure>", _ajustar_ancho)

    def _con_rueda(event):
        if event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, "units")

    # se usa bind_all para poder desplazarse aunque el mouse este sobre
    # cualquier campo de texto de la lista, no solo sobre el canvas
    canvas.bind_all("<MouseWheel>", _con_rueda)
    canvas.bind_all("<Button-4>", _con_rueda)
    canvas.bind_all("<Button-5>", _con_rueda)

    encabezados = ["Estudiante", "Parcial 1", "Parcial 2", "Parcial 3", "Promedio"]
    for col, texto in enumerate(encabezados):
        tk.Label(contenedor, text=texto, font=("Arial", 10, "bold"), bg="steelblue",
                 fg="white", width=12).grid(row=0, column=col, padx=2, pady=2, sticky="ew")

    filas = []
    # FOR: la cantidad de estudiantes ya es conocida y fija (la pidió el
    # usuario antes), así que se necesita crear exactamente "cantidad"
    # filas con 3 campos (un parcial cada uno), ni una mas ni una menos.
    for i in range(cantidad):
        tk.Label(contenedor, text=f"Estudiante {i + 1}", bg="lightblue", width=12, anchor="w").grid(
            row=i + 1, column=0, padx=2, pady=2, sticky="w")

        entradas_estudiante = []
        for col in range(1, 4):
            entrada = tk.Entry(contenedor, width=10)
            entrada.grid(row=i + 1, column=col, padx=2, pady=2)
            entradas_estudiante.append(entrada)

        etiqueta_promedio = tk.Label(contenedor, text="-", bg="lightblue", width=12)
        etiqueta_promedio.grid(row=i + 1, column=4, padx=2, pady=2)

        filas.append((entradas_estudiante, etiqueta_promedio))

    def calcular():
        suma_grupo = 0         # acumulador de los promedios de cada estudiante
        contador_validos = 0   # contador de estudiantes con los 3 parciales validos
        aprobados = 0          # contador de aprobados
        reprobados = 0         # contador de reprobados

        # FOR: se recorre una coleccion de tamano ya conocido (una fila
        # por cada estudiante, creada arriba con el otro for).
        for entradas_estudiante, etiqueta_promedio in filas:
            notas_estudiante = []
            valido = True

            for entrada in entradas_estudiante:
                texto = entrada.get().strip()
                if texto == "":
                    valido = False
                    break
                try:
                    nota = float(texto)
                except ValueError:
                    messagebox.showwarning("Dato inválido", f"'{texto}' no es un número válido.")
                    valido = False
                    break
                if nota < 0 or nota > 100:
                    messagebox.showwarning("Dato inválido", f"La nota {nota} está fuera de rango (0-100).")
                    valido = False
                    break
                notas_estudiante.append(nota)

            if not valido:
                etiqueta_promedio.config(text="-")
                continue

            promedio_estudiante = sum(notas_estudiante) / len(notas_estudiante)
            etiqueta_promedio.config(text=f"{promedio_estudiante:.2f}")

            suma_grupo += promedio_estudiante
            contador_validos += 1
            if promedio_estudiante >= NOTA_MINIMA_APROBAR:
                aprobados += 1
            else:
                reprobados += 1

        if contador_validos == 0:
            resultado.config(text="No hay estudiantes con los 3 parciales completos y válidos.")
            return

        promedio_grupo = suma_grupo / contador_validos
        resultado.config(text=(
            f"Estudiantes evaluados: {contador_validos}\n"
            f"Promedio general del grupo: {promedio_grupo:.2f}\n"
            f"Aprobados: {aprobados}   Reprobados: {reprobados}"
        ))

    btnCalcular = ttk.Button(botones, text="Calcular", style="Azul.TButton", command=calcular)
    btnCalcular.grid(column=0, row=0, padx=5)

    btnReiniciar = ttk.Button(botones, text="Reiniciar", style="Azul.TButton", command=iniciar)
    btnReiniciar.grid(column=1, row=0, padx=5)

    btnSalir = ttk.Button(botones, text="Salir", style="Azul.TButton", command=ventana.destroy)
    btnSalir.grid(column=2, row=0, padx=5)


def iniciar():
    cantidad = pedir_cantidad_estudiantes()
    if cantidad is not None:
        pantalla_ingreso(cantidad)


iniciar()
ventana.mainloop()
