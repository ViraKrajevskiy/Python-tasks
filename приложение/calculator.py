import json
import re
from pprint import pprint
import random
from tabnanny import check

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


    with open("info.json", 'r') as regt:
        check = json.load(regt)

    is_authenticated = any(log["login"] == login and log["password"] == password for log in check.values())

    if is_authenticated:
        print("Отлично, вы вошли в систему.\n")
        return menu()
    else:
         return logit() and print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.")



def read_cash():
    try:
        with open("info.json", "r") as bal:
            dat = json.load(bal)
    except FileNotFoundError:
        print("Файл info.json не найден.")
        dat = {}
    except json.JSONDecodeError:
        print("Ошибка чтения JSON.")
        dat = {}
    return dat

def routr():
    data = read_cash()

    login = input("Введите ваш логин: ")
    card = input("Введите вашу карту: ")

    if card in data and login == data[card].get("login").strip():
        print("Добро пожаловать, {}!".format(data[card]["name"]))
    else:
        print("Пользователь не найден.")
        return False




def account_check():
    card_nuj = input("Введите вашу карту: ")
    password = input("Введите ваш пароль: ")

    with open("info.json", 'r') as regp:
        check = json.load(regp)

    is_authenticated = any(card_nuj["card_number"] == password  and log["cardpass"] == password for log in check.values())

    if is_authenticated:
        print("Отлично, вы вошли в систему.\n")
        return
    else:
        return menu() and print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.")

def cash():
       pass

def account():
        pass


def menu():
    print("1) Проверить баланс или вывести наличные.\n2) Ваш профиль. \n3) Выйти.")
    menu_ch = int(input("Выберите действие: "))
    if menu_ch == 1:
        return routr()
    if menu_ch == 2:
       return account_check()
    elif menu_ch == 3:
        return exit()
    else:
        return menu_ch and print("Неверный выбор, попробуйте снова.")


while True:
    chose = int(input("Здравствуйте, добро пожаловать в программу. Вы можете выбрать одно из условий.\n 1) Зарегистрируйтесь.\n 2) Войти в систему.\n Введите 1 или 2: "))
    if chose == 1:
        inpet()
    elif chose == 2:
        logit()
