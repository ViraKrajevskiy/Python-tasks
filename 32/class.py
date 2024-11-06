import psycopg2
class Parent:
    def __init__(self,hero):
        self.hero = hero

    def info(self):
        print(f" hi {self.hero}")


class Part(Parent):
    def __init__(self,hero,helo,hi):
        super().__init__(hero)
        self.helo = helo
        self.hi = hi

    def info(self):
        print(f"hi how are you {self.hero},")

class a:
    pass
class b(a):
    pass
class c(b):
    pass
#многоуровневое наследие