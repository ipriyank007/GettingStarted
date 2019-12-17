import unittest
from calculator import Calc
import calculator

class CalcTest(unittest.TestCase):
    obj = Calc()
    def test_addition(self):
        
        self.assertEqual(self.obj.addition(4, 6), 10)
        self.assertEqual(self.obj.addition(-5, 5), 0)
        self.assertEqual(self.obj.addition(-5, -5), -10)
    
    def test_subtraction(self):
        self.assertEqual(self.obj.subtraction(4, 2), 2)
        self.assertEqual(self.obj.subtraction(2, 4), -2)
        self.assertEqual(self.obj.subtraction(2, 2), 0)
    
    def test_multiplication(self):
        self.assertEqual(self.obj.multiplication(4, 2), 8)
        self.assertEqual(self.obj.multiplication(-2, 4), -8)
        self.assertEqual(self.obj.multiplication(-2, -2), 4)

    def test_division(self):
        self.assertAlmostEqual(self.obj.division(4, 2), 2, places=0)
        self.assertAlmostEqual(self.obj.division(2, 4), 0, places=0)
        self.assertAlmostEqual(self.obj.division(2, 2), 1, places=0)
        self.assertRaises(ZeroDivisionError, self.obj.division, 13, 0)
        with self.assertRaises(ZeroDivisionError):
            self.obj.division(2, 0)

# print(calculator.__name__)

if __name__ == '__main__':
    unittest.main()
    


## unittest docs: https://docs.python.org/3/library/unittest.html
