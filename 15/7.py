n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Перевернутый массив:", arr)
