n = int(input("Введите значение n: "))

sum_series = sum(1 + i / 10 for i in range(1, n + 1))

print(f"Сумма: {sum_series}")
