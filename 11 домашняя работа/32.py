n = int(input("Введите значение n: "))

A = [1]
for k in range(1, n):
    A.append((A[k - 1] + 1) / k)

print(f"Последовательность: {A}")
