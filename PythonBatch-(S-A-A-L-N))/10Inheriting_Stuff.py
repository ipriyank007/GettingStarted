'''
Created on Feb 19, 2019

@author: Priyank007
'''

class Mario():
    def move(self):
        print("Moving...")


class Shroom():
    def eat_Shroom(self):
        print("Now I am BIG!")


class Big_Mario(Mario, Shroom):
    pass
    

bm = Big_Mario()
bm.move()
bm.eat_Shroom()
bm.eat_Shroom()
bm.eat_Shroom()
k# print(issubclass(Big_Mario, Shroom))
# print(vars(Big_Mario))