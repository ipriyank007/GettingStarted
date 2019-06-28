with open('filename.txt', 'rb') as rf:
    with open('filename2.txt', 'wb') as wf:
        data = rf.read()
        wf.write(data)
    print(wf.closed)

# rf = open('C:\\Users\\Priyank007\\eclipse-workspace\\GettingStarted\\45.jpg', 'rb')
# wf = open('newImage2.jpg', 'wb')
# data = rf.read()
# wf.write(data)
# wf.close()
# rf.close()
