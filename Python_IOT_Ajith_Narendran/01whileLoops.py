a = int(input('Enter first number: '))
d = int(input("Enter the difference you want: "))
n = int(input("Enter no of iteration you want: "))

temp = a

while a < temp+n*d:
    print(a)
    a += d
