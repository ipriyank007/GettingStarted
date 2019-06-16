import random

# welcometext = ['hey', 'hi', 'howdy', 'hola']

# randtext = random.choice(welcometext)
# print(randtext+ "! Visitor")

# balls = ['red', 'blue', 'green']
# result = random.choices(balls, weights=[12,12,2], k=9)
# print(result)

cards = list(range(1,53))

random.shuffle(cards)
print(cards)

mycard = random.sample(cards, k=4)
print(mycard)
