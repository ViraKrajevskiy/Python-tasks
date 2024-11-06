import re


class Student:
    def __init__(self, name, age, telegram_username, phone_number, email, passport_series):
        self._name = None
        self._age = None
        self._telegram_username = None
        self._phone_number = None
        self._email = None
        self._passport_series = None

        # Устанавливаем начальные значения через сеттеры
        self.name = name
        self.age = age
        self.telegram_username = telegram_username
        self.phone_number = phone_number
        self.email = email
        self.passport_series = passport_series

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.fullmatch(r'[A-Za-zА-Яа-яёЁ\s\-]+', value):
            self._name = value
        else:
            raise ValueError("Имя должно содержать только буквы, пробелы или дефисы.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 < value < 120:
            self._age = value
        else:
            raise ValueError("Возраст должен быть числом от 1 до 119.")

    @property
    def telegram_username(self):
        return self._telegram_username

    @telegram_username.setter
    def telegram_username(self, value):
        if re.fullmatch(r'@[A-Za-z0-9_]{5,}', value):
            self._telegram_username = value
        else:
            raise ValueError("Телеграм-юзернейм должен начинаться с '@' и содержать не менее 5 символов.")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if re.fullmatch(r'\+?\d{10,15}', value):
            self._phone_number = value
        else:
            raise ValueError("Телефон должен содержать от 10 до 15 цифр, опционально начинаться с '+'.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', value):
            self._email = value
        else:
            raise ValueError("Некорректный формат email.")

    @property
    def passport_series(self):
        return self._passport_series

    @passport_series.setter
    def passport_series(self, value):
        if re.fullmatch(r'\d{4}\s\d{6}', value):
            self._passport_series = value
        else:
            raise ValueError("Серия паспорта должна быть в формате 'XXXX XXXXXX', где X — цифра.")

    @staticmethod
    def create_student_from_input():
        while True:
            try:
                name = input("Введите имя: ")
                age = int(input("Введите возраст: "))
                telegram_username = input("Введите Telegram-юзернейм (начинается с '@'): ")
                phone_number = input("Введите номер телефона (с '+' или без): ")
                email = input("Введите email: ")
                passport_series = input("Введите серию паспорта (формат 'XXXX XXXXXX'): ")

                return Student(
                    name=name,
                    age=age,
                    telegram_username=telegram_username,
                    phone_number=phone_number,
                    email=email,
                    passport_series=passport_series
                )
            except ValueError as e:
                print(f"Ошибка: {e}")
                print("Попробуйте ещё раз.\n")


# Пример использования
if __name__ == "__main__":
    student = Student.create_student_from_input()
    print("Студент успешно создан:")
    print(f"Имя: {student.name}")
    print(f"Возраст: {student.age}")
    print(f"Telegram: {student.telegram_username}")
    print(f"Телефон: {student.phone_number}")
    print(f"Email: {student.email}")
    print(f"Серия паспорта: {student.passport_series}")
