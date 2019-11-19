a = input('Enter value for a')
b = input('Enter value for b')


try:
    a = int(a)
    b = int(b)
    result = a / b
    print(result)
    print(name)


except ValueError:
    print('Give valid input!')

except NameError:
    print('undefined variable is called')

except ZeroDivisionError:
    print('Cannot divide a number by 0')



