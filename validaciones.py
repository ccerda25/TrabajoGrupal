def readStudent():
    while True:
        try:
            student = input("Ingrese el nombre del estudiante: ")

            if student == "":
                print("El nombre no puede estar vacío.")
            else:
                return student

        except Exception:
            print("Ocurrió un error al ingresar el nombre.")


def chooseOp():
    print("\nREGISTRO DE ESTUDIANTES")
    print("1. Registrar asignatura y nota")
    print("2. Ver resultados")
    print("3. Registrar otro estudiante")
    print("4. Salir")

    while True:
        try:
            option = int(input("Seleccione una opción: "))

            if option >= 1 and option <= 4:
                return option
            else:
                print("Ingrese una opción entre 1 y 4.")

        except ValueError:
            print("Ingrese un valor numérico.")


def readSubject():
    while True:
        try:
            subject = input("Ingrese el nombre de la asignatura: ")

            if subject == "":
                print("El nombre de la asignatura no puede estar vacío.")
            else:
                return subject

        except Exception:
            print("Ocurrió un error al ingresar la asignatura.")


def readGrade():
    while True:
        try:
            grade = float(input("Ingrese su calificación: "))

            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("La calificación debe ser entre 0 y 100.")

        except ValueError:
            print("Debe ingresar un valor numérico.")