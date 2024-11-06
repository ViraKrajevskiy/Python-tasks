n = int(input("Введите n: "))
K = int(input("Введите K: "))
L = int(input("Введите L: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

sum_elements = 0
for i in range(n):
    if i % K == 0 or i % L == 0:
        sum_elements += arr[i]

print(f"Сумма элементов с индексами, кратными {K} или {L}: {sum_elements}")
