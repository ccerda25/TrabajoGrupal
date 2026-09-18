def getRecommendation(performance):

    if performance == "Aprendizaje inicial":
        return "Debe reforzar los contenidos y practicar más."

    elif performance == "Aprendizaje fundamental":
        return "Debe continuar practicando para mejorar su rendimiento."

    elif performance == "Aprendizaje satisfactorio":
        return "Buen rendimiento. Puede seguir fortaleciendo sus conocimientos."

    else:
        return "Excelente rendimiento. Continúe manteniendo este nivel."


def showGrades(subjects, grades):

    print("\nCALIFICACIONES")

    for i in range(len(subjects)):
        print(subjects[i], "-", grades[i])


def showResults(student, subjects, grades, average, status, performance, recommendation):

    print("\nRESULTADOS DEL ESTUDIANTE")

    print("Estudiante:", student)

    showGrades(subjects, grades)

    print("\nPromedio:", round(average, 2))
    print("Estado académico:", status)
    print("Nivel de rendimiento:", performance)
    print("Recomendación:", recommendation)