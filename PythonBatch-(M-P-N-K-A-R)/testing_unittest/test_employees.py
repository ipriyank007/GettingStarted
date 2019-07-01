from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('John', 'Adams', 24, 300000)
        emp2 = Employee('Ron', 'MacDonald', 25, 350000)

        self.assertEqual(emp1.email, 'John.Adams24@gmail.com')
        self.assertEqual(emp2.email, 'Ron.MacDonald25@gmail.com')

        emp1.first = 'Sam'
        emp2.first = 'Norm'

        self.assertEqual(emp1.email, 'Sam.Adams24@gmail.com')
        self.assertEqual(emp2.email, 'Norm.MacDonald25@gmail.com')


    def test_full_name(self):
        emp1 = Employee('John', 'Adams', 24, 300000)
        emp2 = Employee('Ron', 'MacDonald', 25, 350000)

        print(emp1.full_name)
        self.assertEqual(emp1.full_name, 'John Adams')
        self.assertEqual(emp2.full_name, 'Ron MacDonald')

        emp1.first = 'Sam'
        emp2.first = 'Norm'

        self.assertEqual(emp1.full_name, 'Sam Adams')
        self.assertEqual(emp2.full_name, 'Norm MacDonald')


    def test_give_raise(self):
        emp1 = Employee('John', 'Adams', 24, 300000)
        emp2 = Employee('Ron', 'MacDonald', 25, 350000)

        emp1.give_raise()
        emp2.give_raise()

        self.assertEqual(emp1.pay, 450000)
        self.assertEqual(emp2.pay, 525000)


if __name__ == '__main__':
    unittest.main()
