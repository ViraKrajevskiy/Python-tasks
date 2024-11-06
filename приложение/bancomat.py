import json
import re
import random

filename = "info.json"

def inpet():
    while True:
        card_number = input("Здравствуйте, введите номер вашей карты (16 цифр): ")
        if len(card_number) == 16 and card_check(card_number):
            break
        else:
            print("Номер карты должен содержать ровно 16 цифр. Попробуйте снова.")

    while True:
        cardpass = input("Введите пароль вашей карты (4 цифры): ")
        if len(cardpass) == 4 and pass_check(cardpass):
            break
        else:
            print("Пароль карты должен содержать ровно 4 цифры. Попробуйте снова.")

    login = input("Придумайте логин или имя пользователя: ")
    password = input("Придумайте пароль: ")

    new_user_data = {
        card_number: {
            "name": input("Введите ваше имя: "),
            "surname": input("Введите вашу фамилию: "),
            "cardpass": cardpass,
            "login": login.strip(),
            "password": password,
            "balance": random.randint(0, 10000)
        }
    }

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if card_number in data:
        print("Карта уже зарегистрирована. Попробуйте войти в систему или используйте другую карту.")
        return

    data.update(new_user_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print("Регистрация успешна!")
    return new_user_data

def card_check(card_number):
    return bool(re.fullmatch(r"\d{16}", card_number))

def pass_check(password):
    return bool(re.fullmatch(r"\d{4}", password))

def logit():
    data = read_cash()
    attempts = 3  

    while attempts > 0:
        card_number = input("Введите номер вашей карты (16 цифр): ")
        cardpass = input("Введите пароль вашей карты (4 цифры): ")

        if card_number in data:
            user_data = data[card_number]
            if user_data["cardpass"] == cardpass:
                print(f"Отлично, вы вошли в систему, {user_data['name']}.\n")
                return menu(card_number)
            else:
                print("Неверный пароль карты.")
        else:
            print("Карта не найдена.")

        attempts -= 1
        print(f"У вас осталось {attempts} попыток.\n")

    print("Превышено количество попыток входа.")
    return

def read_cash():
    try:
        with open(filename, "r") as bal:
            dat = json.load(bal)
    except FileNotFoundError:
        print("Файл info.json не найден.")
        dat = {}
    except json.JSONDecodeError:
        print("Ошибка чтения JSON.")
        dat = {}
    return dat

def routr(card_number):
    data = read_cash()
    user_data = data.get(card_number)

    if not user_data:
        print("Пользователь не найден.")
        return False

    while True:
        print("\n1) Проверить баланс\n2) Вывести наличные\n3) Назад в меню")
        choice = input("Выберите действие (1-3): ")

        if choice == '1':
            print(f"Ваш баланс: {user_data['balance']} рублей.")
        elif choice == '2':
            while True:
                try:
                    amount = float(input("Введите сумму для снятия: "))
                    if 0 < amount <= user_data['balance']:
                        user_data['balance'] -= amount
                        print(f"Успешно снято {amount} рублей. Остаток: {user_data['balance']} рублей.")
                        save_data(data)
                        break
                    else:
                        print("Недостаточно средств или неверная сумма.")
                except ValueError:
                    print("Пожалуйста, введите корректную сумму.")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def account_check(card_number):
    data = read_cash()
    user_data = data.get(card_number)

    if user_data:
        print("\nВаши данные:")
        print(f"Имя: {user_data['name']}")
        print(f"Фамилия: {user_data['surname']}")
        print(f"Логин: {user_data['login']}")
        print(f"Пароль: {user_data['password']}")
        print(f"Баланс: {user_data['balance']} рублей.")

        while True:
            print("\nВыберите действие:")
            print("1) Добавить новую карту")
            print("2) Удалить карту")
            print("3) Вернуться в меню")

            action = input("Введите номер действия (1-3): ")

            if action == '1':
                add_new_card(card_number, data)
            elif action == '2':
                remove_card(card_number, data)
            elif action == '3':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    else:
        print("Пользователь не найден.")

def add_new_card(card_number, data):
    while True:
        new_card_number = input("Введите номер новой карты (16 цифр): ")
        if len(new_card_number) == 16 and card_check(new_card_number):
            if new_card_number in data:
                print("Карта уже зарегистрирована.")
            else:
                break
        else:
            print("Номер карты должен содержать ровно 16 цифр. Попробуйте снова.")

    while True:
        new_cardpass = input("Введите пароль для новой карты (4 цифры): ")
        if len(new_cardpass) == 4 and pass_check(new_cardpass):
            break
        else:
            print("Пароль карты должен содержать ровно 4 цифры. Попробуйте снова.")



    user_data = data[card_number]
    data[new_card_number] = {
        "name": user_data["name"],
        "surname": user_data["surname"],
        "cardpass": new_cardpass,
        "login": user_data["login"],
        "password": user_data["password"],
        "balance": 0
    }

    save_data(data)
    print("Новая карта успешно добавлена.")

def remove_card(card_number, data):
    user_cards = [num for num, info in data.items() if info['login'] == data[card_number]['login']]

    if len(user_cards) < 2:
        print("У вас только одна карта, ее нельзя удалить.")
        return

    print("Ваши карты:")
    for idx, card in enumerate(user_cards, 1):
        print(f"{idx}) {card}")

    while True:
        try:
            choice = int(input("Введите номер карты, которую хотите удалить: ")) - 1
            if 0 <= choice < len(user_cards):
                card_to_remove = user_cards[choice]
                del data[card_to_remove]
                save_data(data)
                print("Карта успешно удалена.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите номер карты для удаления.")

def save_data(data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def account(card_number):
    account_check(card_number)

def menu(card_number):
    while True:
        print("\nМеню:")
        print("1) Проверить баланс или вывести наличные.")
        print("2) Ваш профиль.")
        print("3) Выйти.")
        choice = input("Выберите действие (1-3): ")

        if choice == '1':
            routr(card_number)
        elif choice == '2':
            account(card_number)
        elif choice == '3':
            print("Выход из системы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def main_menu():
    while True:
        print("\nЗдравствуйте, добро пожаловать в программу. Вы можете выбрать одно из условий.")
        print("1) Зарегистрируйтесь.")
        print("2) Войти в систему.")
        print("3) Выйти.")
        chose = input("Введите 1, 2 или 3: ")

        if chose == '1':
            inpet()
        elif chose == '2':
            logit()
        elif chose == '3':
            print("Спасибо за использование программы. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main_menu()
