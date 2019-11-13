groceries = ['honey', 'milk', 'chips', 'bread', 'apple', 'water']

item = input('enter the item')

if item in groceries:
    groceries.remove(item)
    print(item, 'is removed')
else:
    groceries.append(item)
    print(item, 'added to grocries')

print(groceries)




##items = ['lemon', 'oranges', 'oil']
##
##for item in items:
##    groceries.append(item)
##
##print(groceries)

##item = input('Enter an item')
##
##if item in groceries:
##    print('yes item already in list')
##
##else:
##    groceries.append(item)
##    print(item, 'added to your list')
##
##print(groceries)
