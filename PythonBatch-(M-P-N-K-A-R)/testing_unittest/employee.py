
class Employee:

    raise_amount = 1.5


    def __init__(self, first, last, age , pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}{self.age}@gmail.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'


    def give_raise(self):
        self.pay = self.raise_amount*self.pay
