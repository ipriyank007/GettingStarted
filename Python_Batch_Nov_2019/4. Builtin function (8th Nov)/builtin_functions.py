# All and Any

# nums = [12, 32, 23, 34, 44,]

# nums2 = [1, 10, None,]

## Any ##
# check = any(nums) # check not None or zero value in iterable

# check2 = any(nums2)

## All ##

# check = all(nums) # check all values to be non zero or non None
# check2 = all(nums2)

# print(check2)


# Conversions:

# 1. Int
# value = '1001'
# b = False
# # int - to convert data to an integer base 10
# int_value = int(value)
# int_b = int(b)
# print(int_value * 2)
# print(int_b)

# 2. Str
# num = 2
# b = True
# # str - to convert data to a string

# str_num = str(num)

# str_b = str(b)
# # print(b) -> True
# # print(type(num)) -> '2'

# 3. Float

# num = 10
# value = '123.345'

# # float - to convert valid data to float

# float_num = float(num)
# float_value = float(value)
# print(float_num)
# print(float_value)


# 4. Bool

# num = 10
# num2 = 0
# num3 = -52
# s1 = 'Hello'
# s2 = ''

# # bool - convert any data to its boolean equivalent

# # bool_num = bool(num) -> True
# # bool_num2 = bool(num2) -> False
# # bool_num3 = bool(num3) -> True
# # bool_s1 = bool(s1) -> True
# bool_s2 = bool(s2)
# print(bool_s2)

# 5 Hex

# num = 10 
# num2 = 0
# s1 = 'hello' -> error
# s2 = '123' -> convert to int for this to work

# hex - to convert data to a hexadecimal value

# hex_num = hex(int(s2))
# print(hex_num)


# 6. list

# nums = {12, 34, 56, 67, 56, 45, 45}
# nums_list = list(nums)
# print(nums_list)

# 7. Tuple

# items = ['one', 'two', 'three', 'four']
# items_new = tuple(items)
# print(items_new)

# 8. Set

# values = [ 23, 34, 'python', True]
# values_set = set(values)
# print(values_set)


# 9 Dict

# data = [(1, (1, 1)), (2,( 2, 4)), (3, (3, 9)), (4, (4, 16))]
# data_dict = dict(data)
# print(data_dict)


# Exec
# code = "x = 5"
# exec(code)
# print(x) -> 5


# Sorted

# nums = [112, 213, 334, 415, 156]
# sort_nums = sorted(nums, reverse=True)
# print(sort_nums)


# Abs
# n = -5
# n2 = 5

# print(bin(n))

# Chr
# n = 9

# print(chr(n))

# Ord

# ch = 'a'
# print(ord(ch))

# print(divmod(5,3))

# Enumerate
# items = ['one', 'two', 'three', 'four']
# print(dict(enumerate(items)))

# reversed
# nums = [1, 2 , 43, 4 , 5]
# print(list(reversed(nums)))

# Sum
# print(sum(nums))

# Round
# n = 3.7
# print(round(n))
# ID - To get memory location of the object
# num = 50
# print(id(num))

