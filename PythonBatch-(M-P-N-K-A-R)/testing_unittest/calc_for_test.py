class Calc:
    
    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    def multiply(a, b):
        return a * b


    def divide(a, b):
        if b == 0:
            raise ValueError("You cannot divide nums by zero!")
        return a / b
