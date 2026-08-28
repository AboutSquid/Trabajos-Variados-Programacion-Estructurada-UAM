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

"""El programa debe:
1.	Solicitar mediante input la cantidad de estudiantes que se desean registrar. 
2.	Para cada estudiante: 
o	Solicitar su nombre. 
o	Solicitar 3 calificaciones. 
o	Calcular su promedio mediante una función. 
o	Indicar si el estudiante: 
	Aprobó: promedio ≥ 70 
	Reprobó: promedio < 70 
3.	Utilizar un ciclo for para ingresar las 3 calificaciones de cada estudiante. 
4.	Utilizar un ciclo while para controlar el registro de estudiantes. 
5.	Crear al menos estas funciones: 
o	Una función que reciba las 3 calificaciones y devuelva el promedio. 
o	Una función que reciba el promedio y determine si aprobó o reprobó. 
6.	Al finalizar, mostrar: 
o	Cantidad de estudiantes aprobados. 
o	Cantidad de estudiantes reprobados. 
o	Promedio general de todos los estudiantes. 
o	El nombre del estudiante con el promedio más alto. 
"""

def ValidarRangos(TextoAMostrar, minimo, maximo, TextoError, TipoDeDato):
    if TipoDeDato == "int":
        while True:
            try:
                nota = int(input(TextoAMostrar))
                if minimo < nota <= maximo:
                    return nota
                else:
                    print(TextoError)
            except ValueError:
                print(TextoError)
    elif TipoDeDato == "float":
        while True:
            try:
                nota = float(input(TextoAMostrar))
                if minimo <= nota <= maximo:
                    return nota
                else:
                    print(TextoError)
            except ValueError:
                print(TextoError)

def ValidarString():
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        if nombre_estudiante and nombre_estudiante.replace(" ", "").isalpha():
            return nombre_estudiante
        else:
            print("Ingrese un nombre válido")

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio
def determinar_resultado(promedio):
    if promedio >= 70:
        return "Aprobó"
    else:
        return "Reprobó"

repetir = "s"
while repetir == "s":
    print("""--------------------------------------------------------
            REGISTRO DE ESTUDIANTES
--------------------------------------------------------""")
    Numero_Estudiantes = ValidarRangos("Ingrese el número de estudiantes que desea registrar: ", 0, 50,
                  "Error. Ingrese un número entero válido mayor a 0. \nEl límite a registrar es 40.", "int")
