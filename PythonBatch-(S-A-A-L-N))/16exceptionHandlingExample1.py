try:
    with open('sample.txt', 'r') as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print('There is no file such file.')

