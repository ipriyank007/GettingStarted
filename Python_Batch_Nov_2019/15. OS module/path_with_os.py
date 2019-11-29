import os.path

path = 'C:/users/test/'
file_name = 'demo.txt'

file_path = os.path.join(path, file_name)
# print(os.path.isfile('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg'))

# print(os.path.exists('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg'))

# base = os.path.basename('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg')
# print(base)
# dir_name = os.path.dirname('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg')
# print(dir_name)

# dir_file = os.path.split('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg')
# print(dir_file)

# path_ext = os.path.splitext('C:/Users/Pictures/Sample Pictures/penguins.jpg')
# print(path_ext)

drive_path = os.path.splitdrive('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg')

print(drive_path)

