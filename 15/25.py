
n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

r = arr[1] / arr[0]
is_geometric = True
for i in range(2, n):
    if arr[i] / arr[i-1] != r:
        is_geometric = False
        break

if is_geometric:
    print("Массив является геометрической прогрессией")
else:
    print("Массив не является геометрической прогрессией")
