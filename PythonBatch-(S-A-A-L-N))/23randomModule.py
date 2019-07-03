import random

# rno = random.random() # will give random value form 0-1. were 0 is inclusive and 100 is not
#rnos = random.randrange(0, 100)  #will give out values from 0 - 100 were 0 is inclusive and 100 is not
#rnos = random.randint(0, 100)  #will give out values from 0 - 100 were 0 is inclusive and 100 is not

# list1=['hello','hi',]
# greetings=random.choice(list1)  #will give out one random item from the iterable(list, tuple, etc)
# print(greetings)
suits = ['sphade', 'heart', 'club', 'diamond']
# random.shuffle(suits)  #will shuffle the deck.
values = [i for i in range(7, 11)] + ['Jack', 'Queen', 'King', 'Ace']
# my_card = random.shuffle(values, k=4)       #To get a random number of sample from a list. Here k signifies number of sample.

deck = [(v, s) for s in suits for v in values]
# my_choice = random.choice()       #to get one random choice from the list.

die_sides = int(input("Numbers of sides in the die: "))
roll = random.randint(1, die_sides)
print(roll)

''' Handling Probablity '''

    '''die_sides = 6'''
possibilities = [1, 2, 3, 4, 5, 6]
probablities = [1, 1, 1, 1, 1, 50]
rolls = random.choices(possibilities, weights=probablities, k=2) #Choices taking three arguments, first a list of items,
                                                                #Then the weights is to assign probablities of each items in the list.
                                                                #And k is for numbers of outputs we want.
print(rolls)
