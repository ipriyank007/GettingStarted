import unittest
import calc_for_test

class Test_Calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc_for_test.add(10, 5), 15)
        self.assertEqual(calc_for_test.add(-10, 5), -5)
        self.assertEqual(calc_for_test.add(-10, -5), -15)


    def test_add(self):
        self.assertEqual(calc_for_test.add(10, 5), 15)
        self.assertEqual(calc_for_test.add(-10, 5), -5)
        self.assertEqual(calc_for_test.add(-10, -5), -15)


    def test_subtract(self):
        self.assertEqual(calc_for_test.subtract(10, 5), 5)
        self.assertEqual(calc_for_test.subtract(-10, 5), -15)
        self.assertEqual(calc_for_test.subtract(-10, -5), -5)


    def test_multiply(self):
        self.assertEqual(calc_for_test.multiply(10, 5), 50)
        self.assertEqual(calc_for_test.multiply(-10, 5), -50)
        self.assertEqual(calc_for_test.multiply(-10, -5), 50)


    def test_divide(self):
        self.assertEqual(calc_for_test.divide(10, 5), 2)
        self.assertEqual(calc_for_test.divide(-10, 5), -2)
        self.assertEqual(calc_for_test.divide(-10, -5), 2)
        self.assertEqual(calc_for_test.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc_for_test.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc_for_test.divide(0, 0)



if __name__ == '__main__':
    unittest.main()
