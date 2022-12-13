
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

Hero = SuperHero('Hiro','Homada\n','Fly\n','30','a')
Hero.x()
Hero.a()
print(Hero)
print(f'catchphrase: {len(Hero.catchphrase)}')






































