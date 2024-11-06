import random


while True:
    try:
        num = int(input("ВВеди число "))
        rn_num = random.randint(1, 10)
        if num == rn_num:
           print('Молодец угадал ')
        else:
            print("Неугадал ха ")
    except ValueError:
        print("Нерпавильно напиши чифру")


