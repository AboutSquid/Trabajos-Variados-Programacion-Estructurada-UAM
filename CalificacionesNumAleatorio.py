"""Escriba un programa que genere números aleatorios (entre 0 y 100) utilizando:
a) while
b) for
Calcule el promedio y el tiempo CPU utilizado en cada caso.
La salida debe ser el tiempo, cantidad de notas y promedio."""
import random
import time
import os #para obtener el ID del proceso
import psutil #para la cpu y la ram

proceso = psutil.Process(os.getpid()) #obtiene el ID del proceso
List_Nombres = ["Juan","Ernesto","Pedro","Matias","Mateo", "Petter", "Malcolm", "Jean", "Pierre", "Luc", "Antoine", "Marc", "Mateo", "Lucas", "Gabriel", "Louis", "Jules", "Hugo", "Arthur", "Adam", "Raphaël", "Léo", "Liam", "Ethan", "Paul", "Nathan", "Thomas", "Noah", "Théo", "Victor", "Martin", "Mathis", "Axel", "Maxime", "Enzo", "Clément", "Alexandre", "Samuel", "Simon", "Julien", "Nicolas", "Romain", "Benjamin", "Quentin", "Alexis", "Anthony", "Florian", "Guillaume", "Kevin", "Valentin", "Jeremy", "Dylan", "David", "Christopher", "Carlos", "Javier", "Alejandro", "Daniel", "Manuel", "Francisco", "Juan", "José", "Antonio", "Miguel", "Ángel", "Diego", "Pablo", "Pedro", "Fernando", "Jorge", "Luis", "Alberto", "Álvaro", "Adrián", "Raúl", "Enrique", "Ramón", "Vicente", "Iván", "Rubén", "Óscar", "Andrés", "Joaquín", "Santiago", "Sebastián", "Matías", "Felipe", "Gonzalo", "Rodrigo", "Tomás", "Ignacio", "Maximiliano", "Agustín", "Emmanuel", "Leonardo", "Emiliano", "Oliver", "Jack", "Harry", "Jacob", "Charlie", "George", "James", "William", "Mason", "Michael", "Henry", "Jackson", "Aidan", "Matthew", "Joseph", "Carter", "Owen", "Wyatt", "John", "Luke", "Jayden", "Grayson", "Levi", "Isaac", "Julian", "Jaxon", "Lincoln", "Joshua", "Andrew", "Theodore", "Caleb", "Ryan", "Asher", "Leo", "Isaiah", "Charles", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli", "Ezra", "Aaron", "Landon", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton", "Cameron", "Carson", "Robert", "Angel", "Maverick", "Dominic", "Jaxson", "Greyson", "Ian", "Austin", "Jordan", "Cooper", "Brayden", "Roman", "Evan", "Ezekiel", "Xavier", "Jace", "Jameson", "Everett", "Kayden", "Miles", "Sawyer", "Jason", "Declan", "Weston", "Micah", "Ayden", "Wesley", "Luca", "Vincent", "Damian", "Zachary", "Silas", "Gavin", "Kai", "Kaiden", "Harrison", "Waylon", "Brody", "Tristan", "Parker", "Jasper", "Rowan", "Cole", "Amari", "Nathaniel", "Dean", "Zion", "Bennett", "Felix", "Elliott", "Graham", "Alan", "Erick", "Walter", "Frank", "Hector"]
List_Apellidos = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Morales", "Suárez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Iglesias", "Nuñez", "Medina", "Garrido", "Santos", "Castillo", "Cortés", "Lozano", "Guerrero", "Cano", "Prieto", "Méndez", "Cruz", "Calvo", "Gallego", "Vidal", "León", "Herrera", "Márquez", "Peña", "Cabrera", "Flores", "Campos", "Vega", "Fuentes", "Carrasco", "Díez", "Caballero", "Reyes", "Nieto", "Aguilar", "Pascual", "Santana", "Herrero", "Montero", "Lorenzo", "Hidalgo", "Giménez", "Ibáñez", "Ferrer", "Duran", "Vicente", "Benítez", "Santiago", "Arias", "Mora", "Carmona", "Vargas", "Valero", "Román", "Pastor", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Bernard", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro"]
while True:
    print("""Que deseas utilizar:
    1. For
    2. While
    3. Salir""")
    while True:
       try:
           Cmd = int(input(f"Introduce una opcion:"))
           break
       except ValueError:
            print("Ingresa el numero de lo que deseas.")
    CantidadEstudiantes = 0
    if Cmd == 1:
        print("Se selecciono el for")
        while True:
            try:
                 CantidadEstudiantes = int(input(f"Introduce el numero de estudiantes:"))
                 break
            except ValueError:
                print("Ingresa un numero valido de estudiantes.")
        EstudianteAprobados = 0
        ramAntesdelFor = proceso.memory_info().rss / (1024 * 1024)  # mide en MB la RAM que ocupa antes del ciclo for
        proceso.cpu_percent()  #se marca el punto de referencia para guardar la cpu
        cpuTiempoInicial = proceso.cpu_times() #se marca el punto de referencia para el tiempo cpu
        tiempoInicio = time.time()  # inicia el contador
        for i in range(CantidadEstudiantes):
            Notas = []
            numNombre = random.randint(0, len(List_Nombres)-1)
            numApellido = random.randint(0, len(List_Apellidos)-1)
            for j in range(3):
                NotaRandom = random.randint(0, 100)
                Notas.append(NotaRandom)

            promedio = (Notas[0]+Notas[1]+Notas[2])/3
            print(f"{List_Nombres[numNombre]} {List_Apellidos[numApellido]}: {Notas[0]}, {Notas[1]}, {Notas[2]}, Promedio: { promedio:.2f}")
            if promedio >70:
                EstudianteAprobados += 1
        tiempoFin = time.time() #detiene contador
        cpu = proceso.cpu_percent() #se detiene el intervalo y se devuelve cuanto fue usado
        cpuTiempoFinal = proceso.cpu_times() #se detiene el intervalo y devuelve el tiempo cpu
        #Como devuelven tanto user como system, se crea una variable que contenga todo eso
        timecpu = (cpuTiempoFinal.user + cpuTiempoFinal.system) - (cpuTiempoInicial.user + cpuTiempoInicial.system)
        ramDespuesdelFor = proceso.memory_info().rss / (1024 * 1024) #mide en MB la RAM después del ciclo for
        print("-----------------------------------------------------------------------"
              f"\nCon el ciclo for ha durado {tiempoFin-tiempoInicio:.6f} segundos"
              f"\nRAM usada antes del ciclo for: {(round(ramAntesdelFor,2))} MB"
              f"\nRAM usada después del ciclo for: {round(ramDespuesdelFor,2)} MB."
              f"\nVariación de RAM durante el ciclo for: {ramDespuesdelFor-ramAntesdelFor:.6f} MB."
              f"\nUso de CPU durante el ciclo for: {cpu}%"
              f"\nTiempo CPU: {timecpu:.6f} segundos"
              f"\nEstudiantes Aprobados: {EstudianteAprobados}"
              f"\nEstudiantes Reprobados: {CantidadEstudiantes - EstudianteAprobados}"
              "\n-----------------------------------------------------------------------")

    elif Cmd == 2:
        print("Se selecciono el while")
        while True:
            try:
                 CantidadEstudiantes = int(input(f"Introduce el numero de estudiantes:"))
                 break
            except ValueError:
                print("Ingresa un numero valido de estudiantes.")
        EstudianteAprobados = 0
        p =0
        ramAntesdelWhile = proceso.memory_info().rss / (1024 * 1024)  # mide en MB la RAM que ocupa antes del ciclo while
        proceso.cpu_percent()  #se marca el punto de referencia para guardar la cpu
        cpuTiempoInicial = proceso.cpu_times() #se marca el punto de referencia para el tiempo cpu
        tiempoInicio = time.time()  # inicia el contador
        while p < CantidadEstudiantes:
            Notas = []
            numNombre = random.randint(0, len(List_Nombres)-1)
            numApellido = random.randint(0, len(List_Apellidos)-1)
            m =0
            while m < 3:
                NotaRandom = random.randint(0, 100)
                Notas.append(NotaRandom)
                m+= 1

            print(f"{List_Nombres[numNombre]} {List_Apellidos[numApellido]}: {Notas[0]}, {Notas[1]}, {Notas[2]}, Promedio: {(Notas[0]+Notas[1]+Notas[2])/3 :.2f}")
            p +=1
        tiempoFin = time.time()  # detiene contador
        cpu = proceso.cpu_percent() #se detiene el intervalo y se devuelve cuanto fue usado
        cpuTiempoFinal = proceso.cpu_times() #se detiene el intervalo y devuelve el tiempo cpu
        #Como devuelven tanto user como system, se crea una variable que contenga todo eso
        timecpu = (cpuTiempoFinal.user + cpuTiempoFinal.system) - (cpuTiempoInicial.user + cpuTiempoInicial.system)
        ramDespuesdelWhile = proceso.memory_info().rss / (1024 * 1024) #mide en MB la RAM después del ciclo while
        print("-----------------------------------------------------------------------"
              f"\nCon el ciclo while ha durado {tiempoFin - tiempoInicio:.6f} segundos"
              f"\nRAM usada antes del ciclo while: {(round(ramAntesdelWhile, 2))} MB"
              f"\nRAM usada después del ciclo while: {round(ramDespuesdelWhile, 2)} MB."
              f"\nVariación de RAM durante el ciclo while: {ramDespuesdelWhile - ramAntesdelWhile:.6f} MB."
              f"\nUso de CPU durante el ciclo while: {cpu}%"
              f"\nTiempo CPU: {timecpu:.6f} segundos"
              "\n-----------------------------------------------------------------------")

    elif Cmd == 3:
        print("Adios")
        break
