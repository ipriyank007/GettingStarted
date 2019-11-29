import random

# n = random.random() #returns random num in range [0, 1)

#n = random.randrange(1, 10) # range: [1, 10)
#n = random.randint(1, 10) # [1, 10]

items = ['onion', 'carrot', 'peaches', 'tomatoes']
# random.shuffle(items)
# my_item = random.sample(items, k=2)
my_item = random.choices(items, weights=[1, 1, 50, 1], k=1)
#my_item = random.choice(items)

print(my_item)