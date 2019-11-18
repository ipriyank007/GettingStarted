# class PlantEnemy:
#     def __init__(self, name, height, strength, life):
#         self.name = name
#         self.height = height
#         self.strength = strength
    
    
#     def attack(self):
#         print('Waam!!')


# class Enemy(PlantEnemy):
#     def move(self, direction):
#         print(f'Moving {direction}...')


# a = PlantEnemy('vine', 12.5, 20, 60)

# b = Enemy('bowser', 2.3, 40, 50)
# b.move('right')

class Mario:
    def __init__(self, lives):
        self.lives = lives
    
    def move(self, direction):
        print(f'moving, {direction}')
    
    def jump(self):
        print('Jump!!')
    
    def increase_life(self):
        self.lives += 1
        print(f'{self.lives} remaining!')

    def show_lives(self):
        print('lives left:', self.lives)

class Shroom(Mario):
    def about(self):
        print('100% bigger than the Mario')


class BigMario(Shroom):
    def increase_life(self):
        self.lives += 1
        print(f'{self.lives} remaining!')   

m = Mario(3)
m.move('left')
m.increase_life()
bm = BigMario(3)
bm.move('right')
bm.show_lives()
bm.about()