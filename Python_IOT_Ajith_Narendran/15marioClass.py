class Mario:

    def move(self):
        print('I am moving...')

    def jump(self):
        print('jump!')


class Shrooms:

    def eat_shroom(self):
        print("Now I'm Big!")


class Big_Mario(Mario, Shrooms):
    pass

bm = Big_Mario()
bm.move()
bm.jump()
bm.eat_shroom()
bm.eat_shroom()
bm.eat_shroom()