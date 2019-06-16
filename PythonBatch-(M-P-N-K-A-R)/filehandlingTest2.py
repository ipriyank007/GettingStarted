with open('filehandling2.txt', 'r') as f:

    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)

    # f_content = f.read(10)
    # print(f_content)

    # for line in f:
    #     print(line, end='')


    # f_content = f.readline()
    # print(f_content, end='')
    #
    # f_content = f.readline()
    # print(f_content, end='')

    # f_content = f.read(100)
    # print(f_content)
    # f_content = f.read(100)
    # print(f_content)
    # f_content = f.read(100)
    # print(f_content)

    # f_content = f.read(10)
    # print(f_content, end='*')

    # print(f.tell())
