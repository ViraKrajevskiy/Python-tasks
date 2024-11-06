class Student:
    def __init__(self,name,year):
        self.name = name
        self.year = year

    @property
    def info(self):
        return self.year

    @info.setter
    def info(self,info):
        self.year = info

    def check(self,info):
        if 1920 < info < 2024:
           self.year = info
        else:
            print('xato')


student = Student('kamol',2240)

student.year = 2025

print(student.year)

