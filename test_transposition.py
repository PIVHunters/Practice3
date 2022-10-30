import unittest


class TestTransposition(unittest.TestCase):
    def test_transposition(self):
        # матрица читается слева направо, сверху вниз
        # матрица следующего вида: [[1, 2, 3]
        #                           [4, 5, 6]
        #                           [7, 8, 9]]
        self.assertEqual(transposition([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])  # результат транспонирования

        self.assertEqual(transposition([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
                         [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        self.assertEqual(transposition([[1, 2], [4, 5], [3, 8]]),
                         [[1, 4, 3], [2, 5, 8]])


if __name__ == "__main__":
  unittest.main()
