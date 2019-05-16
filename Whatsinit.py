class Enemy:
    def __init__(self,x):
        self.energy = x
    def current_Energy(self):
        print(self.energy)
        
enemy766 = Enemy(5)
Boss_Enemy = Enemy(30)

enemy766.current_Energy()
Boss_Enemy.current_Energy()