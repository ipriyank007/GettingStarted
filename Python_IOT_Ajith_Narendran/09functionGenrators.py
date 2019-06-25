my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def doubling_list(target_list):
#     d_list = []
#     for item in target_list:
#         d_list.append(item*2)
#     return d_list
#
#
# new_list = doubling_list(my_list)
# print(new_list)


def doubling_items(target_list):
    for item in target_list:
        yield item**0.5


new_list = doubling_items(my_list)

for i in new_list:
    print(i)
