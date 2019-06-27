# import math
#
# n = 4
#
# print(math.sin(math.pi/2))

import os
import time

print(os.getcwd())

os.chdir('C:\\Users\\Priyank007\\eclipse-workspace')
print(os.getcwd())

# os.mkdir('PythonTest\\Testing')
# os.makedirs('PythonTest\\Testing')
# time.sleep(5)
# os.removedirs('PythonTest')



# time.sleep(3)
# os.rename('PythonTest', 'OsChanged')

# t = time.asctime()
# print(t.split()[3])
#
# v = os.environ.get('Path')
# print(v)

for i, j, k in os.walk('C:\\Users\\Priyank007\\eclipse-workspace'):

    if k == []:
        continue
    print(k)





