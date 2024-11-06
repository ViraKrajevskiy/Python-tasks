def logit():
    login = input("Введите ваш логин: ")
    password = input("Введите ваш пароль: ")

    with open("info.json", 'r') as regt:
        check =json.load(regt)

    check_log = any(login == log["login"] for log in check.values())
    check_pass = any(password == pas["password"] for pas in check.values())

    if check_log == check :
        print("Отлично, вы вошли в систему.\n")
        menu()
    else:
        print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.")
        inpet()





import json
from dataclasses import dataclass
from pprint import PrettyPrinter
import random



file_name = "info.json"

def inpet():
    number = str(random.randint(1, 50000))


    variable_name = input("Здравствуйте введите номер вашей карты: ")

    net = {
        {
            "name" : input("Введите ваше имя: "),
            "surname" : input("Введите вашу фамилию: "),
            "cardpass" : input("Пароль вашей карты : "),
            "login" : input("Придумайте логин или имя пользоватлея : "),
            "password" : input(" Придумайте пароль  : "),
        }
    }

    with open("info.json", "a") as regs:
        regs.write(json.dumps(net, indent=4) + "\n")

    return net


def login():
    logir = input("Enter your login: ")
    password = input("Enter your password: ")
    with open("info.json", "r") as regs:
        check = json.load(regs)
    check_log = any(logir == login["login"].replace(" ", " ") for login in check)
    check_pass = any(logir == login["login"].replace(" ", " ") for login in check)

    if check_log and check_pass:
       return True and print("Отлично выы вошли в систему. \n ") and menu()
    else:
        return inpet() and print("Вы не зарегестрировались зарегестрируйтесь")


def minus():
   with open("info.json", "r") as regs:
       data = json.loads(regs)
   passwrd = int(data["Balance"])
   NewBalance = passwrd - cash()

   with open("info.json", "a") as lod:
        append = json.load(lod)
   loaded = append["Balance"] - NewBalance


def cash():
    with open("info.json", "r") as bal:
        balance = json.load(bal)
        walet = balance["Balace"]

    chosee = int(input("Введите вы хотите обналичить или вывести деньги \n 1 Проверить счет  "))
    RetuRnMenu = int(input("если хотите вернуться на выбор нажмите: \n 1) а если хотите вернуться на главную нажмите \n 2) если хотите выйти нажмите \n 3) Выход из программы."))

    if chosee == 1:

       return print(f"Спасибо что пользуйтесь нашим банком. Ваш баланс: {walet}")

    if chosee == 2:

       leftCash = int(input("ВВедите сумму которую хотите вывести: $"))

       if leftCash > walet:
          return print(f"У вас недостаточно денег. Ваш баланс: {walet}")
       if chosee == walet:
           print("Все щяс сумма выведиться.")
           return



def menu():

    menu_ch = int(input())
    if menu_ch == 1:
        cash()
    elif menu_ch== 2:
        print()
    else:
        exit()


while True:
     chose = int(input("Здравствуйте добро пожаловатьв программу калькулятор.Вы можете выбрать эти 2 условия один из них.\n 1) Зарегестрируйтесь если не зарегестрированы. \n 2) Войти в систему. \n ВВедите 1 или 2:  " ))
     if chose == 1:
         inpet()
     if chose == 2:
         login()





def inpet():

    card_number = input("Здравствуйте, введите номер вашей карты: ")


    def card_cech(card_number):
        return bool(re.fullmatch(r"\d{16}", card_number))

    def pas_chek(password):
        return bool(re.fullmatch(r"\d{4}", password))

    new_user_data = {
        card_number: {
            "name": input("Введите ваше имя: "),
            "surname": input("Введите вашу фамилию: "),
            "cardpass": input("Пароль вашей карты: "),
            "login": input("Придумайте логин или имя пользователя: "),
            "password": input("Придумайте пароль: "),
            "balance": random.randint(0, 10000)
        }
    }




    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):\

        data = {}

    data.update(new_user_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print("Регистрация успешна!")
    return new_user_data







def inpet():
    variable_name = input("Здравствуйте, введите номер вашей карты: ")

    Balance = random.randint(0,10000,)

    variable_name = {
        variable_name: {
            "name": input("Введите ваше имя: "),
            "surname": input("Введите вашу фамилию: "),
            "cardpass": input("Пароль вашей карты: "),
            "login": input("Придумайте логин или имя пользователя: "),
            "password": input("Придумайте пароль: "),
            "balance": Balance
        }
    }

    with open("info.json", 'w') as save:
        json.dump( variable_name, save, indent=4)

        save.write("\n")

    return variable_name
