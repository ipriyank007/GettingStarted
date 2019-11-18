class Employee:
    company_name = 'ABC Corp.'
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    
    def show_data(self):
        print(f'name:{self.name}\nage:{self.age}\nrole:{self.role}\ncompany:{self.company_name}')
    

a = Employee('Anthony', 33, 'Manager')
a.show_data()
b = Employee('Bob', 43, 'Accountant')
b.show_data()

