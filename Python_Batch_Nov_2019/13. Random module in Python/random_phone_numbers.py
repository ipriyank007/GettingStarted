import random

n = int(input('Enter number of phone numbers: '))

# all_nums = [random.randint(6000000000, 9999999999) for i in range(n)]
with open('random_numbers.txt', 'w') as f:
    for _ in range(n):
        f.write(f'{random.randint(6000000000, 9999999999)}\t')