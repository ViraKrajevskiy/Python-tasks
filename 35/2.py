import re

class Student:
    def __init__(self, name, phone, email, passport_series, passport_number, username):
        self.name = name
        self.phone = phone
        self.email = email
        self.passport_series = passport_series
        self.passport_number = passport_number
        self.username = username

    def _validate_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя должно быть непустой строкой.")

    def _validate_phone(self, value):
        if not re.match(r"^\+?[0-9]{10,15}$", value):
            raise ValueError("Телефон должен быть в формате '+79998887766'.")

    def _validate_email(self, value):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value):
            raise ValueError("Некорректный email адрес.")

    def _validate_passport_series(self, value):
        if not re.match(r"^\d{4}$", value):
            raise ValueError("Серия паспорта должна содержать 4 цифры.")

    def _validate_passport_number(self, value):
        if not re.match(r"^\d{6}$", value):
            raise ValueError("Номер паспорта должен содержать 6 цифр.")

    def _validate_username(self, value):
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", value):
            raise ValueError("Имя пользователя должно быть от 3 до 20 символов, включая буквы, цифры и '_'.")

    @property
    def name(self):
        print("Имя прочитано")
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value
        print("На Python")

    @property
    def phone(self):
        print("Телефон прочитан")
        return self._phone

    @phone.setter
    def phone(self, value):
        self._validate_phone(value)
        self._phone = value
        print("На Python")

    @property
    def email(self):
        print("Email прочитан")
        return self._email

    @email.setter
    def email(self, value):
        self._validate_email(value)
        self._email = value
        print("На Python")

    @property
    def passport_series(self):
        print("Серия паспорта прочитана")
        return self._passport_series

    @passport_series.setter
    def passport_series(self, value):
        self._validate_passport_series(value)
        self._passport_series = value
        print("На Python")

    @property
    def passport_number(self):
        print("Номер паспорта прочитан")
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value):
        self._validate_passport_number(value)
        self._passport_number = value
        print("На Python")

    @property
    def username(self):
        print("Имя пользователя прочитано")
        return self._username

    @username.setter
    def username(self, value):
        self._validate_username(value)
        self._username = value
        print("На Python")



student = Student(
    name="Иван Иванов",
    phone="+79998887766",
    email="ivanov@example.com",
    passport_series="1234",
    passport_number="567890",
    username="ivan123"
)

print(student.name)
print(student.phone)

student.name = "Петр Петров"
student.phone = "+78885554433"
print(student.name)

try:
    student.email = "wrong-email-format"
except ValueError as e:
    print(e)