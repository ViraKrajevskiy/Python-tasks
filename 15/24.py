n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

d = arr[1] - arr[0]
is_arithmetic = True
for i in range(2, n):
    if arr[i] - arr[i-1] != d:
        is_arithmetic = False
        break

if is_arithmetic:
    print("Массив является арифметической прогрессией")
else:
    print("Массив не является арифметической прогрессией")
