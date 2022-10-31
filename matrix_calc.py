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
def multiplication_on_number(matrix, number):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] *= number
    return matrix


# Функция обрабатывающая операцию умножения двух матриц
def multiplication(matrix_a, matrix_b):
    matrix_result = [[0 for row in range(len(matrix_a))] for col in range(len(matrix_b[0]))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                matrix_result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_result


# Функция обрабатывающая операцию транспонирования
def transposition(matrix):
    matrix_result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return matrix_result


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


# Функция обрабатывающая ввод матриц и выбор операции  [Проверяет только программную правильность параметров!!!]
def self_input():
    print("Введите задачу - ")
    task = input("Например, Сложение: ")  # По задаче определяем сколько параметров запросим ввести

    if task in binary_dict.keys() or task in unary_dict.keys():
        try:
            rows = int(input("Введите кол-во строк в матрице: "))
            coloumns = int(input("Введите кол-во столбцов в матрице: "))
            first_arg = []
            for i in range(rows):
                first_arg.append([])
            for i in range(rows):
                for j in range(coloumns):
                    first_arg[i].append(int(input(f"Введите элемент A{i + 1}{j + 1} = ")))

            match task:
                case "Сложение" | "Вычитание":
                    second_arg = []
                    for i in range(rows):
                        second_arg.append([])
                    for i in range(rows):
                        for j in range(coloumns):
                            second_arg[i].append(int(input(f"Введите элемент B{i + 1}{j + 1} = ")))
                    return task, first_arg, second_arg
                case "Умножение на число":
                    number = int(input("Введите число на которое нужно умножить матрицу: "))
                    return task, first_arg, number
                case "Перемножение":
                    coloumns = int(input("Введите кол-во столбцов во второй матрице: "))
                    second_arg = []
                    for i in range(rows):
                        second_arg.append([])
                    for i in range(rows):
                        for j in range(coloumns):
                            second_arg[i].append(int(input(f"Введите элемент B{i + 1}{j + 1} = ")))
                    return task, first_arg, second_arg
                case "Транспонирование" | "Нахождение обратной":
                    return task, first_arg
        except ValueError:
            print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
            return self_input()

    print("\n\t\t\tДанная функция еще не реализована\n\t\t\t\tПопробуйте еще раз!")
    return self_input()


def main():
    print("\n\t\t\tДобро пожаловать в Matrix_Calc!!!\n")
    data = self_input()
    if data[0] in binary_dict.keys():
        print(f"ANSWER ==> {binary_dict[data[0]](data[1], data[2])}")
        return 0
    print(f"ANSWER ==> {unary_dict[data[0]](data[1])}")
    return 0


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


        second_arg = input("Матрица или число: ")
        if not second_arg.isnumeric() and task == "Умножение на число":
            print("\n\t\t\tВы ошиблись в параметрах или задаче!\n\t\t\t\tВыполните ввод заново")
            return self_input()
        if second_arg.isnumeric() and not task == "Умножение на число":
            print("\n\t\t\tВы ошиблись в параметрах или задаче!\n\t\t\t\tВыполните ввод заново")
            return self_input()
        if second_arg.isnumeric() and task == "Умножение на число":
            return task, first_arg, float(second_arg)
        second_arg = second_arg.replace('[','').split(']')
        second_arg = [value.split(',') for value in second_arg if value != '']
        second_arg = [[float(cell) for cell in row] for row in second_arg]
        return task, first_arg, second_arg

    # valid_data = self_input()
    # if valid_data[0] in binary_dict.keys():
    #     answer = binary_dict[valid_data[0]](valid_data[1], valid_data[2])
    #     print(f"Ответ ==> {answer}")
    # if valid_data[0] in unary_dict.keys():
    #     answer = unary_dict[valid_data[0]](valid_data[1])
    #     print(f"Ответ ==> {answer}")



        if task in binary_dict.keys(): 
        try: # try ... exept - Отлавливает ввод буквенных значений
            first_arg = input("Матрица в формате [[3,2,1][1,1,1][1,2,3]]: ")
            if first_arg in ["", " "]: # Проверка на пустой ввод
                print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t   Выполните ввод заново")
                return self_input()
            if first_arg.isnumeric(): # Проверка на введение числа
                print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
                return self_input()
            first_arg = first_arg.replace('[','').split(']')
            first_arg = [value.split(',') for value in first_arg if value != '']
            first_arg = [[float(cell) for cell in row] for row in first_arg]

            second_arg = input("Матрица или число: ")
            if second_arg in ["", " "]: # Проверка на пустой ввод
                print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
                return self_input()
            if second_arg.isnumeric():
                valid_data = validator(task, first_arg, float(second_arg))
            else:
                second_arg = second_arg.replace('[','').split(']')
                second_arg = [value.split(',') for value in second_arg if value != '']
                second_arg = [[float(cell) for cell in row] for row in second_arg]
                valid_data = validator(task, first_arg, second_arg)
            return valid_data
        except ValueError:
            print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
            return self_input()

    if task in unary_dict.keys():
        try: # try ... exept - Отлавливает ввод буквенных значений
            arg = input("Матрица в формате [[3,2,1][1,1,1][1,2,3]]: ")
            if arg in ["", " "]: # Проверка на пустой ввод
                print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
                return self_input()
            arg = arg.replace('[','').split(']')
            arg = [value.split(',') for value in arg if value != '']
            arg = [[float(cell) for cell in row] for row in arg]
            return arg
        except ValueError:
            print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
            return self_input()

    print("\n\t\t\tДанная функция еще не реализована\n\t\t\t\tПопробуйте еще раз!")
    return self_input()



    # Функция порверяющая правильность аргументов для заданной задачи
def validator(task, *args, **kwargs):
    if len(args) != 1:
        if task == "Умножение на число" and type(args[1]) == float:
            return task, args[0], args[1]
        if task == "Перемножение" and type(args[1]) == list and len(args[0][0]) == len(args[1]):
            return task, args[0], args[1]
        if task == "Сложение" and type(args[1]) == list:
            return task, args[0], args[1]
        if task == "Вычитание" and type(args[1]) == list:
            return task, args[0], args[1]
    else:
        if task == "Транспонирование" and type(args[0]) == list:
            return task, args[0], args[1]
        if task == "Нахождение обратной матрицы" and type(args[0]) == list:
            return task, args[0], args[1]

    print("\n\t\t\tВы ошиблись в параметрах!\n\t\t\t  Выполните ввод заново")
    return self_input()
'''
