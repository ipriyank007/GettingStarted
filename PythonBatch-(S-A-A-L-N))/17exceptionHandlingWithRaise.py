


try:
    amt = int(input('Enter amt: '))
    if amt > 10000:
        raise ValueError('This is memory error.')
    print(amt)
except ValueError as e:
    print(e)
