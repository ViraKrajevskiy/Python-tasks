n = int(input("Введите n: "))
arr = []
for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print("Элементы с четными индексами:")
for i in range(0, n, 2):
    print(arr[i])

print("Элементы с нечетными индексами:")
for i in range(1, n, 2):
    print(arr[i])
