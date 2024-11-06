
n = int(input("Введите n: "))
K = int(input("Введите K: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print(f"Элементы массива, кратные {K}:")
for i in range(n):
    if arr[i] % K == 0:
        print(f"arr[{i}] = {arr[i]}")
