# n = int(input("Enter the number: "))
# d = int(input('Enter difference: '))
# t = int(input('Enter Iterations: '))
# temp = n
# while n < temp+d*t:
#     print(n)
#     n += d

# '''
n = int(input("Enter the number: "))
a = int(input('Enter difference: '))
t = int(input('Enter Iterations: '))

temp = n

while n < temp*(a**t):
    print(n)
    n *= a
# '''

# mylist = ['apple', 'banana', 'grapes', 'oranges']
# n = len(mylist)
# while n > 0:
#     print(mylist[len(mylist)-n])
#     n -= 1

# n = 5
#
# while n<10:
#     print(n)
#     n+=2