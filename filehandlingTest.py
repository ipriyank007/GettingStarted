# my_text = '''
#     ######
#     #    #
#     #    #
#     ######
# '''
#
#
# f = open('filehandling.txt', 'w')
# f.write(my_text)
# # f.write("Continued...")
# f.close()

with open('filehandling.txt', 'w') as f:
    f.write("This is a better method")
print(f.closed)
print(f.name)
print(f.mode)
