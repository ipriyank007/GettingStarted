class Gonebad(Exception):
    def __init__(self, msg):
        self.msg = msg
    def giveTheError(self):
        print("Gone bad because", self.msg)

try:
    raise Gonebad("I've bad feeling about this!")
except Gonebad as e:
    print(e.giveTheError())
