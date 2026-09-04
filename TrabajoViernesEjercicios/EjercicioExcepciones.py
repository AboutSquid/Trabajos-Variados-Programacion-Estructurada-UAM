def MenorQue(nummenor, comparacion, texto,TipoDato):
    while True:
        if TipoDato == "int":
            if comparacion < nummenor:
                print("Introduce un numero mayor que ", nummenor)
                comparacion = int(input(texto))

            else:
                return comparacion
                break
        if TipoDato == "float":
            if comparacion < nummenor:
                print("Introduce un numero mayor que ", nummenor)
                comparacion = float(input(texto))

            else:
                return comparacion

def Ejercicio6():
    #Solicita el precio de un producto y conviértelo a float. Controla ValueError y muestra un mensaje adecuado cuando la entrada no sea numérica.
    print("""
    ------------
    Ejercicio 6
    ------------""")
    while True:
        try:
            precioProducto = float(input("Introduce el precio del producto: "))
            precioProducto = MenorQue(0, precioProducto,"Introduce el precio del producto:", "float")
            break
        except ValueError:
            print("Introduce un precio valido")

    print("El precio del producto es: ", precioProducto)


def Ejercicio7():
    # Solicita la cantidad de unidades que una persona desea comprar. Controla entradas que no puedan convertirse a entero.
    CantidadProducto = 0
    print("""
    ------------
    Ejercicio 7
    ------------""")
    while True:
        try:
            CantidadProducto = int(input("Introduce la Cantidad de producto a comprar: "))
            CantidadProducto = MenorQue(0, CantidadProducto, "Introduce la Cantidad de producto a comprar: ", "int")
            break
        except ValueError:
            print("Introduce una cantidad valida")


    print("La cantidad a comprar es: ", CantidadProducto)

def Ejercicio8():
    #Solicita una calificación numérica. Controla ValueError y, si la conversión funciona, indica si la calificación está entre 0 y 100.
    print("""
    ------------
    Ejercicio 8
    ------------""")
    while True:
        try:
            Nota = float(input("Introduce la calificacion: "))
            while True:
                if Nota < 0 or Nota > 100:
                    print("Introduce una calificacion de 0 a 100")
                    Nota = float(input("Introduce la calificacion: "))
                else:
                    break
            break
        except ValueError:
            print("Introduce una calificacion valida")

    print("La calificacion es de: ", Nota)

def Ejercicio9():
    #Solicita la edad. Controla ValueError y evita que el programa continúe con una edad que no sea válida.
    print("""
    ------------
    Ejercicio 9
    ------------""")
    while True:
        try:
            Edad = int(input("Introduce la edad: "))
            while True:
                if Edad < 0:
                    print("Introduce una edad la introducida es entero pero esta fuera del rango permitido edad < 0")
                    Edad = int(input("Introduce la edad: "))
                else:
                    break
            break
        except ValueError:
            print("Introduce una edad valida, la edad introducida no es un entero")

    print("La edad introducida es de: ", Edad)





