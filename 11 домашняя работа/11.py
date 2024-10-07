#from random import randrange
#k = randrange(0,10)
n = int(input("Введите значение n: "))

sum_series = sum((n + i)**2 for i in range(n))

print(f"Сумма: {sum_series}")
