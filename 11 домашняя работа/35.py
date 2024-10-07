n = int(input("Введите значение n: "))

A = [1, 2, 3]
for k in range(3, n):
    A.append(A[k - 1] + A[k - 2] - 2 * A[k - 3])

print(f"Последовательность: {A}")
