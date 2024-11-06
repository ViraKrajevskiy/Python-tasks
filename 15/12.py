
n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print("Элементы массива с четными индексами:")
for i in range(0, n, 2):
    print(f"arr[{i}] = {arr[i]}")
