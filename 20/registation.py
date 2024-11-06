import re

def validate_input(pattern, prompt):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Неверный формат. Пожалуйста, попробуйте снова.")

def extract_info():
    name = input("Введите имя и фамилию: ")
    phone = validate_input(r"^\+?\d{9,}$", "Введите номер телефона (минимум 9 цифр): ")
    email = validate_input(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Введите email: ")

    return {
        "name": name,
        "phone": phone,
        "email": email
    }

info = extract_info()
print(info)
