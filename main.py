from validaciones import readStudent
from validaciones import chooseOp
from validaciones import readSubject
from validaciones import readGrade

from calculos import calcAverage
from calculos import detStatus
from calculos import detPerf

from resultados import getRecommendation
from resultados import showResults


def main():

    while True:

        student = readStudent()

        subjects = []
        grades = []

        while True:

            option = chooseOp()

            if option == 1:

                subject = readSubject()
                grade = readGrade()

                subjects.append(subject)
                grades.append(grade)

                print("Nota registrada correctamente.")

            elif option == 2:

                if len(grades) > 0:

                    average = calcAverage(grades)
                    status = detStatus(average)
                    performance = detPerf(average)
                    recommendation = getRecommendation(performance)

                    showResults(
                        student, subjects, grades, average, status, performance, recommendation
                    )

                else:

                    print("\nDebe registrar al menos una calificación.")

            elif option == 3:

                if len(grades) > 0:

                    average = calcAverage(grades)
                    status = detStatus(average)
                    performance = detPerf(average)
                    recommendation = getRecommendation(performance)

                    showResults(student, subjects, grades, average, status, performance, recommendation)

                    break

                else:

                    print("\nDebe registrar al menos una calificación.")

            elif option == 4:

                print("\nGracias por utilizar el programa.")
                return


main()