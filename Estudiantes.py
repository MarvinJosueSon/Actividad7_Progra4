Estudiantes={}
Cursos={}
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
                        if codigoCursoAux in Estudiantes[carreraAux][Cursos]:
                            print("El codigo ya existe en este estudiante")
                        else:
                            nombreCursoAux=input("Ingrese el nombre del curso: ")
                            notaTarea=float(input("Ingrese la nota tarea: "))
                            notaParcial=float(input("Ingrese la nota parcial: "))
                            notaProyecto=float(input("Ingrese la nota proyecto: "))
                            if ((notaProyecto>=0) and (notaProyecto<=100)) and ((notaTarea>=0) and (notaTarea<=100)) and ((notaParcial>=0) and (notaParcial<=100)):
                                Cursos[codigoCursoAux]={
                                    "nombreCurso": nombreCursoAux,
                                    "notaTarea": notaTarea,
                                    "notaParcial": notaParcial,
                                    "notaProyecto": notaProyecto
                                }
                                Estudiantes[carnetAux]={
                                    "nombre": nombreAux,
                                    "edad": edadAux,
                                    "carrera": carreraAux,
                                    "cursos": codigoCursoAux
                                }
                                j=j+1
                            else:
                                print("ERROR: TODAS LAS NOTAS DEBEN ESTAR EN UN RANGO DE 0 a 100")
                    i=i+1

                else:
                    print("ERROR: La edad debe ser un numero entero entre 16 y 100")


    except ValueError:
        print("ERROR:")

    while True:
        print("==MENU==")