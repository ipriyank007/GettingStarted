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
        self.count=0
        if self.count > 0 :
            print("Now I can shoot fireballs")
        self.count+=1
class Big_Mario(Mario, Shroom):
    pass
    

bm = Big_Mario()
bm.move()
bm.eat_Shroom()
bm.eat_Shroom()
bm.eat_Shroom()