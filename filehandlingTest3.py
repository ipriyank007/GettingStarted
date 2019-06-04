# with open('filehandling2.txt','r') as rf:
#     with open('filehandling2_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

with open('148.jpg','rb') as rf:
    with open('148_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)