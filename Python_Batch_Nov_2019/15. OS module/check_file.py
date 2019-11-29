import os

os.chdir('C:/Users/Public/Pictures/Sample Pictures/')

file_to_check = 'Penguins.jpg'

path_to_check = os.path.join(os.getcwd(), file_to_check)

if os.path.exists(path_to_check):
    print('file exists')

else:
    print("file doesn't exits!")
