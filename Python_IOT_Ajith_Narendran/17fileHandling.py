with open('C:\\Users\\Priyank007\\eclipse-workspace\\cat.jpg', 'rb') as rf:
    with open('C:\\Users\\Priyank007\\eclipse-workspace\\cat_copy.jpg', 'wb') as wf:
        text_to_copy = rf.read()
        wf.write(text_to_copy)

