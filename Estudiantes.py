Estudiantes={}
def Ingresar():
    try:
        cantidad=int(input("Ingrese la cantidad de estudiantes que desea agregar al sistema: "))
        i=1
        while i<=cantidad:
            carnetAux=input("Ingrese la carnet que desea ingresar: ")
            if carnetAux in Estudiantes:
                print("El estudiante ya existe")
            else:
                nombreAux=input("Ingrese el nombre del estudiante: ")
                edadAux=int(input("Ingrese la edad del estudiante: "))
                if(edadAux>15) and (edadAux<101):
                    carreraAux=input("Ingrese la carrera del estudiante: ")
                    cantidadCursos=int(input("Ingrese la cantidad de cursos: "))
                    j=1
                    while j<=cantidadCursos:
                        codigoCursoAux=input("Ingrese la codigo curso que desea ingresar: ")
                        if codigoCursoAux in Estudiantes[carreraAux]:
                            print("El codigo ya existe en este estudiante")
                        else:
                            nombreCursoAux=input("Ingrese el nombre del curso: ")
                            notaTarea=float(input("Ingrese la nota tarea: "))
                            notaParcial=float(input("Ingrese la nota parcial: "))
                            notaProyecto=float(input("Ingrese la nota proyecto: "))
                else:
                    print("ERROR: La edad debe ser un numero entero entre 16 y 100")


    except ValueError:
        print("ERROR:")