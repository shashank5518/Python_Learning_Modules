import os

os.chdir("D:/Python/testing")

import unittest
import _40_1_calc_for_test


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(_40_1_calc_for_test.add(10, 5), 15)
        self.assertEqual(_40_1_calc_for_test.add(-1, 1), 0)
        self.assertEqual(_40_1_calc_for_test.add(-1, -7), -8)
        self.assertEqual(_40_1_calc_for_test.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(_40_1_calc_for_test.subtract(10, 5), 5)
        self.assertEqual(_40_1_calc_for_test.subtract(-1, 1), -2)
        self.assertEqual(_40_1_calc_for_test.subtract(-1, -7), 6)
        self.assertEqual(_40_1_calc_for_test.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(_40_1_calc_for_test.multiply(10, 5), 50)
        self.assertEqual(_40_1_calc_for_test.multiply(-1, 1), -1)
        self.assertEqual(_40_1_calc_for_test.multiply(-1, -7), 7)
        self.assertEqual(_40_1_calc_for_test.multiply(0, 65), 0)
        self.assertEqual(_40_1_calc_for_test.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(_40_1_calc_for_test.divide(10, 5), 2)
        self.assertEqual(_40_1_calc_for_test.divide(-1, 1), -1)
        self.assertEqual(_40_1_calc_for_test.divide(-7, -1), 7)
        # self.assertEqual(_40_1_calc_for_test.divide(1 ,0), 0)
        self.assertEqual(_40_1_calc_for_test.divide(0, 1), 0)
        # self.assertEqual(_40_1_calc_for_test.divide(0 ,0), 0)

        # self.assertRaises(ValueError, _40_1_calc_for_test.divide, 10, 0)
        # self.assertRaises(ValueError, _40_1_calc_for_test.divide, 10, 2)

        with self.assertRaises(ValueError):
            _40_1_calc_for_test.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
