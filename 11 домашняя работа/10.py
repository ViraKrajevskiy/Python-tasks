n = int(input("Введите значение n: "))

sum_series = sum(1 / i for i in range(1, n + 1))

print(f"Сумма ряда: {sum_series}")
