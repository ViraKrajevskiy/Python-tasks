
from txt2 import Student

class Student_2(Student):
    def __init__(self, name, phone, address, course):
        super().__init__(name, phone, address)
        self.course = course
