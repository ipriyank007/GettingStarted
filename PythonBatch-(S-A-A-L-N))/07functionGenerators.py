mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def print_double(mylist):
#     new_list = []
#     for i in mylist:
#         new_list.append(i*2)
#     return new_list


def print_double(mylist):
    for i in mylist:
        yield i*2


new_values = print_double(mylist)
for i in new_values:
    print(i)
