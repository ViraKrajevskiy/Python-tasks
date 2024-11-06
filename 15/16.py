n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print("Элементы в порядке первый, последний, второй, предпоследний:")
for i in range(n // 2):
    print(arr[i])
    print(arr[n - i - 1])

if n % 2 != 0:
    print(arr[n // 2])
