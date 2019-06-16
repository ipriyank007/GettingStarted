import os

files = []
folders = []
for (path, dirnames, filenames) in os.walk('Data'):
    folders.extend(os.path.join(path, name) for name in dirnames)
    files.extend(os.path.join(path, name) for name in filenames)

print(files)
print(folders)