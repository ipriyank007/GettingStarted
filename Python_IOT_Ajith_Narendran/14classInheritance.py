class Parent:

    def gene_data(self, eyecolor, haircolor, height):
        self.eyecolor = eyecolor
        self.haircolor = haircolor
        self.height = height
        print(self.eyecolor)
        print(self.haircolor)
        print(self.height)


class Child(Parent):

    def personal_detail(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)


sam = Child()
sam.gene_data('brown', 'brown', 155)
sam.personal_detail('Samuel', 34)
print(sam.name)
