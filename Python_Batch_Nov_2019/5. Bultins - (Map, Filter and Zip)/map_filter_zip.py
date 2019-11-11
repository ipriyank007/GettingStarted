##1. Map

##def double_number(n):
##    return n * 2

##nums = [10, 20, 30, 40, 50, 60, 70]

##double_list = list(map(double_number, nums))


##double = []
##for num in nums:
##    double.append(num *2)


##2. Filter
##def check_even(n):
##    if n % 2 == 0:
##        return True
##    else:
##        return False

##nums = [12, 23, 41, 22, 35, 64, 88]

##even_nums = list(filter(check_even, nums))
##print(even_nums)

##for num in nums:
##    if num%2==0:
##        even_nums.append(num)

##print(even_nums)


##3. Zip

##nums_one = [1, 2, 3, 4, 5, 6, 7, 8]
##nums_two = [9, 8, 7, 6, 5, 4,]

##nums_three = (zip(nums_one, nums_two))
##print(nums_three)


##def square(n):
##    return n ** 2
##
##nums = [2, 43, 6, 75, 34]
##
##sq_nums = list(map(square, nums))
##print(sq_nums)


##s = 'hello, world'
##print(s.split(', '))

##groceries = int(input('Enter the items: ')).split()
##print(type(groceries))
##print(groceries)

##12 23 34 43 56 65

##[12, 23, 34, 43, 56, 65]

##nums = input('Enter nums: ').split()
##list_nums = list(map(int, nums))
##print(list_nums)


first = ['john', 'dave']
last = ['Adams', 'Matthew']
ages = [23, 45]
##['John.Adams23@gmail.com', 'Dave.Matthew45@gmail.com']

def full_name_generator(t):
    f, l = t
    return f'{f.capitalize()} {l.capitalize()}'

full_name = list(map(full_name_generator, zip(first, last)))
print(full_name)














