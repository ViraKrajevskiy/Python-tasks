class ExampleClass:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        ExampleClass.counter += 1

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def is_adult(self):
        return self.age >= 18

    @classmethod
    def get_instance_count(cls):
        return f"Всего экземпляров: {cls.counter}"

    @classmethod
    def create_default_instance(cls):
        return cls("Имя по умолчанию", 0)

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        return number * ExampleClass.factorial(number - 1)


person1 = ExampleClass("Алиса", 25)
person2 = ExampleClass("Боб", 17)

print(person1.display_info())
print(person2.is_adult())
print(ExampleClass.get_instance_count())
default_person = ExampleClass.create_default_instance()
print(default_person.display_info())
print(ExampleClass.is_even(10))
print(ExampleClass.factorial(5))
