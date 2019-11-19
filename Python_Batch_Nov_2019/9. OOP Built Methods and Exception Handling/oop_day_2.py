class Associate:
    def __init__(self, name, role, age):
        self.name = name
        self.role = role
        self.age = age
    
    def do_associte(self, associating_with):
        print(f'{self.name} associating with {associating_with}')

    def __str__(self):
        return self.name
    


a = Associate('Adam', 'Associate Developer', 22)
a.do_associte('Matt')
b = Associate('Bob', 'Associate Technician', 24)
b.do_associte(a)
print(a)
print(b)