##tax bracketes

##0 - 400000 tax - 5%
##400000 - 1000000 tax - 8%
##1000000 - 2500000 tax - 10%

salary = int(input('Enter your salary'))

if salary > 0 and salary <= 400000:
    print('salary between 0 - 400000')
    print('tax applied is 5%')
    rem_salary = salary - salary*5/100
    print('Remaining salary', rem_salary)
elif salary > 400000 and salary <= 1000000:
    print('salary between 400000 - 1000000')
    print('tax applied is 8%')
    rem_salary = salary - salary*8/100
    print('Remaining salary', rem_salary)
elif salary > 1000000 and salary <= 2500000:
    print('salary between 400000 - 1000000')
    print('tax applied is 10%')
    rem_salary = salary - salary*10/100
    print('Remaining salary', rem_salary)
else:
    print('Please enter a valid range')
