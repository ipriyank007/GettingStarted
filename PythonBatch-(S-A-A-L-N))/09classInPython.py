class Humans:
    limbs = 4
    #This is a constructer:
    def __init__(self, eyecolor, height, name, age):
        self.eyecolor = eyecolor
        self.height = height
        self.name = name
        self.age = age


    def get_info(self):
        print(self.name)
        print(self.height)
        print(self.age)
        print(self.eyecolor)
        print(self.limbs)


ravi = Humans('Brown', 160, 'Ravi', 23)
ravi.get_info()

sam = Humans('Blue', 150, 'Samuel', 29)
sam.get_info()

jack = Humans('Green', 160, 'Jack', 49)
jack.limbs = 3
jack.get_info()