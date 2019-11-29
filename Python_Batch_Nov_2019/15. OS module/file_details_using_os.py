import os
from datetime import datetime

os.chdir('C:/Users/Jagadheesh/python_batches/Python_300Batch')
info = os.stat('C:/Users/Public/Pictures/Sample Pictures/penguins.jpg')
# print(info.st_size)
mdate = info.st_mtime
normal_mdate = datetime.fromtimestamp(mdate)
print(normal_mdate.date())
print(round(info.st_size/1024, 2), 'KB')