n = int(input("Введите значение n: "))

F = [1, 1]
for k in range(2, n):
    F.append(F[k - 2] + F[k - 1])

print(f"Числа Фибоначчи: {F}")
