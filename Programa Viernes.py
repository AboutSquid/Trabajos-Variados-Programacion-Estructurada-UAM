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

def ValidarString(num, tipovalid):
    #tipovalid solo existe para validar nombres y validar la s y n
    if tipovalid == 1:
        while True:
            nombre_estudiante = input(f"Ingrese el nombre del {num+1}° estudiante: ")
            if nombre_estudiante and nombre_estudiante.replace(" ", "").isalpha():
                return nombre_estudiante
            else:
                print("Ingrese un nombre válido")
    elif tipovalid == 2:
        while True:
            repetir = input("\n¿Desea registrar otro grupo de estudiantes o quiere finalizar el programa?"
                            "\nEscriba 's' para reiniciar o escriba 'n' para finalizar.\n")
            if repetir.lower() == "n" or repetir.lower() == "s":
                return repetir
            else:
                print("Por favor, limite su respuesta a 's' o 'n'.")


def calcular_promedio(notas):
    promedio = notas / 3
    return promedio
def determinar_resultado(promedio, nombre):
    if promedio >= 70:
        print(f"--------------------------------------------------"
              f"\n¡Felicidades {nombre}, has aprobado!"
              f"\nPromedio final: {promedio:.2f}"
              f"\n--------------------------------------------------")
        return 1
    else:
        print(f"--------------------------------------------------"
              f"\n¡Lo sentimos, {nombre}, has reprobado!"
              f"\nPromedio final: {promedio:.2f}"
              f"\n--------------------------------------------------")
        return 0


def Obtener_Mayor_Promedio(promedio_mayor, promedio, nombre, nombre_mayor):
    if promedio > promedio_mayor:
        promedio_mayor = promedio
        nombre_mayor = nombre

    return promedio_mayor, nombre_mayor



repetir = "s"
while repetir == "s":
    print("""--------------------------------------------------------
            REGISTRO DE ESTUDIANTES
--------------------------------------------------------""")
    Numero_Estudiantes = ValidarRangos("Ingrese el número de estudiantes que desea registrar: ", 0, 40,
                  "Error. Ingrese un número entero válido mayor a 0. \nEl límite a registrar es 40.", "int")
    contador = 0
    aprobados = 0
    reprobados = 0
    promedios = 0 #promedio general de estudiantes
    promedio_mayor = -1
    MejorEstudiante = "el que lo esté leyendo"
    while contador < Numero_Estudiantes:
        Nombre_Estudiantes = ValidarString(contador,1)
        notas = 0 #variable para calcular el promedio, ya que está restringido usar listas
        for i in range(3):
            nota = ValidarRangos(f"Ingrese la {i+1}° calificación: ", 0, 100,
                            "Error. Ingrese un número entre 0 y 100.", "float")
            notas += nota
        promedio = calcular_promedio(notas)
        promedios += promedio
        promedio_mayor, MejorEstudiante = Obtener_Mayor_Promedio(promedio_mayor, promedio, Nombre_Estudiantes, MejorEstudiante)
        cant = determinar_resultado(promedio, Nombre_Estudiantes)
        if cant == 1:
            aprobados += 1
        else:
            reprobados += 1
        contador += 1

    print(f"\n\n--------------------------------------------------------"
          f"\n                      REPORTE FINAL"
          f"\n--------------------------------------------------------"
          f"\nEstudiantes Aprobados: {aprobados}"
          f"\nEstudiantes Reprobados: {reprobados}"
          f"\nPromedio General de Todos los Estudiantes: {promedios/Numero_Estudiantes:.2f}"
          f"\nMejor Estudiante: {MejorEstudiante}"
          f"\nPromedio de {MejorEstudiante}: {promedio_mayor:.2f}")

    repetir = ValidarString(0, 2)

