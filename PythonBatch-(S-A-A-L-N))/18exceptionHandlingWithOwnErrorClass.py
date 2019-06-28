class InternError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def more_than_million(self):
        print('You cannot handle transaction about 1,00,000 because,', self.msg)


try:
    amt = int(input("Enter Transaction amount: "))
    if amt >= 1000000:
        raise InternError('You are an Intern!')
except InternError as e:
    e.more_than_million()
