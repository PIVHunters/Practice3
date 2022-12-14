import unittest


class TestDiff(unittest.TestCase):
    def test_difference(self):
        # матрица читается слева направо, сверху вниз
        # матрица следующего вида: [[1, 2, 3]
        #                           [4, 5, 6]
        #                           [7, 8, 9]]
        self.assertEqual(subtraction([[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # матрица A
                                     [[20, 20, 20], [15, 10, 6], [8, 11, 10]]),  # матрица B
                         [[-19, -18, -17], [-11, -5, 0], [-1, -3, -1]])  # результат разности

        self.assertEqual(subtraction([[73, 7, 756], [643, 62, 6], [5, 50, 555]],
                                     [[25, 4, 43], [235, 63, 0], [34, 2, -1]]),
                         [[48, 3, 713], [408, -1, 6], [-29, 48, 556]])

    #    self.assertEqual(Diff([[1, 2], [4, 5], [3, 8]],
    #                          [[1], [1], [1]]),
    #                     'Размеры матриц должны быть одинаковыми')


if __name__ == "__main__":
    unittest.main()
