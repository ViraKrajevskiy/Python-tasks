from typing import Counter

class Num_random:
    count = 0
    def __init__(self,Num1,Sing,Num2,cost):
        self.Num1 = Num1
        self.Sing = Sing
        self.Num2 = Num2
        self.cost = cost
        Num_random.count +=cost

    @staticmethod
    def oop_e(self):
        print('hi')


    @classmethod
    def Counter(cls):
        return f"Общая стоимость: {cls.count}"



Info = Num_random('Mercedes','2012','M200',65372153)
INFO2 = Num_random('','','',20794614)
Info3 = Num_random('Mercedes','2012','M200',65372132153)
INFO4 = Num_random('','','',2079461212134)

print(Num_random.Counter())

