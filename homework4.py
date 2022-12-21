class A:
    def __init__(self,name):
        self.name = name

class B:
    def __init__(self,age):
        self.age = age

class C(A):
    def no(self):
        print(f'{self.name}R')

class D(B):
    def born(self):
        print(f'Born(2020 - self.age')

class E(C, D):
    def __init__(self,name,age):
        C.__init__(self, name)
        D.__init__(self, age)

x = E('Ben', 20)
x.no()
x.born()

with open("Git_codes.txt","w")as file:
    file.write('git init'
               'git remote add origin(Ссылка с гита)'
               'git add(Названия файла)'
               'git add.(Выбрать все файлы)'
               'git commit -m (Коментарии)'
               'git push origin main'
               'git branch'
               'git branch -d main'
               'git checkout -b main'
               'git clone'
               'git status')







