import os
import time

currdir = os.getcwd()
os.mkdir('New Folder')
time.sleep(3)
os.rename('New Folder', 'New Folder2')
time.sleep(3)
# os.rmdir('New Folder2')
print(currdir)
