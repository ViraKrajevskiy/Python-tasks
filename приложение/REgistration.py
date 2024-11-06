
import json
import re
import random
def read_cash():
    try:
        with open("info.json", "r") as bal:
              dat = json.load(bal)
    except FileNotFoundError:
        dat = {}


def routr():
    data= read_cash()

    login = input("Введите ваш логин : ")
    card = input("Ведите вашу карту : ")

    if card and login == data["login"] and data["card_number"]:

        print("Добро пожаловать, !")
    else:
        print("Пользователь не найден.")
        return False

filename = "info.json"

def inpet():
    while True:
        card_number = input("Здравствуйте, введите номер вашей карты (16 цифр): ")
        if len(card_number) == 16 and card_cech(card_number):
            break
        else:
            print("Номер карты должен содержать ровно 16 цифр. Попробуйте снова.")

    while True:
        cardpass = input("Введите пароль вашей карты (4 цифры): ")
        if len(cardpass) == 4 and pas_chek(cardpass):
            break
        else:
            print("Пароль карты должен содержать ровно 4 цифры. Попробуйте снова.")

    new_user_data = {
        card_number: {
            "name": input("Введите ваше имя: "),
            "surname": input("Введите вашу фамилию: "),
            "cardpass": cardpass,
            "login": input("Придумайте логин или имя пользователя: "),
            "password": input("Придумайте пароль: "),
            "balance": random.randint(0, 10000)
        }
    }

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_user_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print("Регистрация успешна!")
    return new_user_data

def card_cech(card_number):
    return bool(re.fullmatch(r"\d{16}", card_number))

def pas_chek(password):
    return bool(re.fullmatch(r"\d{4}", password))

def logit():
    login = input("Введите ваш логин: ")
    password = input("Введите ваш пароль: ")

    with open(filename, 'r') as regt:
        check = json.load(regt)

    is_authenticated = any(log["login"] == login and log["password"] == password for log in check.values())

    if is_authenticated:
        print("Отлично, вы вошли в систему.\n")
        return menu()
    else:
        print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.")
        return logit()

def cash():
    logir = input("Введите ваш логин для проверки баланса: ")
    with open(filename, "r") as bal:
        balance_data = json.load(bal)

    walet = next((user["balance"] for user in balance_data.values() if user["login"] == logir), None)

    if walet is None:
        print("Логин не найден.")
        return

    chosee = int(input("Введите 1, чтобы проверить счет: "))
    if chosee == 1:
        print(f"Ваш баланс: {walet}")

    RetuRnMenu = int(input("Введите 1, чтобы вернуться на выбор, 2 - выйти: "))
    if RetuRnMenu == 1:
        menu()
    else:
        exit()

def account():
    card_number = input("Введите номер вашей карты для доступа к данным: ")
    password = input("Введите пароль вашей карты: ")

    with open(filename, 'r') as regt:
        user_data = json.load(regt)

    user_info = user_data.get(card_number, None)

    if user_info and user_info["cardpass"] == password:
        print("Данные о вас:")
        print(f"Имя: {user_info['name']}")
        print(f"Фамилия: {user_info['surname']}")
        print(f"Логин: {user_info['login']}")
        print(f"Баланс: {user_info['balance']}")

        # Предложить изменить данные
        change = input("Хотите изменить свои данные? (да/нет): ")
        if change.lower() == "да":
            user_info["name"] = input("Введите новое имя: ")
            user_info["surname"] = input("Введите новую фамилию: ")
            user_info["login"] = input("Введите новый логин: ")
            user_info["password"] = input("Введите новый пароль: ")
            # Сохраняем изменения
            with open(filename, 'w') as regt:
                json.dump(user_data, regt, indent=4)
            print("Данные успешно обновлены!")
    else:
        print("Неправильный номер карты или пароль.")

def menu():
    print("1) Проверить баланс или вывести наличные.\n2) Ваш профиль. \n3) Выйти.")
    menu_ch = int(input("Выберите действие: "))
    if menu_ch == 1:
        return cash()
    elif menu_ch == 2:
        return account()
    elif menu_ch == 3:
        exit()
    else:
        print("Неверный выбор, попробуйте снова.")
        return menu()

while True:
    chose = int(input("Здравствуйте, добро пожаловать в программу. Вы можете выбрать одно из условий.\n 1) Зарегистрируйтесь.\n 2) Войти в систему.\n Введите 1 или 2: "))
    if chose == 1:
        inpet()
    elif chose == 2:
        logit()
