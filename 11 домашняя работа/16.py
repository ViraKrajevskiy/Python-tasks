a = float(input("Введите значение a: "))
n = int(input("Введите значение n: "))

sum_series = sum(a**i for i in range(1, n + 1))

print(f"Сумма: {sum_series}")
