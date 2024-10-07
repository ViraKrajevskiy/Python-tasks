N = int(input("Введите значение N: "))

sum_series = sum(i**2 for i in range(1, N + 1))

print(f"Сумма: {sum_series}")
