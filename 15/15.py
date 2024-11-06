n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print("Элементы в порядке возрастания индексов:")
for i in range(n):
    print(arr[i])

print("Элементы в порядке убывания индексов:")
for i in range(n - 1, -1, -1):
    print(arr[i])
