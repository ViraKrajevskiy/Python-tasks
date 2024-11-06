
def counter():
    while True:
        num1 = (input())
        ind = str(input())
        num2 = (input())
        oldinp = str(input())

        def n_check():
            if num1.isdigit() and num2.isdigit():
                    return num1 and num2

        def chekc_str():
            if num1 or ind or num2 or oldinp  == "menu":
                return menu()
            else:
                return False

        if ind == '+' and n_check():
            response = int(num1) + int(num2)
            return print(response, "Если хотите выйти в меню введите знак =  ")
        if ind == '-' and n_check():
            response1 = int(num1) - int(num2)
            return print(response1, "Если хотите выйти в меню введите знак = ")
        if ind == '*' and n_check():
            response3 = int(num1) * int(num2)
            return print(response3, "\n Если хотите выйти в меню введите знак = menu" )
        if ind == '/' and n_check():
            response4 = int(num1) / int(num2)
            return print(response4, "Если хотите выйти в меню введите знак = " )
        if chekc_str() == True:
            return menu()
        else:
            return counter()


def menu():
    while True:

            chose_u = (input(
                "Ввыберите действие которые вы хотите совершить. \n В калькулятор: 1 \n Выйти из программы: 2 \n ВВедите свой выбор:"))

            def n_check():
                if chose_u.isdigit():
                    return int(chose_u)
                else:
                    return print('Введи число ишак') or menu()

            if n_check() == 1:
                return counter()
            if n_check() == 2:
                return exit()

menu()

def acount():
    pass



