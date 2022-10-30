import unittest


class TestAdd(unittest.TestCase):
    def test_addition(self):
        # матрица читается слева направо, сверху вниз
        # матрица следующего вида: [[1, 2, 3]
        #                           [4, 5, 6]
        #                           [7, 8, 9]]
        self.assertEqual(summation([[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # матрица A
                             [[5, 10, 1], [4, 22, 0], [8, 1, 6]]),  # матрица B
                         [[6, 12, 4], [8, 27, 6], [15, 9, 15]])  # результат сложения

        self.assertEqual(summation([[73, 7, 756], [643, 62, 6], [5, 50, 555]],
                             [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
                         [[73, 7, 756], [643, 62, 6], [5, 50, 555]])

        # self.assertEqual(summation([[1, 2], [4, 5], [3, 8]],
        #                      [[1], [1], [1]]),
        #                  'Размеры матриц должны быть одинаковыми')


if __name__ == "__main__":
  unittest.main()