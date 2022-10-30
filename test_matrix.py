import unittest


class TestAdd(unittest.TestCase):
    def test_addiction_positive(self):
        self.assertEqual(summation([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],  # matrix A
                                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),          # matrix B
                                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        self.assertEqual(summation([[3928, 2]], [[1, -2]]), [[3929, 0]])


class TestSubstr(unittest.TestCase):
    def test_subtraction_positive(self):
        self.assertEqual(subtraction([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                     [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        self.assertEqual(subtraction([[-10, 0, 9]], [[7, -5, 89]]), [[-17, 5, -80]])


class TestMultOnNumber(unittest.TestCase):
    def test_multiplication_on_number(self):
        self.assertEqual(multiplication_on_number([[0]], -3), [[0]])

        self.assertEqual(multiplication_on_number([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]], 2),
                                                  [[2, 2, 2, 2], [4, 4, 4, 4], [6, 6, 6, 6], [8, 8, 8, 8]])


class TestMultMatrix(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication([[12, 78, 96], [0, 1, 7865], [-88, -4, 0]],
                                        [[65, 11, -32], [-78, -52, -1], [172, 87, 99]]),
                                        [[-21816, -12276, -9966], [1352702, 684203, 778634], [-5408, -760, 2820]])


class TestTrans(unittest.TestCase):
    def test_transposition(self):
        self.assertEqual(transposition([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]),
                                       [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]])
