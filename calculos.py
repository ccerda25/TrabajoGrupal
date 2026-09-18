minPass = 70


def calcAverage(grades):

    if len(grades) == 0:
        return 0

    total = 0

    for grade in grades:
        total = total + grade

    average = total / len(grades)

    return average


def detStatus(average):

    if average >= minPass:
        return "Aprobado"

    else:
        return "Reprobado"


def detPerf(average):

    if average <= 69:
        return "Aprendizaje inicial"

    elif average <= 79:
        return "Aprendizaje fundamental"

    elif average <= 89:
        return "Aprendizaje satisfactorio"

    else:
        return "Aprendizaje avanzado"