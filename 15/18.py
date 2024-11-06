n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

last_elem = arr[-1]

print("Элементы, которые меньше последнего:")
for i in range(n):
    if arr[i] < last_elem:
        print(arr[i])
