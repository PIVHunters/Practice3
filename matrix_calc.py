def summation(matrix_a, matrix_b):
    pass


def multiplication_on_number(number, matirx):
    pass


def multiplication(matrix_a, matrix_b):
    pass


task_dict = {"Сложение": summation,
             "Умножение на число": multiplication_on_number,
             "Умножение матриц": multiplication}


def self_input():
    task_key = input("Введите интересующую вас операцию: ")



def main():
    print("\n\t\t\tДобро пожаловать в Matrix_Calc!!!\n")
    self_input()


if __name__ == "__main__":
    main()