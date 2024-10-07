a = float(input("Введите значение a: "))
n = int(input("Введите значение n: "))

sum_series = sum((-1)**i * a**i for i in range(n + 1))

print(f"Сумма: {sum_series}")
