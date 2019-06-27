# def addition(n1=0, n2=0):
#     return n1+n2
#
#
# result = addition(12)
# print(result)


def generate_email_id(fn, ln, ag):
    global  myfn
    myfn = fn
    print(f'Your email id is: {fn}.{ln}{ag}@gmail.com')


f_name = input("Enter firstname: ")
l_name = input("Enter lastname: ")
age = input("Enter your age: ")

generate_email_id(f_name, l_name, age)

print(myfn)
# a = int(input('Enter a number: '))
# b = int(input('Enter another num: '))
#
# print(a+b)


