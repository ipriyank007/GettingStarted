my_list = [1, 2, 3, 4, 5]

new_list = list(map(lambda x: x*2, my_list))
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)
print(filtered_list)

