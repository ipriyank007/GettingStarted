import random

first = ['sam', 'Wade', 'tony', 'bruce']
last = ['arnold', 'Wilson', 'stark', 'Wayne']
domains = ['gmail', 'yahoo', 'hotmail', 'live']
n = int(input("Emails you want: "))

with open('FakeEmails.txt', 'w') as f:
    for i in range(n):
        f_name = random.choice(first)
        l_name = random.choice(last)
        r_no = random.randint(100, 999)
        d_name = random.choice(domains)


        email = f'{f_name}.{l_name}{r_no}@{d_name}.com\n'
        f.write(email)
