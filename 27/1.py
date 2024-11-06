import random


def card():
     card2 = random.randint( 10000000000000000,9999999999999999)
     return card2

class Cashing_out:
    def __init__(self,card_number,work_date,user_name,password,balance):
        self.card_number = card_number
        self.work_date= work_date
        self.user_name= user_name
        self.password= password
        self.balance = balance


def __str__(self):
    return "Student classning object"


def info(self):
    return f"ism = {self.user_name}, cartsi{self.card_number}"


class Car:
    def __init__(self, color,mark,year,cost):
        self.color = color
        self.mark = mark
        self.year = year
        self.cost = cost

card = Car('red','supra',2435,'2366284$')
card1 = Car('green','supra2',202,'2366284$')
card2 = Car('blue','supram5',2004,'2366284$')
card3 = Car('yellow','supra',9000,'2366284$')

fer = [card,card1,card2,card3]
for i in fer:
    if i.year > 2000:
        print(i.year,i.mark)
