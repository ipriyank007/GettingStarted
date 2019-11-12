nums = [12, 23, 34, 45, 54, 56, 65]

sq_num = [i ** 2 for i in nums if i < 50]


nums = [12, -23, 34, -32, 43, 22, -92]

positive_nums = [i if i > 0 else 0 for i in nums]

one = [12, 34, 45, 45]
two = [17, 23, 22, 53]
three = [10, 20, 30, 40]
four = [9, 15, 33, 46]

##quotients = [i/j if i > j else j/i for i, j in zip(one, two)]

##quotients = [i[0]/i[1] if i[0] > i[1] else i[1]/i[0] for i in zip(one, two)]

##smaller = [i if i < j else j for i, j in zip(one, two)]

##total = [sum(i) for i in zip(one, two, three, four)]


first = ['Sam', 'George', 'James']
last = ['Adams', 'Washigton', 'Maddison']

full_names = [f'{i} {j}' for i, j in zip(first, last)]

fruits = ['apple', 'peach', 'grape', 'banana', 'mango']

len_fruits = [len(i) for i in fruits]
