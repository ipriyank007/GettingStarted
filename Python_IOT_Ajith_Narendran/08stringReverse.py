word = 'Hello'
word_list = list(word)
word_list = word_list[::-1]
print(' '.join(word_list))

n = input('Enter list items: ')
n_list = list(map(int, n.split(' ')))
print(n_list)
