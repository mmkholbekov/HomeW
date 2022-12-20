
class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.health_points = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def x(self):
        print(f'Name:{self.name}')

    def a(self):
        self.health_points *= 1

    def __str__(self):
        return f'Nickname:{self.nickname}'\
               f'Power:{self.superpower}'\
               f'health:{self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

Hero = SuperHero('Bug','M7055\n','Fly\n','30','Not')
Hero.x()
Hero.a()
print(Hero)
print(f'catchphrase: {len(Hero.catchphrase)}')


# Hw2

class Robot(SuperHero):
    people = 'people'

    def __init__(self, name,nickname,superpower,health_points,catchphrase, damage=False, fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def n(self):
        hd = self.health_points ** 2
        self.health_points = hd
    def a(self):
        self.fly = True
    def phrase(self):
        print('fly in the True_phrase')

hdr = Robot('Rob','OTO\n','Dexterity\n', 10, 'no')
hdr.n()
print(hdr)
print(f'Damage:{hdr.damage}')
hdr.a()
print(f'Fly: {hdr.fly}')
hdr.phrase()


class Robot2(SuperHero):
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase, damage=False, fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly

    def n(self):
        dest = self.health_points ** 2
        self.health_points = dest

    def a(self):
        self.fly = True

    def phrase(self):
         print('fly in the True_phrase')

des = Robot2('Dotty', 'Bot\n', 'Power\n', 10, 'No')
des.n()
print(des)
print(f'Damage: {des.damage}')
des.a()
print(f'Fly: {des.fly}')
des.phrase()

class Villian(Robot2):
    monster = 'monster'

    def __init__(self, name,nickname,superpower,health_points,catchphrase):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
    def gen_x(self):...
    def crit(self):
        print(f'Crit:{self * 2}')
newf = Villian('Wall-E', 'R2D2\n', 'Intelegence\n', 50, 'robot')
print(newf)
newf.gen_x()
Villian.crit(hdr.damage)









































