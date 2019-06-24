def generate_email(f_name, l_name, age):
    email_id = f'{f_name}.{l_name}{age}@gmail.com'
    return email_id


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))
my_email = generate_email(first_name, last_name, age)
print(my_email)
