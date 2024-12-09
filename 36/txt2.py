
from txt import Person

class Student(Person):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address
