import unittest


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # матрица читается слева направо, сверху вниз
        # матрица следующего вида: [[1, 2, 3]
        #                           [4, 5, 6]
        #                           [7, 8, 9]]
        self.assertEqual(multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # матрица A
                                        [[2, 3, 4], [5, 6, 7], [8, 9, 1]]),  # матрица B
                                          [[36, 42, 21], [81, 96, 57], [126, 150, 93]])  # результат умножения

        self.assertEqual(multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
                         [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        self.assertEqual(multiplication([[2, 3], [4, 5], [6, 7]],  # разная размерность
                                  [[1, 2, 3], [4, 5, 6]]),
                         [[14, 19, 24], [24, 33, 42], [34, 47, 60]])

        # self.assertEqual(Multiply([[1, 2], [4, 5], [3, 8]],  # несоответствие кол-ву столбцов и строк
        #                           [[1], [1], [1]]),
        #                  'Количество столбцов первой матрицы должно равняться количеству строк второй')


if __name__ == "__main__":
  unittest.main()
