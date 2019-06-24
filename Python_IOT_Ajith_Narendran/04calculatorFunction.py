
def addition(n1, n2):
    global n3
    n3 = n1 + n2 + 100
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def subtraction(n1, n2):
    return n1 - n2


def division(n1, n2):
    return n1 / n2


n_one = int(input('Enter first num: '))
n_two = int(input('Enter second num: '))
op = input('Enter the operation: ')
if op == '+':
    result = addition(n_one, n_two)
elif op == '-':
    result = subtraction(n_one, n_two)
elif op == '*' or op == 'x':
    result = multiplication(n_one, n_two)
elif op == '/':
    result = division(n_one, n_two)
else:
    print('Wrong choice, try again!')
print(result)
print("This is global: ", n3)