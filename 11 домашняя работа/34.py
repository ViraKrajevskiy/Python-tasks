n = int(input("Введите значение n: "))

A = [1, 2]
for k in range(2, n):
    A.append((A[k - 2] + 2 * A[k - 1]) / 3)

print(f"Последовательность: {A}")
