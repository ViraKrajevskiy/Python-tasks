import random
number = random.randint(-100, 100)
print(f"Число: {number}")

if number > 0 and number % 2 != 0:
    print("Число положительное нечётное")
elif number < 0 and number % 2 == 0:
    print("Число отрицательное чётное")
elif number == 0:
    print("Число равно нулю")
else:
    print("Число не подходит под категорию")
