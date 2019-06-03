# a = 5
# b = 0
#
# try:
#     print(a/b)
#
# except ZeroDivisionError:
#     print('Please try again!')
#
# finally:
#     print("Process Ended!")
try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))


    print(a+b)
except ValueError:
    print('Try again')