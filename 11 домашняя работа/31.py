n = int(input("Введите значение n: "))

A = [2]
for k in range(1, n):
    A.append(2 + 1 / A[k - 1])

print(f"Последовательность: {A}")
