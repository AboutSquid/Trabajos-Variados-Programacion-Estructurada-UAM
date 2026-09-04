while True:
    print("""
    --------------------
    1. Ir a calculadora
    2.Salir
    --------------------""")
    operacion = input("Ingrese operacion: ")
    if operacion == "1":
        operacion = input("Calculadora: ")
        resultado = eval(operacion)
        print("Resultado: ", resultado)
    elif operacion == "2":
        print("Saliendo...")
        break
