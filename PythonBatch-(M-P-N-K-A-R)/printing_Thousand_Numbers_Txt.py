import random

numbers_to_print = []

for i in range(1000):
    new_no = random.randrange(100, 1000)
    numbers_to_print.append(new_no)
toprint = ''
for i in numbers_to_print:
    toprint += str(i)+' '
newfile = open('New_Sample.txt', 'w')
newfile.write(toprint)
newfile.close()
