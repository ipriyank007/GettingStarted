import os

os.chdir('C:/Users/Jagadheesh/python_batches/Python_300Batch')
file_to_find = 'cities.csv'
location = ''
# data = os.walk(os.getcwd())
for path, dirs, files in os.walk(os.getcwd()):
    if file_to_find in files:
        location = path
        break
    print(path)
    print(dirs)
    print(files)
    print('\n')

print(f'{file_to_find} exists in {location}')