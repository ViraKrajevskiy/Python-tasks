N = int(input("Введите значение N: "))
K = int(input("Введите значение K: "))

sum_series = sum(i**K for i in range(1, N + 1))

print(f"Сумма: {sum_series}")
