Estudiantes = {}

def Ingresar():
    try:
        cantidad = int(input("Ingrese la cantidad de estudiantes que desea agregar al sistema: "))
        i = 1
        while i <= cantidad:
            print(f"\n== Ingreso estudiante #{i} ==")
            carnetAux = input("Ingrese el carnet que desea ingresar: ")
            if carnetAux in Estudiantes:
                print("ERROR: El estudiante ya existe")
            else:
                nombreAux = input("Ingrese el nombre del estudiante: ")
                edadAux = int(input("Ingrese la edad del estudiante: "))
                if 15 < edadAux < 101:
                    carreraAux = input("Ingrese la carrera del estudiante: ")
                    cantidadCursos = int(input("Ingrese la cantidad de cursos: "))
                    cursos = {}
                    j = 1
                    while j <= cantidadCursos:
                        print(f"\nIngreso curso #{j} del estudiante #{i}")
                        codigoCursoAux = input("Ingrese el código del curso: ")
                        if codigoCursoAux in Estudiantes[carnetAux][codigoCursoAux]:
                            nombreCursoAux = input("Ingrese el nombre del curso: ")
                            notaTarea = float(input("Ingrese la nota de tarea: "))
                            notaParcial = float(input("Ingrese la nota del parcial: "))
                            notaProyecto = float(input("Ingrese la nota del proyecto: "))

                            if (notaProyecto>=0 and notaProyecto<=100) and (notaTarea>=0 and notaTarea<=100) and (notaParcial>=0 and notaParcial<=100):
                                cursos[codigoCursoAux] = {
                                    "nombre": nombreCursoAux,
                                    "notaTarea": notaTarea,
                                    "notaParcial": notaParcial,
                                    "notaProyecto": notaProyecto
                                }
                                j = j+ 1
                            else:
                                print("ERROR: Todas las notas deben estar entre 0 y 100")

                    Estudiantes[carnetAux] = {
                        "nombre": nombreAux,
                        "edad": edadAux,
                        "carrera": carreraAux,
                        "cursos": cursos
                    }
                    i += 1
                else:
                    print("ERROR: La edad debe ser un número entre 16 y 100")

    except ValueError:
        print("ERROR: Ingrese valores válidos")

def verCursos():
    for carnet, datos in Estudiantes.items():
        print(f"\n== Carnet: {carnet} ==")
        print(f"Nombre del estudiante: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print("Cursos:")
        for codigo, curso in datos['cursos'].items():
            print(f"Código: {codigo}")
            print(f"Nombre: {curso['nombre']}")
            print(f"Nota tarea: {curso['notaTarea']}")
            print(f"Nota parcial: {curso['notaParcial']}")
            print(f"Nota proyecto: {curso['notaProyecto']}")



while True:
    print("\n== MENÚ ==")
    print("1. Ingresar estudiante")
    print("2. Mostrar todos los estudiantes y cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")
    opcion = input("Ingrese la opción: ")

    match opcion:
        case "1":
            Ingresar()
        case "2":
            verCursos()
        case "4":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida")
