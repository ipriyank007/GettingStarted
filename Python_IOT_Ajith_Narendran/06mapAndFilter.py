# list1 = [12, 3, 5, 6, 7, 78, 8]
# mylist = list(map(lambda x: x*2, list1))

# print(mylist)

# mylist = list(filter(lambda x:x%2==0, list1))
# print(mylist)

nums = input("Enter numbers here: ")
list_of_nums = list(map(int, nums.split()))
print(list_of_nums)
