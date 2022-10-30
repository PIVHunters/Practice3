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


# Функция обрабатывающая операцию транспонирования
def transposition(matrix):
    pass


# Функция обрабатывающая операцию умножения двух матриц
def inverting(matrix):
    pass


# Словарь бинарных операций
binary_dict = {"Сложение": summation,
               "Вычитание": subtraction,
               "Умножение на число": multiplication_on_number,
               "Перемножение": multiplication}

# Словарь унарных операций
unary_dict = {"Транспонирование": transposition,
              "Нахождение обратной": inverting}


# Функция обрабатывающая ввод матриц и выбор операции (Поработать над защитой)
def self_input():
    print("Введите задачу - ")
    task = input("Например, Сложение: ")

    if task in binary_dict.keys():
        first_arg = input("Матрица в формате [[3,2,1][1,1,1][1,2,3]]: ")
        first_arg = first_arg.replace('[', '').split(']')
        first_arg = [value.split(',') for value in first_arg if value != '']
        first_arg = [[float(cell) for cell in row] for row in first_arg]

        second_arg = input("Матрица или число: ")
        if not second_arg.isnumeric() and task == "Умножение на число":
            print("\n\t\t\tВы ошиблись в параметрах или задаче!\n\t\t\tВыполните ввод заново")
            return self_input()
        if second_arg.isnumeric() and task == "Умножение на число":
            return task, first_arg, float(second_arg)
        second_arg = second_arg.replace('[', '').split(']')
        second_arg = [value.split(',') for value in second_arg if value != '']
        second_arg = [[float(cell) for cell in row] for row in second_arg]
        return task, first_arg, second_arg

    if task in unary_dict.keys():
        arg = input("Матрица в формате [[3,2,1][1,1,1][1,2,3]]: ")
        arg = arg.replace('[', '').split(']')
        arg = [value.split(',') for value in arg if value != '']
        arg = [[float(cell) for cell in row] for row in arg]
        return task, arg

    print("\n\t\t\tДанная функция еще не реализована\n\t\t\t\tПопробуйте еще раз!")
    return self_input()


def main():
    print("\n\t\t\tДобро пожаловать в Matrix_Calc!!!\n")
    print(self_input())


if __name__ == "__main__":
    main()

''' 
    Кладбище кода 

    arg_first = input("Матрица в формате [[3,2,1][1,1,1][1,2,3]]: ")
    arg_first = arg_first.replace("[","").split("]")


    arg_second = input("Матрица, число или '-': ")
    if (arg_second != '-') and not (type(arg_second) == int or type(arg_second) == float):
        arg_second = arg_second.replace("[","").replace("]","")
        arg_second = [int(cell) for cell in arg_second.split(",")]
    return task, arg_first, 

    for row in first_arg:
    for cell in row:
    cell = int(cell)
'''
