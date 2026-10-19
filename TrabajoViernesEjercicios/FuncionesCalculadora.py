# Calculadora de limites de una funcion en base a x, hecha con tkinter
# Calcula el limite de forma numerica (acercandose por la izquierda y por la derecha),
# muestra la tabla de valores y la grafica de la funcion dentro de la misma ventana.

import math
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------------------------------------------------
# Parte del calculo del limite
# ---------------------------------------------------------------

# Funciones y constantes permitidas dentro de la expresion que escribe el usuario
FuncionesPermitidas = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "sqrt": math.sqrt, "raiz": math.sqrt,
    "log": math.log, "ln": math.log, "log10": math.log10,
    "exp": math.exp, "abs": abs, "pow": pow,
    "pi": math.pi, "e": math.e,
}

# Distancias con las que nos vamos acercando al punto
Acercamientos = [1, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

# Diferencia maxima para aceptar que los dos limites laterales son iguales
Tolerancia = 0.001

# A partir de este valor se considera que la funcion se va al infinito
Infinito = 100000

# Colores de la ventana
ColorFondo = "#f0f4f8"
ColorTitulo = "#1f3b57"
ColorBien = "#1b7f3b"
ColorMal = "#b32020"


def EvaluarFuncion(Expresion, ValorX):
    #Evalua la funcion en un valor de x. Devuelve None si en ese punto no existe.
    try:
        Resultado = eval(Expresion, {"__builtins__": {}}, dict(FuncionesPermitidas, x=ValorX))
        Resultado = float(Resultado)
        if math.isnan(Resultado) or math.isinf(Resultado):
            return None
        return Resultado
    except (ZeroDivisionError, ValueError, OverflowError, TypeError, NameError, SyntaxError):
        return None


def LimpiarExpresion(Expresion):
    #Deja la expresion lista para evaluarla.
    return Expresion.replace("^", "**").strip()


def FuncionEsValida(Expresion):
    #Comprueba que la funcion se pueda evaluar en algun valor de x.
    for Prueba in [0.7, 1.3, 2.1, -1.7, 3.5]:
        if EvaluarFuncion(Expresion, Prueba) is not None:
            return True
    return False


def CalcularLimiteLateral(Expresion, Punto, Lado):
    #Calcula el limite acercandose por un lado. Lado -1 es izquierda y 1 es derecha.
    Valores = []
    for Distancia in Acercamientos:
        ValorX = Punto + (Lado * Distancia)
        Valores.append((ValorX, EvaluarFuncion(Expresion, ValorX)))
    return Valores


def LimiteDeLaLista(Valores):
    #Devuelve el ultimo valor calculado de la lista, que es el mas cercano al punto.
    for ValorX, ValorY in reversed(Valores):
        if ValorY is not None:
            return ValorY
    return None


def TextoDelLimite(Valor):
    #Convierte el limite lateral en texto, indicando cuando se va al infinito.
    if Valor is None:
        return "no se pudo calcular"
    if Valor > Infinito:
        return "tiende a + infinito"
    if Valor < -Infinito:
        return "tiende a - infinito"
    return str(round(Valor, 6))


def SonIguales(PrimerValor, SegundoValor):
    #Compara dos limites laterales usando una tolerancia relativa al tamano de los valores.
    Referencia = max(1, abs(PrimerValor), abs(SegundoValor))
    return abs(PrimerValor - SegundoValor) <= (Tolerancia * Referencia)


def AnalizarLimite(Izquierda, Derecha):
    #Compara los dos limites laterales. Devuelve el limite y el texto del resultado.
    LimiteIzquierda = LimiteDeLaLista(Izquierda)
    LimiteDerecha = LimiteDeLaLista(Derecha)

    Mensaje = "Limite por la izquierda:  " + TextoDelLimite(LimiteIzquierda) + "\n"
    Mensaje = Mensaje + "Limite por la derecha:    " + TextoDelLimite(LimiteDerecha) + "\n\n"

    if LimiteIzquierda is None or LimiteDerecha is None:
        Mensaje = Mensaje + "No se pudo calcular alguno de los limites laterales,\nel limite NO existe"
        return None, Mensaje, False

    if abs(LimiteIzquierda) > Infinito and abs(LimiteDerecha) > Infinito:
        if SonIguales(LimiteIzquierda, LimiteDerecha) or (LimiteIzquierda * LimiteDerecha) > 0:
            Mensaje = Mensaje + "La funcion crece sin limite por los dos lados,\nel limite es infinito y NO existe como numero"
            return None, Mensaje, False

    if SonIguales(LimiteIzquierda, LimiteDerecha):
        Limite = (LimiteIzquierda + LimiteDerecha) / 2
        Mensaje = Mensaje + "Los dos limites laterales son iguales, el limite SI existe\n"
        Mensaje = Mensaje + "El limite es aproximadamente: " + str(round(Limite, 6))
        return Limite, Mensaje, True

    Mensaje = Mensaje + "Los limites laterales son diferentes, el limite NO existe"
    return None, Mensaje, False


def PuntosDeLaGrafica(Expresion, Punto):
    #Calcula los puntos que se van a dibujar en la grafica.
    Inicio = Punto - 5
    Final = Punto + 5
    Cantidad = 1000
    Paso = (Final - Inicio) / Cantidad

    ListaX = []
    ListaY = []
    for i in range(Cantidad + 1):
        ValorX = Inicio + (i * Paso)
        ValorY = EvaluarFuncion(Expresion, ValorX)
        ListaX.append(ValorX)
        # Se corta la linea donde la funcion no existe o se dispara demasiado
        if ValorY is None or abs(ValorY) > 1000:
            ListaY.append(float("nan"))
        else:
            ListaY.append(ValorY)
    return ListaX, ListaY


def RangoDelEjeY(ListaY, Limite):
    #Devuelve hasta donde llega el eje Y cuando la funcion se dispara, o None si no hay que recortarlo.
    Valores = sorted(Valor for Valor in ListaY if not math.isnan(Valor))
    if len(Valores) < 20:
        return None

    Menor = Valores[int(len(Valores) * 0.05)]
    Mayor = Valores[int(len(Valores) * 0.95)]
    RangoRecortado = Mayor - Menor
    RangoCompleto = Valores[-1] - Valores[0]

    # Solo se recorta si los valores extremos son mucho mas grandes que el resto
    if RangoRecortado <= 0 or RangoCompleto < (RangoRecortado * 5):
        return None

    if Limite is not None:
        Menor = min(Menor, Limite)
        Mayor = max(Mayor, Limite)

    Margen = (Mayor - Menor) * 0.2
    return Menor - Margen, Mayor + Margen


# ---------------------------------------------------------------
# Parte de la ventana
# ---------------------------------------------------------------

def CrearVentana():
    #Arma toda la ventana y devuelve la ventana con sus componentes.
    Ventana = tk.Tk()
    Ventana.title("Calculadora de limites de una funcion")
    Ventana.geometry("1120x700")
    Ventana.minsize(1120, 700)
    Ventana.configure(background=ColorFondo)

    Componentes = {}

    CrearEncabezado(Ventana, Componentes)

    Cuerpo = tk.Frame(Ventana, background=ColorFondo)
    Cuerpo.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    CrearPanelIzquierdo(Cuerpo, Componentes)
    CrearPanelDerecho(Cuerpo, Componentes)

    return Ventana, Componentes


def CrearEncabezado(Ventana, Componentes):
    #Crea el titulo, las cajas de texto y los botones.
    Encabezado = tk.Frame(Ventana, background=ColorFondo)
    Encabezado.pack(fill="x", padx=15, pady=15)

    Titulo = tk.Label(Encabezado, text="Calculadora de limites",
                      font=("Helvetica", 20, "bold"),
                      background=ColorFondo, foreground=ColorTitulo)
    Titulo.grid(row=0, column=0, columnspan=6, sticky="w")

    tk.Label(Encabezado, text="f(x) =", font=("Helvetica", 13, "bold"),
             background=ColorFondo).grid(row=1, column=0, sticky="w", pady=(10, 0))

    CajaFuncion = tk.Entry(Encabezado, font=("Courier", 14), width=34)
    CajaFuncion.grid(row=1, column=1, sticky="w", padx=(8, 20), pady=(10, 0))
    CajaFuncion.insert(0, "(x**2 - 1)/(x - 1)")

    tk.Label(Encabezado, text="x tiende a:", font=("Helvetica", 13, "bold"),
             background=ColorFondo).grid(row=1, column=2, sticky="w", pady=(10, 0))

    CajaPunto = tk.Entry(Encabezado, font=("Courier", 14), width=10)
    CajaPunto.grid(row=1, column=3, sticky="w", padx=(8, 20), pady=(10, 0))
    CajaPunto.insert(0, "1")

    BotonCalcular = tk.Button(Encabezado, text="Calcular limite",
                              font=("Helvetica", 12, "bold"),
                              command=lambda: Calcular(Componentes))
    BotonCalcular.grid(row=1, column=4, padx=5, pady=(10, 0))

    BotonAyuda = tk.Button(Encabezado, text="Ayuda", font=("Helvetica", 12),
                           command=MostrarAyuda)
    BotonAyuda.grid(row=1, column=5, padx=5, pady=(10, 0))

    Componentes["CajaFuncion"] = CajaFuncion
    Componentes["CajaPunto"] = CajaPunto

    # Con la tecla Enter tambien se calcula el limite
    CajaFuncion.bind("<Return>", lambda Evento: Calcular(Componentes))
    CajaPunto.bind("<Return>", lambda Evento: Calcular(Componentes))


def CrearPanelIzquierdo(Cuerpo, Componentes):
    #Crea la tabla de valores y el cuadro con el resultado.
    Panel = tk.Frame(Cuerpo, background=ColorFondo)
    Panel.pack(side="left", fill="both", padx=(0, 15))

    tk.Label(Panel, text="Tabla de valores", font=("Helvetica", 14, "bold"),
             background=ColorFondo, foreground=ColorTitulo).pack(anchor="w")

    MarcoTabla = tk.Frame(Panel)
    MarcoTabla.pack(fill="both", expand=True, pady=(5, 10))

    Tabla = ttk.Treeview(MarcoTabla, columns=("Lado", "x", "fx"),
                         show="headings", height=17)
    Tabla.heading("Lado", text="Lado")
    Tabla.heading("x", text="x")
    Tabla.heading("fx", text="f(x)")
    Tabla.column("Lado", width=90, anchor="center")
    Tabla.column("x", width=150, anchor="e")
    Tabla.column("fx", width=170, anchor="e")

    Barra = ttk.Scrollbar(MarcoTabla, orient="vertical", command=Tabla.yview)
    Tabla.configure(yscrollcommand=Barra.set)
    Tabla.pack(side="left", fill="both", expand=True)
    Barra.pack(side="right", fill="y")

    # Colores para diferenciar cada lado
    Tabla.tag_configure("izquierda", background="#e8f0fb")
    Tabla.tag_configure("derecha", background="#fdf0e4")

    CuadroResultado = tk.Label(Panel, text="Escribe una funcion y presiona Calcular limite",
                               font=("Courier", 12), background="white",
                               justify="left", anchor="w", relief="groove",
                               width=48, height=7, padx=10, pady=8)
    CuadroResultado.pack(fill="x")

    Componentes["Tabla"] = Tabla
    Componentes["CuadroResultado"] = CuadroResultado


def CrearPanelDerecho(Cuerpo, Componentes):
    #Crea la grafica dentro de la ventana.
    Panel = tk.Frame(Cuerpo, background=ColorFondo)
    Panel.pack(side="left", fill="both", expand=True)

    tk.Label(Panel, text="Grafica de la funcion", font=("Helvetica", 14, "bold"),
             background=ColorFondo, foreground=ColorTitulo).pack(anchor="w")

    Figura = Figure(figsize=(6, 5), dpi=100)
    Dibujo = Figura.add_subplot(111)
    Dibujo.grid(True, linestyle=":", linewidth=0.6)
    Dibujo.set_xlabel("x")
    Dibujo.set_ylabel("f(x)")

    Lienzo = FigureCanvasTkAgg(Figura, master=Panel)
    Lienzo.get_tk_widget().pack(fill="both", expand=True, pady=(5, 0))
    Lienzo.draw()

    Componentes["Figura"] = Figura
    Componentes["Dibujo"] = Dibujo
    Componentes["Lienzo"] = Lienzo


def MostrarError(Componentes, Mensaje):
    #Muestra un mensaje de error en el cuadro de resultado y limpia la tabla.
    Componentes["Tabla"].delete(*Componentes["Tabla"].get_children())
    Componentes["CuadroResultado"].configure(text=Mensaje, foreground=ColorMal)


def Calcular(Componentes):
    #Toma lo que escribio el usuario, calcula el limite y actualiza la ventana.
    Expresion = LimpiarExpresion(Componentes["CajaFuncion"].get())

    if Expresion == "":
        MostrarError(Componentes, "No escribiste ninguna funcion")
        return

    if not FuncionEsValida(Expresion):
        MostrarError(Componentes, "La funcion no se pudo evaluar,\nrevisa que este bien escrita.\n\nPresiona Ayuda para ver los ejemplos.")
        return

    try:
        Punto = float(Componentes["CajaPunto"].get())
    except ValueError:
        MostrarError(Componentes, "El valor al que tiende x\ndebe ser un numero valido")
        return

    Izquierda = CalcularLimiteLateral(Expresion, Punto, -1)
    Derecha = CalcularLimiteLateral(Expresion, Punto, 1)
    Limite, Mensaje, Existe = AnalizarLimite(Izquierda, Derecha)

    LlenarTabla(Componentes["Tabla"], Izquierda, Derecha)
    MostrarResultado(Componentes["CuadroResultado"], Expresion, Punto, Mensaje, Existe)
    DibujarGrafica(Componentes, Expresion, Punto, Limite)


def LlenarTabla(Tabla, Izquierda, Derecha):
    #Llena la tabla con los valores de los dos lados.
    Tabla.delete(*Tabla.get_children())

    for ValorX, ValorY in Izquierda:
        Tabla.insert("", "end", tags=("izquierda",),
                     values=("izquierda", "{:.6f}".format(ValorX), TextoDeLaCelda(ValorY)))

    for ValorX, ValorY in reversed(Derecha):
        Tabla.insert("", "end", tags=("derecha",),
                     values=("derecha", "{:.6f}".format(ValorX), TextoDeLaCelda(ValorY)))


def TextoDeLaCelda(ValorY):
    #Convierte el valor de f(x) en el texto que se ve en la tabla.
    if ValorY is None:
        return "no definido"
    return "{:.6f}".format(ValorY)


def MostrarResultado(CuadroResultado, Expresion, Punto, Mensaje, Existe):
    #Escribe el resultado del limite en el cuadro de la ventana.
    Encabezado = "lim f(x) cuando x -> " + str(Punto) + "\n"
    Encabezado = Encabezado + "f(x) = " + Expresion + "\n\n"
    if Existe:
        Color = ColorBien
    else:
        Color = ColorMal
    CuadroResultado.configure(text=Encabezado + Mensaje, foreground=Color)


def DibujarGrafica(Componentes, Expresion, Punto, Limite):
    #Dibuja la funcion, el punto y el limite dentro de la ventana.
    Dibujo = Componentes["Dibujo"]
    Dibujo.clear()

    ListaX, ListaY = PuntosDeLaGrafica(Expresion, Punto)
    Dibujo.plot(ListaX, ListaY, color="blue", label="f(x) = " + Expresion)
    Dibujo.axhline(0, color="black", linewidth=0.8)
    Dibujo.axvline(0, color="black", linewidth=0.8)
    Dibujo.axvline(Punto, color="gray", linestyle="--", linewidth=1,
                   label="x = " + str(Punto))

    Rango = RangoDelEjeY(ListaY, Limite)
    if Rango is not None:
        Dibujo.set_ylim(Rango[0], Rango[1])

    if Limite is not None:
        Dibujo.axhline(Limite, color="red", linestyle="--", linewidth=1,
                       label="limite = " + str(round(Limite, 4)))
        ValorEnElPunto = EvaluarFuncion(Expresion, Punto)
        if ValorEnElPunto is None:
            # La funcion no existe en el punto, se marca con un circulo vacio
            Dibujo.plot(Punto, Limite, marker="o", markersize=9,
                        markerfacecolor="white", markeredgecolor="red")
        else:
            Dibujo.plot(Punto, ValorEnElPunto, marker="o", markersize=8, color="red")

    Dibujo.set_title("Limite en x = " + str(Punto))
    Dibujo.set_xlabel("x")
    Dibujo.set_ylabel("f(x)")
    Dibujo.grid(True, linestyle=":", linewidth=0.6)
    Dibujo.legend(fontsize=9)
    Componentes["Figura"].tight_layout()
    Componentes["Lienzo"].draw()


def MostrarAyuda():
    #Abre una ventana con la explicacion de como escribir la funcion.
    TextoAyuda = """Operaciones:  +   -   *   /   **  (o ^ para la potencia)

Funciones:    sqrt(x) o raiz(x), ln(x), log10(x), exp(x), abs(x)
              sin(x), cos(x), tan(x), asin(x), acos(x), atan(x)
              sinh(x), cosh(x), tanh(x)

Constantes:   pi, e

Ejemplos:
    (x**2 - 1)/(x - 1)        con x tiende a 1
    sin(x)/x                  con x tiende a 0
    (sqrt(x) - 2)/(x - 4)     con x tiende a 4
    1/x                       con x tiende a 0  (no existe)

El limite se calcula de forma numerica, acercandose al punto
por la izquierda y por la derecha. Si los dos lados llegan al
mismo valor, entonces el limite existe."""

    VentanaAyuda = tk.Toplevel()
    VentanaAyuda.title("Como escribir la funcion")
    VentanaAyuda.configure(background=ColorFondo)

    tk.Label(VentanaAyuda, text="Como escribir la funcion",
             font=("Helvetica", 15, "bold"),
             background=ColorFondo, foreground=ColorTitulo).pack(padx=20, pady=(15, 5))

    tk.Label(VentanaAyuda, text=TextoAyuda, font=("Courier", 12),
             background=ColorFondo, justify="left").pack(padx=20, pady=(0, 10))

    tk.Button(VentanaAyuda, text="Cerrar", font=("Helvetica", 12),
              command=VentanaAyuda.destroy).pack(pady=(0, 15))


def CalculadoraDeLimites():
    #Enciende la calculadora.
    Ventana, Componentes = CrearVentana()
    Calcular(Componentes)
    Ventana.mainloop()


if __name__ == "__main__":
    CalculadoraDeLimites()
