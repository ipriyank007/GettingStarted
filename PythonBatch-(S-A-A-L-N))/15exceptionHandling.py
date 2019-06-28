n = input('Enter numerator: ')
d = input('Enter denominator: ')

try:
    n = int(n)
    d = int(d)
    quotient = n / d
    print(quotient)

except ZeroDivisionError:
    print('You cannot divide by zero.')

except ValueError:
    print('You have to enter nums only')

# except:
#     print('There is some issue because,', e)