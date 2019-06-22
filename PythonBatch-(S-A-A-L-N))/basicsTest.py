def printingfunction(mylist):
    # squaredlist = []
    # for i in mylist:
    #     squaredlist.append(i*i)
    # return squaredlist
    for i in mylist:
        yield i*i

mylist = [i for i in range(100)]
result = printingfunction(mylist)

for i in result:
    print(i)
