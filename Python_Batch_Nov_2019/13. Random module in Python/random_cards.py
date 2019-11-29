import random

PEOPLE = 4
EACH_HAND = 52//PEOPLE
suits = ['Spade', 'Heart', 'Club', 'Diamond']

values = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

deck = [(value, suit) for suit in suits for value in values ]

random.shuffle(deck)
# print(deck)
for i in range(PEOPLE):
    hand = random.sample(deck, k=EACH_HAND)
    for card in hand:
        deck.remove(card)
   
    print(hand)

print(len(deck))