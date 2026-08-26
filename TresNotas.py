ListaNotas = []
for i in range(3):
    InputNotas = 0
    while True:
        try:
            InputNotas = float(input(f"Introduce la nota numero {i+1}"))
            break
        except ValueError:
            print("Introduce un numero valido")
        finally:
            print("mim")
    while True:
        if InputNotas < 0:
            print("Introduce un numero mayor que 0")
            InputNotas = int(input(f"Introduce la nota numero {i + 1}"))
        else:
            break
    ListaNotas.append(InputNotas)
promedio = 0
for i in range(3):
    promedio += ListaNotas[i]

promedio /= 3
print("El promedio es de:",promedio)