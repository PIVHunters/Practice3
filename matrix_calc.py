# Функция обрабатывающая операцию сложения двух матриц
def summation(matrix_a, matrix_b):
    for i in range(0, len(matrix_a)):
        for j in range(0, len(matrix_a[i])):
            matrix_a[i][j] += matrix_b[i][j]
    return matrix_a


# Функция обрабатывающая операцию вычитание двух матриц
def subtraction(matrix_a, matrix_b):
    for i in range(0, len(matrix_a)):
        for j in range(0, len(matrix_a[i])):
            matrix_a[i][j] -= matrix_b[i][j]
    return matrix_a


# Функция обрабатывающая операцию умножения матрицы на число
def multiplication_on_number(number, matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] *= number
    return matrix


# Функция обрабатывающая операцию умножения двух матриц
def multiplication(matrix_a, matrix_b):
    pass


# Словарь операций
task_dict = {"Сложение": summation,
             "Вычитание": subtraction,
             "Умножение на число": multiplication_on_number,
             "Умножение матриц": multiplication}


# Функция обрабатывающая ввод матриц и выбор операции
def self_input():
    task_key = input("Введите интересующую вас операцию: ")
    pass


def main():
    print("\n\t\t\tДобро пожаловать в Matrix_Calc!!!\n")
    print(multiplication_on_number(5, [[3, 2, 1], [1, 2, 3]]))


if __name__ == "__main__":
    main()