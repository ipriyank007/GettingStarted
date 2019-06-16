import os

os.chdir('C:/Users/Priyank007/eclipse-workspace')
print(os.getcwd())
# os.makedirs('C:\\Users\\Priyank007\\eclipse-workspace')
# print(os.listdir('C:\\Users\\Priyank007\\eclipse-workspace'))
print(os.stat('GettingStartedRobotSample.csv').st_size)

