suits = ['sphade', 'heart', 'club', 'diamond'] #All suits in the deck

values = [i for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace'] #All 13 values in a deck of cards



deck = [(v, s) for s in suits for v in values]      #making our entire deck based on values and suits.
print(len(deck))        #Total numbers of cards in deck
for i in range(4):
    hand = random.sample(deck, 4)   #sampling out 4 random cards from our deck.
    for j in hand:
        deck.remove(j)      #removing the given hand from the deck.
    print(hand)     #Hands of each players
print(len(deck))  #Cards left in deck
