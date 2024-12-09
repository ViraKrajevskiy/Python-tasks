
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Men(Person):
    def __init__(self, name, phone, age):
        super().__init__(name, phone)
        self.age = age









