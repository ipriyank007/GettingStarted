# exec('x = 5')
# print(x)


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
print()
for i in mygenerator:
    print(i)