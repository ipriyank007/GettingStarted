##Arithmatic Progression

a = int(input ('Enter first number: '))
d = int(input('Enter common difference: '))
n = int(input('Number of term: '))

tn = a

while tn <= a + (n - 1) * d:
    print(tn, end=" ")
    tn += d
    

