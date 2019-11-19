# transaction_amt = input('enter transaction amount: ')
# print(help(Exception))
# try:
#     transaction_amt = int(transaction_amt)
#     if transaction_amt >= 100000:
#         raise ValueError('You are not allowed to handling such amount')
#     print('proceed transaction!')

# except ValueError as v:
#     print(v)

class ZeroToPowerZeroError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

a = input('enter value of a: ')
b = input('enter value of b: ')

try:
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        raise ZeroToPowerZeroError('0 to power of 0 is undefined!')
    print(a ** b)


except ValueError as v:
    print(v)

except ZeroToPowerZeroError as z:
    print(z)